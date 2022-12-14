# Računalniška delavnica - Git

Ta repozitorij je namenjen računalniški delavnici 8. 12. 2022

## Splošno o gitu

Git je sistem za nadziranje različic. To pomeni, da na nek način shranjuje celotno zgodovino naše kode in lahko kadarkoli pogledamo, kako je naša koda zgledala v nekem trenutku zgodovine. Tako imamo na enem mestu shranjeno trenutno verzijo in celotno zgodovino za nazaj.

Git lahko uporabljamo lokalno na svojem računalniku, ali pa tudi na strežniku, kjer lahko sodelujemo tudi z ostalimi programerji. Lahko uporabljamo svoj lasten strežnik, lahko pa kodo shranjujemo na za to namenjene strežnike, kot naprimer pri Githubu, Gitlabu, Bitbucketu ... Git torej ni isto kot Github. Github je samo grafični vmesnik, ki v ozadju poganja git ukaze in nam zagotovi prostor na strežniku, da našo kodo lahko delimo s svetom (ali pa samo s partnerji, s katerimi sodelujemo na projektu).

Git navadno uporabljamo v terminalu, obstajajo pa tudi desktop aplikacije, ki omogočajo uporabo git s pomočjo grafičnega vmesnika. Pri tem je treba opozoriti, da v aplikacijah navadno nimamo vključenih vseh funkcij, medtem ko v terminalu lahko naredimo vse. Osnovne ukaze za git lahko izvajamo tudi s pomočjo urejevalnikov kode, kot je naprimer VS Code. Ta nam omogoča vse funkcionalnosti, ki jih vsakodnevno potrebujemo.

## Navodila za namestitev

Na operacijskem sistemu macOS je git že nameščen. To lahko vseeno preverimo tako, da v terminal napišemo `git --version`. Če dobimo odgovor `git version 2.34.1`, je git že nameščen. Številka na koncu se lahko razlikuje.

Če git še ni naložen, ga je potrebno naložiti.

- na debian based distribucijah linuxa to storimo z ukazom `sudo apt install git-all`.
- na fedora based distribucijah linuxa s `sudo dnf install git-all`.
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

Ko je ključ ustvarjen, ga lahko dodamo na strežnik. Na Githubu gremo na nastavitve za naš profil (v desnem zgornjem kotu kliknemo na našo sliko profila, in izberemo settings). Na levi strani v meniju izberemo opcijo `SSH and GPG keys`. Klinknemo na zelen gumb `New SSH key`. Za title napišemo karkoli, saj je to le oznaka, da vemo za kaj bomo ta ključ uporabljali. Key type pustimo na Authentication Key. V polje Key nalepimo naš javni ključ (vsebino datoteke `id_[nekineki].pub`). Na koncu pritisnemo Add SSH key in smo končali.

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
- avtorja kode (tistega, ki je kodo spisal)
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

### Veje v gitu

Veje v gitu so v resnici pointerji na commite, zato so veje "poceni" (ne zasedejo dodatnega prostora). Veje uporabljamo, kadar želimo nekaj testirati in nismo prepričani, ali bo stvar delovala. Takrat ustvarimo svojo vejo, na njej ustvarjamo spremembe, jih commitamo, kot običajno, na koncu pa, če smo z delom zadovljni, lahko vejo združimo (merge) v našo glavno vejo, če pa z delom nismo zadovoljni, lahko vejo pobrišemo, ali pa pustimo pri miru, če bomo kdaj želeli na njej nadaljevati delo.

Novo vejo ustvarimo tako, da poženemo `git branch <branch_name>`. To nam ustvari novo vejo, vendar nas ne preusmeri avtomatično na njo. Da se na novo vejo prestavimo, poženemo `git checkout <branch_name>`, ali pa `git switch <branch_name>`. Razlika med `switch` in `checkout` je, da pri prvem se git pritoži, če dobi npr. commit namesto imena veje, `checkout` pa gre lahko tudi na commit (kot smo videli že prej).

