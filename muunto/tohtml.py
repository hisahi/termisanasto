#!/usr/bin/python3
"""
Muuntaa Markdown-yhteensopivan sanakirjan HTML-muotoon.
"""

import sys, argparse, os.path, textwrap, hashlib, re, datetime

def indent(html, spaces):
    """
    Sisentää HTML-koodia tai muuta tekstiä lisäämällä jokaisen
    rivin alkuun halutun määrän välilyöntejä.
    """
    head = ' ' * spaces
    return os.linesep.join(head + line for line in html.splitlines())

def allowed_in_id(char):
    """
    Kertoo, onko merkki sallittu HTML:n id:ssä.
    """
    return char[0].upper() in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_:.'

def word_to_id(word):
    """
    Muuntaa sanan yhteensopivaksi HTML id:ksi.
    """
    res = ''
    for c in word:
        if allowed_in_id(c):
            res += c
        elif c == ' ':
            res += '_'
        elif c == ')':
            res += ':'
    return res

def safefind(haystack, needle, start = 0):
    """
    Hakee tekstistä tiettyä kohtaa ja palauttaa sijainnin, tai
    tekstin pituuden jos osaa ei löytynyt.
    """
    length = len(haystack)
    # (-1 % (length + 1)) => length
    return haystack.find(needle, start) % (length + 1)

def minfind(haystack, needles, start = 0):
    """
    Hakee tekstistä tietystä kohtaa eri kohtia ja palauttaa sen, joka
    on lähinnä alkua muodossa ("osa", kohta). Jos tuloksia ei löydy
    ollenkaan, palauttaa None.
    """
    length = len(haystack)
    result = None

    for needle in needles:
        match = (needle, safefind(haystack, needle, start))
        if match[1] < length:
            if not result or result[1] > match[1] or (
                    result[1] == match[1] and len(result[0]) < len(match[0])):
                result = match
    return result

def convert_tt_to_links(markdown):
    """
    Muuntaa <tt>...</tt> linkeiksi sanoihin.
    """
    return re.sub(r'<tt>([^<]+)</tt>',
                  lambda m: '<a href="#sanalinkki_{}">{}</a>'.format(
                                        word_to_id(m.group(1)),
                                        m.group(1)),
                  markdown)

def convert_markdown_extra(markdown):
    """
    Muuntaa linkkejä sekä numeroimattomia listoja.
    """
    # linkit
    markdown = re.sub(r"\[([^\"\]]+)\]\(([^)]+)\)",
                  lambda m: "<a href=\"{}\">{}</a>".format(
                                        m.group(1),
                                        m.group(2)),
                  markdown)
    res, bullet, clist = [], "", []

    def end_list():
        nonlocal res, bullet, clist
        if bullet:
            res.append("<ul>")
            for l in clist:
                res.append("    <li>{}</li>".format(l))
            res.append("</ul>")
        clist = []

    for line in markdown.splitlines():
        if line[:2] in ["* ", "- "]:
            pref = line[:2]
            if bullet != pref:
                end_list()
                bullet = pref
            clist.append(line[2:])
        elif line[:2] in ["  "]:
            clist[-1] = clist[-1] + line[2:]
        else:
            end_list()
            bullet = ""
        if not bullet:
            res.append(line)
    end_list()
    return os.linesep.join(res)

def convert_markdown_to_html(markdown, word_links = False):
    """
    Muuntaa Markdown-koodia HTML-muotoon. Tukee **lihavointia** (myös __...__),
    *kursivointia* (myös _..._), ~~yliviivausta~~ ja `tasalevyistä tekstiä`.

    Jos word_links asetetaan todeksi, `sana`-muotoiset kohdat
    muutetaan linkeiksi kyseisiin sanoihin.
    """
    converted, pointer, state = '', 0, set()
    html_tags = {'*': '<i>', '**': '<b>', '~~': '<s>', '`': '<tt>'}
    markdown = markdown.replace("<", "&lt;").replace(">", "&gt;")
    markdown = convert_markdown_extra(markdown)
    in_html = False
    while True:
        result = minfind(markdown,
                ['**', '*', '_', '__', '~~', '`', '>' if in_html else '<'], start = pointer)
        if result is None:
            converted += markdown[pointer:]
            break
        meta, index = result
        if meta in ['<', '>']:
            in_html = not in_html
            tag = meta
        elif in_html:
            tag = meta
        else:
            meta = meta.replace('_', '*') # unify _ => *, __ => **
            tag = html_tags[meta]
            if meta in state:
                tag = tag.replace('<', '</')
            state ^= {meta}
        converted += markdown[pointer:index] + tag
        pointer = len(meta) + index
    if word_links:
        converted = convert_tt_to_links(converted)
    return converted

