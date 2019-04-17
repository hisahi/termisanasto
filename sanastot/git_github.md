# Alku
Englanninkieliset selitykset / English explanations:
https://git-scm.com/docs/gitglossary
https://help.github.com/en/articles/about-issues
https://help.github.com/en/articles/about-pull-requests

Jotain suomenkielistä sanastoa on haettu lähtei stä
https://git-scm.com/book/fi/v1/
https://www.linux.fi/wiki/Git

Itse keksimäni sanat ovat **lihavoitu**.
The terms I coined are in **bold**.

Sanasto on vielä keskeneräinen.

# Sanat

_(n.)_ branch
> An active line of development.
* _(subst.)_ haara
>> Kehityksen aktiivinen osa, esim. _master_ (päähaara) tai jokaista 
>> ominaisuutta varten tehtävä uusi oksa, jossa kehitystyö tehdään ja lopuksi
>> oksa yhdistetään pääoksaan.
- Katso myös: `fork`

---

_(v.)_ to clonbe
> To get oneself a local copy of a repository.
* _(verb.)_ kopioida, kahdentaa

---

_(n.)_ commit
> A single point in the Git history; the entire history of a project is
> represented as a set of interrelated commits
* _(subst.)_ **solminta**
>> Pysyvä muutos.

---

_(v.)_ to commit
> The action of storing a new snapshot of the project’s state in the Git
> history, by creating a new commit representing the current state of the
> index and advancing HEAD to point at the new commit.
* _(verb.)_ **solmia**
>> Tehdä pysyvä muutos.

----

_(n.)_ fast-forward
> A fast-forward is a special type of merge where you have a revision
> and you are "merging" another branch's changes that happen to be a
> descendant of what you have.
* _(subst.)_ pikakelaus

---

_(n.)_ fork
> GitHub: A fork is a copy of a repository. Forking a repository allows you
> to freely experiment with changes without affecting the original project.
* _(subst.)_ haarauma
- Katso myös: `branch`

---

_(n.)_ issue
> On GitHub, a system for tracking ideas, enhancements, tasks,
> or bugs for work.
* _(subst.)_ **seikka**

---

_(v.)_ to merge
> To bring the contents of another branch (possibly from an external
> repository) into the current branch. 
>* _(verb.)_ yhdistää
> Yhdistää jokin ulkoinen haara nykyiseen haaraan.

---

_(n.)_ object
> The unit of storage in Git.
* _(subst.)_ olio

---

_(n.)_ origin
> The default upstream repository.
* _(subst.)_ alkuperä

---

_(v.)_ to pull
> Pulling a branch means to fetch it and merge it.
* _(verb.)_ vetää

---

_(v.)_ to push
> Pushing a branch means to get the branch’s head ref from a remote repository,
> find out if it is an ancestor to the branch’s local head ref, and in that
> case, putting all objects, which are reachable from the local head ref,
> and which are missing from the remote repository, into the remote object
> database, and updating the remote head ref. 
* _(verb.)_ työntää

---

_(n.)_ pull request
> On GitHub, a system for recommending changes to a project,
> requesting the project maintainer or any person with such
> permissions to pull a given branch into the repository.
* _(subst.)_ vetopyyntö, **vetoehdotus**

---

_(n.)_ rebase
> To reapply a series of changes from a branch to a different base,
> and reset the head of that branch to the result.
* _(verb.)_ **sulauttaa**
>> Haaran sulauttaminen esimerkiksi päähaaraan vaihtaa sulautettavan
>> haaran pohjaksi taas päähaaran. Tämän toteuttaakseen kaikki
>> haaran päähaarasta eroavat muutokset kelataan takaisin ja tehdään
>> uudestaan päähaaran vastaavan tilan päälle, jonka jälkeen molemmat
>> haarojen puussa ei ole enää varsinaisesti "haaraa".

---

_(v.)_ to rewind
> To throw away part of the development, i.e. to assign the head
> to an earlier revision.
* _(verb.)_ kelata taaksepäin

---

_(n.)_ staging area
* _(subst.)_ valmistelualue

---

_(n.)_ upstream
* _(subst.)_ ylätaso, **yläjuoksu**

---

_(n.)_ working tree
> The tree of actual checked out files. The working tree normally
> contains the contents of the HEAD commit’s tree, plus any local
> changes that you have made but not yet committed.
* _(subst.)_ työpuu