Ko smo z delom na veji zadovoljni, lahko vejo priključimo naši main veji. To najlažje storimo tako, da gremo na vejo main in tam poženemo `git merge <branch_name>`, kjer je branch_name ime veje s katere želimo delo priključiti. Git pri tem ustvari `merge commit`, torej nov commit, ki ima dva starša, torej obe veji iz katerih smo delo združili. Ni nujno, da vedno združimo vejo na main. Veje lahko med sabo poljubno združujemo, iz vej lahko naredimo poljubno število vej.

Več o tem, si lahko preberete v razdelku merge, rebase, cherry-pick.

### Delo z gitom v skupini

Kadar delamo v skupini z nekom drugim, želimo imeti nek "remote" repozitorij, kamor lahko vsi shranjujemo svoje spremembe. To lahko storimo tako, da na Githubu ustvarimo repozitorij in vanj kot kontributorje dodamo ljudi, ki sodelujejo z nami na projektu. Tako lahko vsak klonira projekt in na njem ustvarja spremembe. Spremembe pa se dogajajo samo lokalno. Če jih želimo poslati na remote, poženemo `git push origin`. To deluje lepo, dokler ne ustvarimo nove veje, ali pa kdo drug že pred nami pusha svoje delo.

V praksi zato običajno naredimo svojo vejo in na veji naredimo spremembe in nato pushamo vejo na strežnik, ko pa so veje stabilne jih pridružimo v master. Vejo objavimo na strežnik na sledeč način:

```
git push -u <remote> <branch_name>:<branch_name>
```

Ki naredi vejo in na strežnik objavi vejo z istim imenom. Vsakič naslednjič, lahko naše delo objavimo na to vejo tako, da preprosto poženemo `git push`.

Želimo si tudi, da je naš repozitorij sinhroniziran z repozitorijem na strežniku, zato vsakič predno želimo pushati in predno začnemo delati poženemo `git fetch <remote>`, ki na naš računalnik prenese spremembe s strežnika. Nato, če so spremembe prisotne, poženemo `git pull --all`, ki nam posodobi vse spremembe, na vseh vejah.

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

Včasih želimo združiti datoteke z različnih vej, ki se med sabo razhajajo. Takrat, če poženemo `git merge` dobimo konflikt, ki ga moramo razrešiti. Recimo, da imamo v repozitoriju datoteko `moje_besedilo.txt` z naslednjo vsebino:

```
Pozdravljen, svet!
```

To datoteko smo dodali v commit in ustvarili novo vejo ki izhaja iz tega commita. Na obeh vejah (main in veja1), smo to datoteko spreminjali, na koncu pa ju želimo združiti. Na veji veja1 besedilo izgleda tako:

```
Pozdravljen, svet!
Kako lepo vreme je danes! Kot nalašč za učenje algebre. :)
```

Na veji main pa besedilo izgleda tako:

```
Pozdravljen, svet!
Algebre pa res ne maram. :(
Ok no, recimo da ni tok slaba ;)
```

Ko na veji main poženemo `git merge veja1`, dobimo konflikt:

```
Auto-merging moje_besedilo.txt
CONFLICT (content): Merge conflict in moje_besedilo.txt
Automatic merge failed; fix conflicts and then commit the result.
```

Če sedaj pogledamo v datoteko `moje_besedilo.txt`, bo izgledala nekako tako:

```
Pozdravljen, svet!
<<<<<<< HEAD
Algebre pa res ne maram. :(
Ok no, recimo da ni tok slaba ;)
=======
Kako lepo vreme je danes! Kot nalašč za učenje algebre. :)
>>>>>>> veja1
```

Vidimo, da nam je git označil kje so nastali konflikti. Tako se lahko odločimo, kaj želimo obdržati. Med HEAD in enačaji je besedilo, ki se nahaja na naši veji, pod enačaji in nad veja1 pa je kaj prihaja z druge veje. Popravimo besedilo na

```
Pozdravljen, svet!
Algebre pa res ne maram. :(
Kako lepo vreme je danes! Kot nalašč za učenje algebre. :)
```

in poženemo `git commit -a -m "merged HEAD and veja1"`.

<!-- ### rebase, cherry-pick

### Git v praksi -->

## .gitignore