def prepare_md_block(markdown):
    """
    Muuntaa Markdownin rivinvaihdot HTML-rivinvaihdoiksi.
    """
    return markdown.replace("\n", "<br />")

class SanastoAlku():
    """
    Luokka sanaston Alku-osiolle.

    Ottaa parametrikseen vain tekstin.
    """
    def __init__(self, text):
        self.text = text

    def html(self):
        """
        Palauttaa osion HTML-koodina.
        """
        return textwrap.dedent("""\
                <header>
                    <p>
                {}
                    </p>
                </header>
                """).format(indent(prepare_md_block(convert_markdown_to_html(self.text)), 8))

class SanastoSana():
    """
    Luokka sanaston yhdelle sanalle.

    Ottaa parametrikseen englanninkieliset sanat (listana), suomenkieliset
    sanat (listana) sekä mahdollisesti englanninkielisen kuvauksen,
    suomenkielisen kuvauksen sekä lisärivit.
    """
    def __init__(self, eng, fin, eng_text = '', fin_text = '', extra = []):
        if not eng or not fin:
            raise ValueError('eng ja fin tulee sisältää jotain')
        self.eng, self.fin, self.eng_text, self.fin_text, self.extra = \
                    eng, fin, eng_text, fin_text, extra

    def clean(self):
        """
        Palauttaa sanan 'puhtaassa' muodossa.
        """
        candidate = self.eng[0]
        if ')_' in candidate:
            return word_to_id(candidate.split(')_', 1)[1].strip())
        elif ')' in candidate:
            return word_to_id(candidate.split(')', 1)[1].strip())
        else:
            return word_to_id(candidate)

    def html_id(self):
        """
        Palauttaa tämän sanan HTML id:n.
        """
        return 'sana_' + word_to_id(self.eng[0])

    def html_eng(self):
        return indent("\n".join("<dt>{}</dt>".format(
                    convert_markdown_to_html(w)) for w in self.eng), 12)

    def html_fin(self):
        return indent("\n".join("<dt>{}</dt>".format(
                    convert_markdown_to_html(w)) for w in self.fin), 12)

    def html_see_also(self):
        if not self.extra:
            return ""
        lista = indent(os.linesep.join("<li>{}</li>".format(
                        convert_markdown_to_html(w, word_links = True)) 
                        for w in self.extra), 4)
        return indent(textwrap.dedent("""\
                <ul>
                {}
                </ul>
                    """).format(lista), 8)

    def html(self):
        """
        Palauttaa osion HTML-koodina.
        """
        return textwrap.dedent("""\
                <tr id="sana_{}">
                    <td>
                        <dl>
                {}
                            <dd>
                {}
                            </dd>
                        </dl>
                    </td>
                    <td>
                        <dl>
                {}
                            <dd>
                {}
                            </dd>
                        </dl>
                {}
                    </td>
                </tr>
                """).format(word_to_id(self.eng[0]),
                           self.html_eng(),
                           indent(convert_markdown_to_html(self.eng_text), 16),
                           self.html_fin(),
                           indent(convert_markdown_to_html(self.fin_text), 16),
                           self.html_see_also())

class SanastoSanat():
    """
    Luokka sanaston Sanat-osiolle.

    Ottaa parametrikseen listan SanastoSana-olioita.
    """
    def __init__(self, words):
        self.words = words

    def word_ids(self):
        """
        Palauttaa taulukon sanoista ja niiden varsinaisista id:eistä
        linkkien korjaamista varten.
        """
        result = {}
        for word in self.words:
            clean = word.clean()
            if clean not in result:
                result[clean] = word.html_id()
        return result

    def html(self):
        """
        Palauttaa osion HTML-koodina.
        """
        return textwrap.dedent("""\
                <table>
                    <thead>
                        <tr>
                            <th>Englanniksi / English</th>
                            <th>Suomeksi / Finnish</th>
                        </tr>
                    </thead>
                    <tbody>
                {}
                    </tbody>
                </table>
                """).format(indent("\n".join(word.html()
                                     for word in self.words), 8))

