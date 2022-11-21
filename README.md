# Računalniška delavnica - Git

Ta repozitorij je namenjen računalniški delavnici 29. 11. 2022

## Splošno o gitu

Git je sistem za nadziranje različic. To pomeni, da na nek način shranjuje celotno zgodovino naše kode in lahko kadarkoli pogledamo, kako je naša koda zgledala v nekem trenutku zgodovine. Tako imamo na enem mestu shranjeno trenutno verzijo in celotno zgodovino za nazaj.

Git lahko uporabljamo lokalno na svojem računalniku, ali pa tudi na strežniku, kjer lahko sodelujemo tudi z ostalimi programerji. Lahko uporabljamo svoj lasten strežnik, lahko pa kodo shranjujemo na za to namenjene strežnike, kot naprimer pri Githubu, Gitlabu, Bitbucketu ... Git torej ni isto kot Github. Github je samo grafični vmesnik, ki v ozadju poganja git ukaze in nam zagotovi prostor na strežniku, da našo kodo lahko delimo s svetom (ali pa samo s partnerji, s katerimi sodelujemo na projektu).

Git navadno uporabljamo v terminalu, obstajajo pa tudi desktop aplikacije, ki omogočajo uporabo git s pomočjo grafičnega vmesnika. Pri tem je treba opozoriti, da v aplikacijah navadno nimamo vključenih vseh funkcij, medtem ko v terminalu lahko naredimo vse. Osnovne ukaze za git lahko izvajamo tudi s pomočjo urejevalnikov kode, kot je naprimer VS Code. Ta nam omogoča vse funkcionalnosti, ki jih vsakodnevno potrebujemo.

## Navodila za namestitev

Na operacijskem sistemu macOS je git že nameščen. To lahko vseeno preverimo tako, da v terminal napišemo `git --version`. Če dobimo odgovor `git version 2.34.1`, je git že nameščen. Številka na koncu se lahko razlikuje.

Če git še ni naložen, ga je potrebno naložiti.

- na debian based distribucijah linuxa to storimo z ukazom `sudo apt install git-all`.
- na fedora based distribucijah linuxa z `sudo dnf install git-all`.
- na macOS, če git še ni nameščen, sledite navodilom v terminalu, ki se izpišejo ko poženete ukaz `git --version`.
- za operacijski sistem Windows, lahko git naložite s pomočjo [spletne strani](https://git-scm.com/download/win).

## Osnovne nastavitve

### SSH ključ

Ker gita običajno ne želimo uporabljati samo lokalno, ampak tudi na strežniku, želimo to početi varno. Ne bi želeli, da lahko v našem repozitoriju kodo spreminja kdorkoli, pač pa samo "pooblaščene" osebe. V ta namen obstaja SSH ključ. SSH ključ pride v dveh delih. En je naš privatni ključ, ki ga imamo shranjenega na računalniku, drugi pa je javni ključ, ki ga shranimo na strežnik. Ko torej želimo poslati spremembe na strežnik, bo git preveril, ali se ključa ujemata. Če se ne, spremembe ne moremo izvesti.

#### Pridobivanje SSH ključa

Ključ ustvarimo s pomočjo terminala. če vtipkamo `cd ~/.ssh`, se lahko zgodi dvoje. Če mapa še ne obstaja, ključa verjetno še nismo ustvarili. Če mapa že obstaja, lahko z ukazom `ls` dobimo imena vseh datotek, ki se v tej mapi nahajajo. Če se v mapi nahajata datoteki oblike `id_[nekineki]` in `id_[nekineki].pub`, ključ že obstaja. V tem primeru ga lahko uporabljamo. Sicer ključ generiramo na novo. To storimo tako, da poženemo ukaz `ssh-keygen -t ed25519 -C "username"`. pri tem `ed25519` predstavlja kodiranje, ki ga uporabimo za generiranje ključa, za `username` pa lahko napišemo karkoli, saj je to komentar. Dobro je, da ga napišemo tako, da bomo vedeli kje ga uporabljamo. Naprimer, če želimo ta ključ uporabljati za Github, lahko napišemo uporabniško ime ali mail, ki ga uporabljamo za Github. Ko pritisnemo Enter, nas terminal vpraša, kako želimo shraniti ključ. Če je to naš prvi ključ, lahko pritisnemo Enter in bo uporabil privzeto ime, ki je `id_ed25519`.

Če je ključ že ustvarjen, lahko nov ključ dodamo na enak način. Pri tem je treba paziti, da ne uporabimo privzetega imena, saj bi s tem povozili stari ključ, ki bi s tem nehal delovati. Zato, ko nas vpraša za ime, napišemo celotno pot. Naprimer `/home/gasper/.ssh/id_ed25519_github`. Če želimo ključ uporabljati, ga moramo dodati v ssh-agent. to storimo z dvema ukazoma:

```
$ eval "$(ssh-agent -s)"
$ ssh-add ~/.ssh/<ssh_key_name>
```

> TODO: dodajanje ključa v github (in gitlab)

### Nastavitve gita

Najprej je potrebno ustvariti git repozitorij. To lahko storimo na dva načina.

1.) Lahko ustvarimo mapo, ki bo postala repozitorij, v terminalu navigiramo do ustvarjene mape in poženemo `git init`. Potem je treba nastaviti uporabniško ime in mail. To storimo z ukazoma:

