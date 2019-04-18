Säännöllisten lausekkeiden sanasto

# Alku
Itse keksimäni sanat ovat **lihavoitu**.
The terms I coined are in **bold**.

Sanasto on vielä keskeneräinen (ainahan se!).

# Sanat

_(n.)_ anchor
* _(subst.)_ ankkuri
> A zero-length match that ties the position of the pattern
> to a given part of the text, usually the beginning or end
> of a line.

---

_(n.)_ backreference
* _(subst.)_ takaisinviittaus
> Reference to an earlier group in a pattern.

---

_(n.)_ capturing group
* _(subst.)_ **poimiva ryhmä**
* _(subst.)_ **poimintaryhmä**
* _(subst.)_ tallennusryhmä
* _(subst.)_ tallentava ryhmä
> A group that stores its matched value for use in a 
> substitution.
- Katso myös: `non-capturing group`

---

_(n.)_ character class
* _(subst.)_ merkkiryhmä
> A class of characters that define the allowed
> characters in a given context.

---

_(n.)_ complemented character class
* _(subst.)_ käänteinen merkkiryhmä
> A class of characters that define the forbidden
> characters in a given context.

---

_(v.)_ escape
* _(verb.)_ **peitellä**
* _(verb.)_ eskapoida
> To transform text in such a way that its
> interpretation even in systems where some
> characters have special meanings is still
> literal and equal to the original text.
>> Peittelyn tarkoituksena on esimerkiksi varmistaa,
>> että jotain tekstiä tarkoitetaan sellaisenaan,
>> joten esim. säännöllisissä lausekkeissa tähti (`*`)
>> peitellään kirjoittamalla sen sijaan `\*` tai `[*]`.

---

_(n.)_ escape character
* _(subst.)_ **peittelymerkki**
* _(subst.)_ suojausmerkki
> A character used to signify that the next
> character is to be used literally.

---

_(n.)_ escape sequence
* _(subst.)_ **peittelysarja**
> A combination of the escape character and another
> character used to represent a character that is
> difficult to represent otherwise.

---

_(adj.)_ greedy
* _(adj.)_ ahne
> That matches as much text as possible.

---

_(n.)_ lookahead
* _(subst.)_ **etuvilkaisu**
> A zero-length match that either asserts (positive) 
> or forbids (negative) certain text after another.
>> Etuvilkaisu tarkistaa jonkin tekstin jälkeen olevaa
>> tekstiä ja käyttää sitä ehtona, muttei pidä sitä osana
>> itse täsmäystä. Positiivinen eli vaativa etuvilkaisu
>> vaatii jonkun tekstin olemassaoloa jonkun tekstin jälkeen,
>> kun taas negatiivinen eli kieltävä etuvilkaisu kieltää
>> jonkun tekstin olemassaolon.

---

_(n.)_ lookaround
* _(subst.)_ **vilkaisu**
> A collective term for lookaheads and lookbehinds, two types
> of zero-length matches.
>> Yhteinen termi sekä etu- että takavilkaisuille.

---

_(n.)_ lookbehind
* _(subst.)_ **takavilkaisu**
> A zero-length match that either asserts (positive) 
> or forbids (negative) certain text before another.
>> Takavilkaisu tarkistaa jotain tekstiä ennen olevaa
>> tekstiä ja käyttää sitä ehtona, muttei pidä sitä osana
>> itse täsmäystä. Positiivinen eli vaativa takavilkaisu
>> vaatii jonkun tekstin olemassaoloa ennen jotain tekstiä,
>> kun taas negatiivinen eli kieltävä takavilkaisu kieltää
>> jonkun tekstin olemassaolon.

---

_(n.)_ match
* _(subst.)_ **täsmäys**
> That which has been matched.

---

_(v.)_ match
* _(verbi.)_ täsmätä
> To find some text that corresponds to the given regular
> expression.

---

_(n.)_ metacharacter
* _(subst.)_ metamerkki
> Any character used to refer to something else than
> that character itself.

---

_(n.)_ non-capturing group
* _(subst.)_ **poimimaton ryhmä**
* _(subst.)_ tallentamaton ryhmä
> A group or grouping that does not capture its match.
- Katso myös: `capturing group`

---

_(n.)_ pattern
* _(subst.)_ lauseke
> A regular expression used to search or match text.

---

_(n.)_ subpattern
* _(subst.)_ alilauseke
> A pattern within another pattern.

---

_(n.)_ wildcard
* _(subst.)_ jokerimerkki
> A character matching any other character.