class SanastoLoppu():
    """
    Luokka sanaston Loppu-osiolle.

    Ottaa parametrikseen vain tekstin.
    """
    def __init__(self, text):
        self.text = text

    def html(self):
        """
        Palauttaa osion HTML-koodina.
        """
        return textwrap.dedent("""\
                <footer>
                    <p>
                {}
                    </p>
                </footer>
                """).format(indent(prepare_md_block(convert_markdown_to_html(self.text)), 8))

class SanastoTiedosto():
    """
    Esittää sanastotiedostoa.
    """
    def __init__(self, file):
        self.file = file

    def expect_line(self):
        """
        Lukee rivin tiedostosta ja palauttaa sen, tai palauttaa arvon None
        jos rivejä ei enää ole. Siirtää myös tiedosto-osoittimen seuraavalle
        riville, joten tämän funktion kutsuminen uudelleen ja uudelleen lukee
        tiedoston rivi kerrallaan.
        """
        l = self.file.readline()
        return l.rstrip() if l else None

    def advance_line(self):
        """
        Siirtää tiedosto-osoittimen seuraavalle riville.
        """
        self.file.readline()

    def expect_line_check(self):
        """
        Sama kuin expect_line, muttei siirrä tiedosto-osoitinta seuraavalle
        riville.
        """
        file = self.file
        position = file.tell()
        l = self.expect_line()
        file.seek(position)
        return l

    def has_lines(self):
        """
        Tarkistaa, onko rivejä vielä jäljellä.
        """
        return self.expect_line_check() is not None

    def skip_empty_lines(self):
        """
        Ohittaa rivejä tiedostossa kunnes seuraava rivi ei ole tyhjä.
        """
        while self.has_lines() and '' == self.expect_line_check().strip():
            self.advance_line()

    def expect_heading(self, heading):
        """
        Odottaa kohtaavansa tietyn otsikon, ja palauttaa, löytyikö
        kyseinen otsikko.
        """
        while True:
            l = self.expect_line_check()
            if l is None:
                return False
            elif l.startswith('#'):
                found = l[1:].strip()
                return found.lower() == heading.lower()
            self.advance_line()

    def read_lines_meeting(self, condition, postp):
        """
        Lukee rivejä, jotka täyttävät jonkin ehdon, kunnes ehto
        ei enää täyty. Ehto ja käsittely annetaan funktiona.
        """
        result = []
        while True:
            l = self.expect_line_check()
            if l is None or not condition(l):
                break
            result.append(postp(l))
            self.advance_line()
        return os.linesep.join(result)

    def read_lines_starting_with(self, prefix, strip_prefix = False):
        """
        Lukee rivejä, jotka alkavat jollain alkuosalla, kunnes rivi
        ei enää ala sillä.
        """
        return self.read_lines_meeting(lambda x: x.startswith(prefix),
                                       (lambda x: x[len(prefix):].strip()) 
                                        if strip_prefix
                                        else (lambda x: x.strip()))

    def read_section(self):
        """
        Lukee osion seuraavaan osio-otsikkoon asti.
        """
        return self.read_lines_meeting(lambda x: not x.startswith('#')
                                       or x.startswith('##'),
                                       lambda x: x)

    def expect_nimi(self):
        """
        Lukee tiedostosta sanaston nimen tai palauttaa None, jos sitä
        ei annettu.
        """
        return self.expect_line()

    def expect_alku(self):
        """
        Lukee tiedostosta Alku-osion.
        """
        if not self.expect_heading('Alku'):
            return None
        self.advance_line()
        return SanastoAlku(self.read_section().strip())

    def expect_sana_eng(self):
        """
        Lukee termin englanninkieliset esitysmuodot.
        """
        return self.read_lines_meeting(lambda x: not (x.startswith('*')
                         or x.startswith('>') or x.startswith('-')),
                                       lambda x: x.strip())

    def expect_sana_fin(self):
        """
        Lukee termin suomenkieliset esitysmuodot.
        """
        return self.read_lines_starting_with('*', strip_prefix = True)

    def expect_sana_eng_q(self):
        """
        Lukee termin englanninkielisen selityksen.
        """
        return self.read_lines_meeting(lambda x: x.startswith('>')
                                                 and not x.startswith('>>'),
                                       lambda x: x[1:].strip())

    def expect_sana_fin_q(self):
        """
        Lukee termin suomenkielisen selityksen.
        """
        return self.read_lines_starting_with('>>', strip_prefix = True)

    def expect_sana_extra(self):
        """
        Lukee lisärivit, kuten Katso myös -rivit.
        """
        return self.read_lines_meeting(lambda x: x.startswith('-')
                                                 and not x.startswith('--'),
                                       lambda x: x[1:].strip())

    def expect_sana_sep(self):
        """
        Tarkistaa, onko seuraava rivi sanojen välissä oleva erotin.
        """
        self.skip_empty_lines()
        return (self.expect_line() or '').strip().startswith('---')

    def expect_sanat(self):
        """
        Lukee tiedostosta Sanat-osion.
        """
        if not self.expect_heading('Sanat'):
            return None
        self.advance_line()
        sanat = []
        while True:
            self.skip_empty_lines()
            eng = self.expect_sana_eng().splitlines()
            fin = self.expect_sana_fin().splitlines()
            eng_q = self.expect_sana_eng_q()
            fin_q = self.expect_sana_fin_q()
            extra = self.expect_sana_extra().splitlines()
            sanat.append(SanastoSana(eng, fin, eng_q, fin_q, extra))
            if not self.expect_sana_sep():
                break
        return SanastoSanat(sanat)

    def expect_loppu(self):
        """
        Lukee tiedostosta Loppu-osion.
        """
        if not self.expect_heading('Loppu'):
            return None
        self.advance_line()
        return SanastoLoppu(self.read_section().strip())