```
$ git config --global user.name "rzgdmqt"
$ git config --global user.email "gasperzajdela@gmail.com"
```

S tem smo nastavili uporabniško ime in mail globalno, in ga bo git uporabljal za vse git repozitorije. Če želimo nastaviti ime in mail samo za trenutni repozitorij, spustimo `--global`.

Nato na githubu ustvarimo prazen repozitorij in sledimo navodilom, ki nam jih da github.

2.) Druga možnost je, da repozitorij ustvarimo na Githubu in ga nato kloniramo na mesto, kjer ga želimo imeti. Ko ustvarjamo repozitorij na Githubu, moramo vanj dodati vsaj eno datoteko (običajno README.md), ki nam jo Github že ponudi. Potem sledimo navodilom na Githubu.

Naslednji korak je, da si nastavimo privzet urejevalnik besedila, ki ga bo git tudi uporabljal za izpisovanje in urejanje datotek. To storimo z ukazom

- Normalni OS:

```
$ git config --global core.editor <ime_urejevalnika>
```

- Windows:

```
$ git config --global core.editor "'C:/Program Files/Notepad++/notepad++.exe' -multiInst -notabbar -nosession -noPlugin"
```

## Delo z gitom

V gitu imajo lahko datoteke 3 stanja:

- modified: spremembe, ki jih naredimo v urejevalniku in jih shranimo na računalniku, git si jih ne zapomni.
- staged: stanje, kamor damo datoteke, za katere želimo, da jih git shrani.
- committed: datoteke v tem stanju so shranjene v git.

Osnovni gradniki gita so torej commiti, saj so commiti tisto, kar beleži zgodovino našega projekta. Commit se zgradi tako, da git najprej poračuna checksum celotnega repozitorija in ustvari hash (SHA-1), ki je sestavljen iz 40 znakov v hexadecimalnem zapisu. Nato ustvari objekt, ki vsebuje:

- hash commita
- hash prejšnjega commita
- sporočilo, ki ga zapišemo, ko ustvarimo commit
- avtorja projekta (lastnik repozitorija)
- committerja (tistega, ki je ustvaril commit)
- drevo "blobov"

Blob se v gitu imenujejo daoteke, ki jih imamo v repozitoriju. V vsakem commitu si git zapomni vse datoteke in si poračuna njihove hashe. Če se kaka datoteka ne spremeni, si zapomni hash datoteke iz prejšnjega commita.

### Delo z gitom lokalno

Najprej si poglejmo, kako z gitom delamo sami (torej brez kontributorjev). Ko smo ustvarili (ali klonirali) repozitorij, lahko v njem spreminjamo datoteke. Ko želimo spremembe zabeležiti v zgodovino, moramo ustvariti commit. Najprej pogledamo, kakšno je stanje našega repozitorija

```
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        main.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Zaenkrat si poglejmo le del `Changes not staged for commit`. Vidimo, da je README.md datoteka označena z `modified`, kar pomeni, da smo jo spreminjali, nismo pa je dodali za commitanje. Pod `Untracked files` vidimo datoteko `main.py`. Untracked pomeni, da te datoteke pred zadnjim commitom še nismo imeli shranjene. V obeh primerih, če želimo gitu povedati, da si želimo, da si zapomni spremembe, to storimo tako, da napišemo ukaz `git add` in naštejemo kaj želimo dodati.

```
$ git add README.md main.py
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md
        new file:   main.py