Včasih želimo, da določenih datotek git ne bo sledil. V ta namen lahko ustvarimo datoteko z imenom `.gitignore`. V njej z nekoliko poenostavljenim regexom določimo obliko imena datotek, za katere želimo, da jim git ne sledi. V .gitignore naprimer navedemo tiste datoteke (ali mape), ki se naredijo same pri poganjanju projekta. Datoteko v terminalu ustvarimo z ukazom `touch .gitignore` in jo uredimo tako da poženemo `<editor_name> .gitignore`, vsebino izpišemo z ukazom `cat .gitignore`. Datoteko `.gitignore` lahko ustvarite tudi na vam ljubi način, vendar pozor, datoteke katerih imena se začno z piko, jih v osnovi računalnik v grafičnem vmesniku ne prikaže. Na linuxu skrite datoteke pokažemo z `ctrl + h` na macOS `command + shift + .`, na ostalih operacijskih sistemih naložite dual boot linux. :)

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

V tem razdelku se nahajajo najpogostejši ukazi, ki jih potrebujemo za git. Vse ukaze poženemo kot `git <command_name> -fl1 -fl2 -fl... --flag1 --flag2 --flag...`, kjer je `<command_name>` ime ukaza, `-fl#` je krajše ime za `--flag#`, ki predstavlja dodatne specifikacije za ukaz. Nekatere zastavice vzamejo tudi argumente, ki jih preprosto navedemo za imenom zastavice. Če želimo preveriti katere zastavice ukaz sprejme lahko poženemo `git help <command>` in nam git izpiše vse kaj ukaz `command` zna.

### Setup

|          Command           |           Flag           |                                                       Description                                                        |                      Example                       |                                                                             Additional                                                                             |
| :------------------------: | :----------------------: | :----------------------------------------------------------------------------------------------------------------------: | :------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|       clone \<repo>        |                          | Klonira repozitorij na mesto kjer se nahajamo. Klonira celotno zgodovino, z vsemi commiti in vejami, ki so na strežniku. | git clone git@github.com:rzgdmqt/delavnica_git.git |                                                                                                                                                                    |
|            init            |                          |                                      trenuten direktorij spremeni v git repozitorij                                      |                      git init                      |                                             če želimo, da repozitorij ni več git repozitorij, poženoemo `rm -rf .git`                                              |
|           config           |            -e            |                              odpre config datoteko v kateri lahko nastavljamo spremenljivke                              |                   git config -e                    |
|                            | --global \<var> \<value> |                     globalno (za vse repozitorije) nastavi spremenljivko \<var> na vrednost \<value>                     |      git config --global user.name "rzgdmqt"       |                                        user.name, user.mail, core.editor init.defaultBranch, alias.\<alias> <git_commands>                                         |
|                            | --local \<var> \<value>  |                   lokalno (za trenutni repozitorij) nastavi spremenljivko \<var> na vrednost \<value>                    |       git config --local user.name "rzgdmqt"       |                                             user.name, user.mail, core.editor, init.defaultBranch, remote.pushDefault                                              |
|                            |          --list          |                            izpiše nastavitve za repozitorij (tako lokalne, kot tudi globalne)                            |                 git config --list                  |
|       rm \<filename>       |                          |                                           odstrani datoteko z imenom filename                                            |                  git rm README.md                  |                 namesto filename lahko damo tudi celo pot. Naprimer `git rm log/\*.log` odstrani v podmapi log vse datoteke, ki se končajo s .log.                 |
|                            |   --cached \<filename>   |                                   odstrani datoteko z imenom filename s "staged area"                                    |             git rm --cached README.md              |                                                                                                                                                                    |
| mv `<file_from> <file_to>` |                          |                                         preimenuje datoteko file_from v file_to                                          |             git mv README.md readme.md             | uporablja se tudi za prestavljanje datotek med mapami, torej če bi pognali `git mv README.md README/README.md`, bi datoteko README.md prestavilo v podmapo README. |

### Git ukazi

