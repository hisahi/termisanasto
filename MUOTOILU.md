# Sanastojen muoto
Sanastot ovat Markdown-yhteensopivassa muodossa. Niiden ensimmäinen rivi
on aina sanaston nimi tai muu otsikko, joka on pakollinen. Jokaisen sanaston
alussa voi olla Alku-kappale ja lopussa Loppu-kappale, jotka lisätään
joko luotavan sanastoasiakirjan alkuun tai loppuun. Pääasiallinen 
sisältö on Sanat-kappaleessa, jossa jokainen sana on seuraavassa muodossa:

1. Englanninkielinen sana, yksi rivi termiä kohden (yleensä vain yksi)
2. Suomenkieliset käännökset; jokaisen rivin alkuun
   tulee `*`.
3. (Mahdollisesti) englanninkielinen selitys käyttämällä
   Markdownin lainaussyntaksia.
4. (Mahdollisesti) suomenkielinen selitys, samaan tapaan
   kuin englanninkielinenkin, mutta rivien alussa `>>` eikä `>`.
5. Mahdollinen "katso myös" -osio, yksi kohta per rivi,
   ja rivien alkuun tulee `-`. Jokainen rivi koetaan omaksi
   rivikseen HTML-taulukossa.
6. Jokaisen sanan väliin tulee `---`, joka on Markdownissa
   vaakasuuntainen viiva.

Esimerkiksi:

```
_(v.)_ to merge
* _(verb.)_ yhdistää
> To bring the contents of another branch (possibly from an external
> repository) into the current branch. 
>> Yhdistää jokin ulkoinen haara nykyiseen haaraan.
- Katso myös: `rebase`
- Katso myös: `branch`

---
```

Suomenkielisessä sanastossa lihavoidut termit ovat pääosin
minun (Sampo Hippeläisen) ehdotuksia, joiden toivoisin tulevan
laajempaan käyttöön.

# Lyhenteet

* _(adj.)_ = adjective / adjektiivi
* _(n.)_ = noun ~ (subst.)
* _(puh.)_ = puhekielessä
* _(slg.)_ = slangi
* _(subst.)_ = substantiivi ~ (n.)
* _(v.)_ = verb ~ (verb.)
* _(verb.)_ = verbi ~ (v.)




