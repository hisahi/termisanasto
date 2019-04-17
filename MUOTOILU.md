# Sanastojen muoto
Sanastot ovat Markdown-yhteensopivassa muodossa. Jokaisen sanaston
alussa voi olla Alku-kappale ja lopussa Loppu-kappale, jotka lisätään
joko luotavan sanastoasiakirjan alkuun tai loppuun. Pääasiallinen 
sisältö on Sanat-kappaleessa, jossa jokainen sana on seuraavassa muodossa:

1. Englanninkielinen sana, yhdellä rivillä
2. (Mahdollisesti) englanninkielinen selitys käyttämällä
   Markdownin lainaussyntaksia.
3. Suomenkieliset käännökset; jokaisen rivin alkuun
   tulee `*`.
4. (Mahdollisesti) suomenkielinen selitys, samaan tapaan
   kuin englanninkielinenkin, mutta rivien alussa `>>` eikä `>`.
5. Mahdollinen "katso myös" -osio, yksi kohta per rivi,
   ja rivien alkuun tulee `-`.
6. Jokaisen sanan väliin tulee `---`, joka on Markdownissa
   vaakasuuntainen viiva.

Esimerkiksi:

```
_(v.)_ to commit
> The action of storing a new snapshot of the project’s state in the Git
> history, by creating a new commit representing the current state of the
> index and advancing HEAD to point at the new commit.
* _(verb.)_ **solmia**
>> Tehdä pysyvä muutos.
* Katso myös: `commit`

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