```

Če želimo dodati vse, kar se dodati da (v našem primeru README.md in main.py), lahko uporabimo tudi `git add .`, ki doda vse spremenjene datoteke in datoteke, ki jih še nismo imeli v preteklosti.

Ko so datoteke dodane, jih lahko commitamo. To storimo tako, da poženemo ukaz `git commit`, ki odpre v terminalu urejevalnik, ki smo ga nastavili za privzetega in vanj lahko napišemo sporočilo commita. Za sporočilo lahko napišemo karkoli med 0 in 50 znakov, vendar je smiselno, da v sporočilu nakratko napišemo, kaj smo spremenili (to nam bo koristilo kasneje). Druga možnost je tudi, da napišemo `git commit -m "sporočilo"`, ki ustvari commit s sporočilom "sporočilo". Več napotkov glede commitov sledi kasneje. S tem smo ustvarili nov zabeležek v zgodovini.

Kadar želimo pogledati v zgodovino, nam pri tem pomaga ukaz `git log`, ki nam pokaže celotno zgodovino commitov in za njih prikaže hash, avtorja, datum in sporočilo commita.
če želimo pogledati, kako je naša koda zgledala v nekem commitu, rabimo kopirati nekaj prvih znakov hasha (več kot 8 in vsaj toliko, da nista 2 commita enaka v vseh prvih znakih). Potem poženemo `git checkout f4dce6b6`, ki nas prestavi v trenutek zgodovine, ko smo commitali f4dce6b6. Če se želimo vrniti nazaj v sedanjost, poženemo `git checkout -`, kar je isto kot `git checkout main`, ki v tem trenutku predstavlja sedanjost. če se želimo iz preteklosti preseliti v malo mlajšo zgodovino (naprimer za dva commita naprej), potrebujemo hash. Tokrat je problem, če poženemo `git log`, saj nam ta ukaz prikaže le commite v preteklosti od trenutka, kjer se nahajamo sedaj. Če pa želimo izpisati vse commite, ki so v preteklosti in v prihodnosti, poženemo `git log --all`. Več načinov kako prikazovati log, si lahko pogledate spodaj v tabeli.

Včasih želimo naše trenutno delo nadaljevati na drugem računalniku. V ta namen lahko naše lokalne spremembe shranimo na Github. To storimo tako na sledeč način:

```
$ git remote add origin git@github.com:<username>/<repository_name>.git
$ git push -u origin main
```

Prvi ukaz pravi, da nastavimo `remote`, ki ga poimenujemo `origin` in dodamo povezavo do našega repozitorija na githubu. Drugi ukaz pa "potisne" naš repozitorij v `origin`, torej remote repozitorij.

Ko želimo delo nadaljevati na drugem računalniku prvič, moramo najprej repozitorij klonirati. To storimo z ukazom:

```
$ git clone git@github.com:<username>/<repository_name>.git
```

Ko delo končamo, je treba ponovno pognati push. Vsakič naslednjič, ko bomo želeli nadaljevati delo (na tem ali na starem računalniku), pa bo potrebno z githuba povlečti spremembe. To storimo z ukazom:

```
$ git pull origin
```

Po končanem delu, pa ne smemo pozabiti na push.

_Opomba: Če želimo na drugem računalniku spreminjati kodo, moramo tudi na drugem računalniku nastaviti ssh ključ in ga dodati v github._

### Delo z gitom v skupini

Kadar delamo v skupini z nekom drugim, želimo imeti nek "remote" repozitorij, kamor lahko vsi shranjujemo svoje spremembe. To lahko storimo tako, da na Githubu ustvarimo repozitorij in vanj kot kontributorje dodamo ljudi, ki sodelujejo z nami na projektu. Tako lahko vsak klonira projekt in na njem ustvarja spremembe. Spremembe pa se dogajajo samo lokalno. Če jih želimo poslati na remote, poženemo

> TODO

### Veje v gitu

Veje v gitu so v resnici pointerji na commite, zato so veje "poceni" (ne zasedejo dodatnega prostora). Veje uporabljamo, kadar želimo nekaj testirati in nismo prepričani, ali bo stvar delovala. Takrat ustvarimo svojo vejo, na njej ustvarjamo spremembe, jih commitamo, kot običajno, na koncu pa, če smo z delom zadovljni, lahko vejo združimo (merge) v našo glavno vejo, če pa z delom nismo zadovoljni, lahko vejo pobrišemo, ali pa pustimo pri miru, če bomo kdaj želeli na njej nadaljevati delo.

Novo vejo ustvarimo tako, da poženemo `git branch <branch_name>`. To nam ustvari novo vejo, vendar nas ne preusmeri avtomatično na njo. Da se na novo vejo prestavimo, poženemo `git checkout <branch_name>`, ali pa `git switch <branch_name>`. Razlika med `switch` in `checkout` je, da pri prvem se git pritoži, če dobi npr. commit namesto imena veje, `checkout` pa gre lahko tudi na commit (kot smo videli že prej).

Ko smo z delom na veji zadovoljni, lahko vejo priključimo naši main veji. To najlažje storimo tako, da gremo na vejo main in tam poženemo `git merge <branch_name>`, kjer je branch_name ime veje s katere želimo delo priključiti. Git pri tem ustvari `merge commit`, torej nov commit, ki ima dva starša, torej obe veji iz katerih smo delo združili. Ni nujno, da vedno združimo vejo na main. Veje lahko med sabo poljubno združujemo, iz vej lahko naredimo poljubno število vej.

Več o tem, si lahko preberete v razdelku merge, rebase, cherry-pick.

### Napotki za commite

Kadar delamo v skupini, je še toliko bolj pomembno, da so sporočila commitov jasna in zgovorna. Kadar poženemo `git commit`, brez značke `-m`, se nam odpre urejevalnik, kamor lahko napišemo daljše sporočilo. Prva vrstica je kratek in jedrnat opis, po prazni vrstici pa lahko sledi daljše sporočilo. Primer template:

```
Capitalized, short (50 chars or less) summary

