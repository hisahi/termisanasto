Git- ja GitHub-sanasto

# Alku
Englanninkieliset selitykset / English explanations:
* [https://git-scm.com/docs/gitglossary](https://git-scm.com/docs/gitglossary)
* [https://help.github.com/en/articles/about-issues](
   https://help.github.com/en/articles/about-issues)
* [https://help.github.com/en/articles/about-pull-requests](
   https://help.github.com/en/articles/about-pull-requests)

Jotain suomenkielistä sanastoa on haettu lähteistä
* [https://git-scm.com/book/fi/v1/](https://git-scm.com/book/fi/v1/)
* [https://www.linux.fi/wiki/Git](https://www.linux.fi/wiki/Git)

Itse keksimäni sanat ovat **lihavoitu**.
The terms I coined are in **bold**.

Sanasto on vielä keskeneräinen (ainahan se!).

# Sanat

_(n.)_ branch
* _(subst.)_ haara
> An active line of development.
>> Kehityksen aktiivinen osa, esim. _master_ (päähaara) tai jokaista 
>> ominaisuutta varten tehtävä uusi oksa, jossa kehitystyö tehdään ja lopuksi
>> oksa yhdistetään pääoksaan.
- Katso myös: `fork`

---

_(n.)_ checkout
* _(subst.)_ haaranvaihto
> The action of updating all or part of the working tree with a tree
> object or blob from the object database, and updating the index
> and HEAD if the whole working tree has been pointed at a new branch.

---

_(v.)_ clone
* _(verb.)_ kopioida
* _(verb.)_ kahdentaa
> To get oneself a local copy of a repository.

---

_(n.)_ commit
* _(subst.)_ talletus
* _(subst.)_ **sitoutus**
* _(subst.)_ **varastointi**
* _(subst.)_ vahvistus
* _(subst.)_ pysyvä muutos
* _(subst.)_ **solminta**
* _(subst.)_ **solmittu muutos**
> A single point in the Git history; the entire history of a project is
> represented as a set of interrelated commits.
>> Pysyvä muutos.

---

_(v.)_ commit
* _(verb.)_ tallettaa
* _(verb.)_ **sitouttaa**
* _(verb.)_ **varastoida**
* _(verb.)_ vahvistaa
* _(verb.)_ **solmia**
> The action of storing a new snapshot of the project’s state in the Git
> history, by creating a new commit representing the current state of the
> index and advancing HEAD to point at the new commit.
>> Tehdä pysyvä muutos.

---

_(n.)_ fast-forward
* _(subst.)_ pikakelaus
> A fast-forward is a special type of merge where you have a revision
> and you are "merging" another branch's changes that happen to be a
> descendant of what you have.

---

_(v.)_ fetch
* _(verb.)_ hakea
> Fetching a branch means to get the branch’s head ref from a remote
> repository, to find out which objects are missing from the local
> object database, and to get them, too.

---

_(n.)_ fork
* _(subst.)_ haarauma
> GitHub: A fork is a copy of a repository. Forking a repository allows you
> to freely experiment with changes without affecting the original project.
- Katso myös: `branch`

---

_(n.)_ index
* _(subst.)_ indeksi
* _(subst.)_ hakemisto
> A collection of files with stat information, whose contents are stored 
> as objects. The index is a stored version of your working tree.

---

_(n.)_ issue
* _(subst.)_ **aloite**
* _(subst.)_ ehdotus
> On GitHub, a system for tracking ideas, enhancements, tasks,
> or bugs for work.

---

_(v.)_ merge
* _(verb.)_ yhdistää
> To bring the contents of another branch (possibly from an external
> repository) into the current branch. 
>> Yhdistää jokin ulkoinen haara nykyiseen haaraan.
- Katso myös: `rebase`

---

_(n.)_ object
* _(subst.)_ olio
> The unit of storage in Git.

---

_(n.)_ origin
* _(subst.)_ alkuperä
> The default upstream repository.

---

_(v.)_ pull
* _(verb.)_ vetää
> Pulling a branch means to fetch it and merge it.

---

_(v.)_ push
* _(verb.)_ työntää
> Pushing a branch means to get the branch’s head ref from a remote repository,
> find out if it is an ancestor to the branch’s local head ref, and in that
> case, putting all objects, which are reachable from the local head ref,
> and which are missing from the remote repository, into the remote object
> database, and updating the remote head ref. 

---

_(n.)_ pull request
* _(subst.)_ vetopyyntö
* _(subst.)_ **vetoehdotus**
> On GitHub, a system for recommending changes to a project,
> requesting the project maintainer or any person with such
> permissions to pull a given branch into the repository.

---

_(n.)_ rebase
* _(verb.)_ **varrentaa**
> To reapply a series of changes from a branch to a different base,
> and reset the head of that branch to the result.
>> Haaran varrentaminen (käsite kasvien jalostuksesta) esimerkiksi
>> päähaaraan vaihtaa varrennettavan haaran pohjaksi taas päähaaran.
>> Tämän toteuttaakseen kaikki haaran päähaarasta eroavat muutokset
>> kelataan takaisin ja tehdään uudestaan päähaaran vastaavan
>> tilan päälle, jonka jälkeen molemmat haarojen puussa ei ole
>> enää varsinaisesti "haaraa".
- Katso myös: `merge` 

---

_(n.)_ ref (reference)
* _(subst.)_ viittaus

---

_(n.)_ repository
* _(subst.)_ tietolähde
* _(subst.)_ tietovarasto
* _(subst.)_ tietosäilö
* _(subst.)_ tietosäiliö
* _(subst. slg.)_ repo

---

_(v.)_ rewind
* _(verb.)_ kelata taaksepäin
> To throw away part of the development, i.e. to assign the head
> to an earlier revision.

---

_(n.)_ staging area
* _(subst.)_ valmistelualue

---

_(n.)_ tag
* _(subst.)_ **lippu**
* _(subst.)_ merkintä
> A ref under `refs/tags/` namespace that points to an object of an
> arbitrary type (typically a tag points to either a tag or a commit object).

---

_(n.)_ upstream
* _(subst.)_ ylätaso
* _(subst.)_ **yläjuoksu**

---

_(n.)_ working directory
* _(subst.)_ työhakemisto

---

_(n.)_ working tree
* _(subst.)_ työpuu
> The tree of actual checked out files. The working tree normally
> contains the contents of the HEAD commit’s tree, plus any local
> changes that you have made but not yet committed.