def replace_sanalinkki(text, words):
    """
    Korjaa sanalinkit.
    """
    for key in words.keys():
        text = text.replace("#sanalinkki_{}".format(key), "#" + words[key])
    return text

"""
Pääfunktio.
"""
def main():
    parser = argparse.ArgumentParser(description =
        'Muuntaa hisahi/termisanasto-formaatin HTML-muotoon.')
    parser.add_argument('sanasto',
        help='polku sanastoon termisanaston Markdown-yhteensopivassa muodossa')
    parser.add_argument('tulos',
        help='tiedostopolku tuloksena oleva HTML-tiedostolle')

    args = parser.parse_args()
    if not os.path.isfile(args.sanasto):
        print('Sanastotiedostoa ei ole olemassa: {}'.format(args.sanasto),
                            file = sys.stderr)
        return 2

    with open(args.sanasto, 'r', encoding = 'utf-8') as file:
        pfile = SanastoTiedosto(file)

        nimi = pfile.expect_nimi()
        if not nimi:
            print('Sanastotiedoston syntaksissa on vikaa: nimi puuttuu', 
                            file = sys.stderr)
            return 2
        alku = pfile.expect_alku()
        sanat = pfile.expect_sanat()
        if not sanat:
            print('Sanastotiedoston syntaksissa on vikaa: sanat puuttuvat',
                            file = sys.stderr)
            return 2
        loppu = pfile.expect_loppu()
        with open(args.tulos, 'w', encoding = 'utf-8') as output:
            output.write(replace_sanalinkki(textwrap.dedent("""\
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>{0}</title>
                        <meta charset="utf-8">
                        <style type="text/css">
                            td {{
                                border: 1px solid grey;
                                padding: 2px 10px 2px 2px;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1>{0}</h1>
                {1}
                {2}
                {3}
                        <p><i>Päivitetty {4}</i></p>
                    </body>
                </html>
                """).format(nimi,
                           indent(alku.html() if alku else '', 8),
                           indent(sanat.html(), 8),
                           indent(loppu.html() if loppu else '', 8),
                           datetime.datetime.utcnow().isoformat()),
                sanat.word_ids()))
    return 0

if __name__ == '__main__':
    sys.exit(main() or 0)