More detailed explanatory text, if necessary. Wrap it to about 72
characters or so. In some contexts, the first line is treated as the
subject of an email and the rest of the text as the body. The blank
line separating the summary from the body is critical (unless you omit
the body entirely); tools like rebase will confuse you if you run the
two together.

Write your commit message in the imperative: "Fix bug" and not "Fixed bug"
or "Fixes bug." This convention matches up with commit messages generated
by commands like git merge and git revert.

Further paragraphs come after blank lines.

- Bullet points are okay, too

- Typically a hyphen or asterisk is used for the bullet, followed by a
single space, with blank lines in between, but conventions vary here

- Use a hanging indent
```

Dobra praksa je, da se commita čim več. V smislu, da se vsaj vsako zaključeno celoto commita posebej, saj to kasneje olajša delo za debuganje ali merganje.

### merge

### rebase, cherry-pick

### Git v praksi

## .gitignore

Včasih želimo, da določenih datotek git ne bo sledil. V ta namen lahko ustvarimo datoteko z imenom `.gitignore`. V njej z nekoliko poenostavljenim regexom določimo obliko imena datotek, za katere želimo, da jim git ne sledi. V .gitignore naprimer navedemo tiste datoteke (ali mape), ki se naredijo same pri poganjanju projekta. Datoteko v terminalu ustvarimo z ukazom `touch .gitignore` in jo uredimo tako da poženemo `<editor_name> .gitignore`, vsebino izpišemo z ukazom `cat .gitignore`.

Primer .gitignore:

```
# ignore all .a files
*.a
# but do track lib.a, even though you're ignoring .a files above
!lib.a
# only ignore the TODO file in the current directory, not subdir/TODO
/TODO
# ignore all files in any directory named build
build/
# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt
# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf
```

Na [povezavi](https://github.com/github/gitignore) so predloge za .gitignore datoteke glede na tip (programski jezik) projekta, na katerem delate. Lahko imamo .gitignore datoteke tudi v podmapah. Vsak .gitignore povozi vse .gitignore datoteke iz "višjih" map.

## Cheatsheet

V tem razdelku se nahajajo najpogostejši ukazi, ki jih potrebujemo za git. Vse ukaze poženemo kot `git <command_name> -fl1 -fl2 -fl... --flag1 --flag2 --flag...`, kjer je `<command_name>` ime ukaza, `-fl#` je krajše ime za `--flag#`, ki predstavlja dodatne specifikacije za ukaz. Nekatere zastavice vzamejo tudi argumente, ki jih preprosto navedemo za imenom zastavice. Zastavice, ki so na voljo, lahko napišemo `git help <command>` in nam git izpiše vse kaj ukaz `command` zna.

### Setup

| Command |            Flag            |                                      Description                                      |                 Example                 |                      Additional                       |
| :-----: | :------------------------: | :-----------------------------------------------------------------------------------: | :-------------------------------------: | :---------------------------------------------------: |
|  init   |                            |                    trenuten direktorij spremeni v git repozitorij                     |                git init                 |                                                       |
| config  |             -e             |            odpre config datoteko v kateri lahko nastavljamo spremenljivke             |              git config -e              |
|         | --global `<var>` `<value>` |  globalno (za vse repozitorije) nastavi spremenljivko `<var>` na vrednost `<value>`   | git config --global user.name "rzgdmqt" | user.name, user.mail, core.editor init.defaultBranch  |
|         | --local `<var>` `<value>`  | lokalno (za trenutni repozitorij) nastavi spremenljivko `<var>` na vrednost `<value>` | git config --local user.name "rzgdmqt"  | user.name, user.mail, core.editor, init.defaultBranch |
|         |           --list           |          izpiše nastavitve za repozitorij (tako lokalne, kot tudi globalne)           |                                         |