|                      Command                      |              Flag               |                                                                                            Description                                                                                             |                                                  Example                                                   |                                                                                                                                                                             Additional                                                                                                                                                                              |
| :-----------------------------------------------: | :-----------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                      status                       |                                 |                                            Pokaže stanje repozitorija, koliko commitov smo zadaj/spredaj in kaj smo spreminjali, dodali, odstranili ...                                            |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                       diff                        |                                 |                                                                              Pokaže kaj se je v datotekah spremenilo.                                                                              |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |            --staged             |                                                                       Pokaže kaj se je spremenilo pri datotekah ki so staged                                                                       |                                                                                                            |                                                                                                                                                                         Enako kot --cached                                                                                                                                                                          |
|           add \<file1> \<file2> \<...>            |                                 |                                                                                  Doda naštete datoteke "on stage"                                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                      commit                       |                                 |                                                                  Odpre (core) urejevalnik, v katerega napišemo sporočilo commita                                                                   |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |       -m "commit message"       |                                                                            Ustvari commit s sporočilom "commit message"                                                                            |                                 git commit -m "V README.md dodal poglavje"                                 |
|                                                   |             --amend             |                                                       Odstrani zadnji commit, da lahko popraviš (dodaš datoteke, popraviš sporočilo commita)                                                       | `git commit -m "pozabil sem dodati README.md"; git add README.md; git commit --amend -m "Dodal README.md"` |                                                                                                                  Uporabljaj samo lokalno, saj če pushaš, nato spreminjaš in potem spet pushaš, uničiš delo ostalim, ki izhajajo iz tvojega commita                                                                                                                  |
|                                                   |               -a                |                                                              Doda v commit vse datoteke, ki so sledene do sedaj, pa so se spremenile.                                                              |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|             push \<remote> \<branch>              |                                 |                                                                                 Na remote pošlje našo vejo branch                                                                                  |                                                                                                            |                                                                                                                  Če namesto \<branch> napišemo \<branch>:\<branch_remote>, bo <branch_remote> označeval na katero vejo želimo potisniti spremembe                                                                                                                   |
|                                                   |              --all              |                                                                                     Na remote pošlje vse veje                                                                                      |                                           git push origin --all                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |               -u                |                          Na remote pošlje vejo branch in si zapomni, da naslednjič, ko poženemo pull brez argumentov, je remote veja, s katere želimo povlečti spremembe.                          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |            --delete             |                                                                                       Pobriše vejo na remote                                                                                       |                                       git push origin --delete veja1                                       |                                                                                                                                                                                                                                                                                                                                                                     |
|               fetch \<remote_name>                |                                 |                                           Pogleda če so na remote_name kake spremembe in jih potegne na naš računalnik (ne na naš lokalni repozitorij!)                                            |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|               merge \<from_branch>                |                                 |                                                                              V trenutno vejo združi vejo from_branch.                                                                              |                                                                                                            |                                                                                                                               Včasih naletimo na konflikte, ki jih je potrebno razrešiti. Po merge nastane commit, ki ima dva starša.                                                                                                                               |
|                                                   |            --squash             |                                                                 Zgleda kot merge, ampak ostane na trenutni veji in vej ne združi.                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                  pull \<remote>                   |                                 |                                                                      Z \<remote> potegne spremembe v naš lokalni repozitorij.                                                                      |                                                                                                            |                                                                                                                                                                  Deluje podobno kot fetch + merge                                                                                                                                                                   |
|                      remote                       |                                 |                                                                              Pokaže kaj je remote za trenutni branch                                                                               |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |               -v                |                                                        Pokaže vse remote ki jih imamo in še url kam lahko pushamo in od kod lahko fetchamo.                                                        |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|           remote add \<shortname> \<url>            |                                 |                                                                  Doda remote, z imenom shortname, ki je dostopen na povezavi url                                                                   |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|               remote show \<remote>                |                                 |                                                          Pokaže vse podatke o remote (kaj dela push, fetch, katere veje kažejo nanj ...).                                                          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|        remote rename \<old_name> \<new_name>        |                                 |                                                                                          Očitno kaj dela.                                                                                          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|            remote remove <remote_name>            |                                 |                                                                                          Očitno kaj dela.                                                                                          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                 checkout \<file>                  |                                 |                                                                          Pobriše vse spremembe narejene na datoteki file                                                                           |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|              checkout <branch_name>               |                                 |                                                                                  Se prestavi na vejo branch_name.                                                                                   |                                                                                                            |                                                                                                                                                                Enako kot `git switch <branch_name>`                                                                                                                                                                 |
|             checkout -b <branch_name>             |                                 |                                                                          Ustvari vejo branch_name in se prestavi na njo.                                                                           |                                                                                                            |                                                                                                                                                               Enako kot `git switch -c <branch_name>`                                                                                                                                                               |
| checkout -b <branch_name> \<remote>/<branch_name> |                                 |                                                                      Naredi novo vejo in v njo shrani vejo remote/branch_name                                                                      |                                                                                                            |                                                                                                                                                           Krajše lahko samo `git checkout <branch_name>`                                                                                                                                                            |
|               branch <branch_name>                |                                 |                                                                              Iz trenutnega commita ustvari novo vejo.                                                                              |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                      branch                       |                                 |                                                                                          Pokaže vse veje.                                                                                          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |     --delete \<branch_name>     |                                                                                    Izbriše vejo \<branch_name>                                                                                     |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |  --move \<branch1> \<branch2>   |                                                                             Preimenuje vejo branch1 v branch2 lokalno                                                                              |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |     -u \<remote>/\<branch>      |                                                                         Nastavi upstream za trenutno vejo na remote/branch                                                                         |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |               -vv               |                                                                                 Pokaže veje in njihove upstreame.                                                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |               -v                |                                                                                   Pokaže veje in zadnje commite                                                                                    |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                  restore \<file>                  |                                 |                                                                            Datoteko da nazaj na stanje zadnjega commita                                                                            |                                                                                                            |                                                                                                                                                                    Podatki so lahko izgubljeni!                                                                                                                                                                     |
|                                                   |            --staged             |                                                                                 Datoteko odstrani iz staged area.                                                                                  |                                       git restore --staged README.md                                       |                                                                                                                                                                       Podatki niso izgubljeni                                                                                                                                                                       |
|                 revert \<commit>                  |                                 |                                                           Naredi nov commit, ki razveljavi spremembe commita \<commit>, kjer se nahajamo                                                            |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |        -m #num \<commit>        |                                           Naredi nov commit, ki razveljavi merge commit in ostane na veji kjer smo, če damo za #num 2, gre na drugo vejo                                           |                                            git revert -m 1 HEAD                                            |                                                                                                                            Če revertamo merge commit, in želimo spet mergati veji, dobimo da je up to date! Zato je treba spet revertat.                                                                                                                            |
|                                                   |           --no-commit           |                                                                Obnovi datoteke, kot so bile v starem commitu, ampak jih ne commita                                                                 |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                  reset \<commit>                  |                                 |                                              Prestavi celotno vejo na predhodnika commita \<commit>, pri čemer je vse od \<commit> naprej izgubljeno                                               |                                                                                                            |                                                                                                Podatki so lahko izgubljeni! Če resetu podamo pot do datoteke namesto commita, bo dano datoteko v tistem commitu unstage-al in ohranil spremembe. (nasprotje od add)                                                                                                 |
|                                                   |             --soft              |                                                                    Razveljavi \<commit>, ohrani spremembe na delovnem drevesu.                                                                     |                                                                                                            |                                                                                                                                    S tem lahko squashamo commite, če poženemo `git reset --soft <commit>` in potem `git commit`                                                                                                                                     |
|                                                   |             --mixed             |                                                  Je default nastavitev. Se vrne v trenutek kjer smo naredili \<commit> in unstage-a vse datoteke.                                                  |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |             --hard              |                                                                      Pobriše vse commite od vključno commita \<commit> naprej                                                                      |                                                                                                            |                                                                                                                                      !!!zelo nevarno!!! Če resetamo commite, na katerih sloni delo ostalih, bodo hude težave.                                                                                                                                       |
|                        log                        |                                 |                                                        Pokaže commite v zgodovini. Za vsak commit pokaže hash, autorja, datum in sporočilo.                                                        |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |             --stat              |                                                                          Pokaže tudi, kaj se je po datotekah spreminjalo.                                                                          |                                                                                                            |
|                                                   |        --pretty=oneline         |                                                                       Pokaže samo hash in sporočilo commita, v eni vrstici.                                                                        |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |   --pretty=format: `<format>`   |                                                                              Pokaže format v obliki, kot jo določimo.                                                                              |                                git log --pretty=format "%h - %an, %ar : %s"                                | Opcije za format %H - hash, %h - okrajšan hash, %T - hash drevesa, %t - kratek hash drevesa, %P - hash starša, %p - okrajšano ime starša, %an - avtorjevo ime, %ae - avtorjev email, %ad - autorjev čas, %ar - relativen avtorjev čas, %cn - commiterjevo ime, %ce commiterjev mail, %cd - commiterjev čas, %cr - relativen commiterjev čas, %s - sporočilo commita |
|                                                   |             --graph             |                                                                         Pokaže graf, kako si sledijo commiti z razvejanji.                                                                         |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                rebase \<branch_to>                |                                 |                                                                         Vejo kjer smo, bo poskusil rebaseat na branch_to.                                                                          |                                                                                                            |                                                                                                                                Če pride do konfliktov, jih moraš razrešit in potem daš `git add <file_name>; git rebase --continue`                                                                                                                                 |
|                                                   | --onto \<b1> \<b2> \<...> \<bn> |                                          Če bn izhaja iz b(n-1), ki izhaja iz ..., ki izhaja iz b2, ki izhaja iz b1, naredi rebase iz veje bn na vejo b1                                           |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|               cherry-pick \<commit>               |                                 |                                                                          Vzame commit in ga da na vrh naše trenutne veje.                                                                          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                       stash                       |                                 |                                                                                   Shrani trenutno delo na stack.                                                                                   |                                                                                                            |                                                                                                                                       Če ne želimo commitati, ampak vseeno želimo menjati vejo, lahko delo shranimo na stack.                                                                                                                                       |
|                                                   |          --keep-index           |                                                                                 Doda na stack in ohrani spremembe.                                                                                 |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |       --include-untracked       |                                                                                 V stash vključi nesledene datoteke                                                                                 |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                                                   |              --all              |                                                                             V stash vključi tudi ignorirane datoteke.                                                                              |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                    stash list                     |                                 |                                                                                     Pokaže kaj imamo stashano.                                                                                     |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                    stash apply                    |                                 |                                                                                       Uporabi zadnji stash.                                                                                        |                                                                                                            |                                                                                                                                                          Če želimo specificirat stash, dodamo stash@{#num}                                                                                                                                                          |
|                                                   |             --index             |                                                                                Če želiš da stash ostane na stacku.                                                                                 |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                    stash drop                     |                                 |                                                                                       Odstrani zadnji stash.                                                                                       |                                                                                                            |                                                                                                                                                          Če želimo specificirat stash, dodamo stash@{#num}                                                                                                                                                          |
|          stash branch \<new_branch_name>          |                                 |                                                         Naredi novo vejo iz mesta kjer smo stashali, uporabi spremembe in odstrani stash.                                                          |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |        <command>                                                              |
|                rev-parse \<branch>                |                                 |                                                                         Pokaže hash od commita, kjer se nahaja veja branch                                                                         |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                      reflog                       |                                 |                                                                   Pokaže zgodovino, kje se je glava (HEAD) nahajala v zgodovini.                                                                   |                                                                                                            |                                                                                                                                                                                                                                                                                                                                                                     |
|                    show \<ref>                    |                                 | Pokaže kako je repozitorij izgledal v času \<ref>. možnosti za \<ref> so: HEAD@{#num}, HEAD@{2.months.ago} (ali kakšno drugo časovno obdobje), HEAD^#num HEAD~#num, \<commit>^#num, \<commit>~#num |                                                                                                            |                                                                                                  ^ se uporablja za merge commite. Če je #num = 1 je to veja kjer smo, če je #num = 2, pokaže vejo s katere smo mergali, ~#num pomeni #num linearnih commitov nazaj                                                                                                  |
| filter-branch --tree-filter 'rm -f \<file>' HEAD  |                                 |                                                                               Iz zgodovine odstrani datoteko \<file>                                                                               |                                                                                                            |                                                                                                                           !!!ZELO NEVARNO!!! enako kot `git filter-branch --index-filter 'git rm --cached --ignore-unmatch <file>' HEAD`                                                                                                                            |
