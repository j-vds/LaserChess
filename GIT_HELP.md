# Git CheatSheet

## Een repo opzetten
**Zonder vooraf gegeven code**
1. Surf naar <https://github.ugent.be> en klik op *new repository*
2. Kies een naam voor je repository en voeg een .gitignore en README bestand toe. Voor de .gitignore kan je kiezen uit de templates voorzien op github of je kan zelf een .gitignore file aanmaken. Als je in VS Code werkt, vergeet dan niet de volgende lijnen toe te voegen:
    ```bash
    .vscode/*
    !.vscode/tasks.json
    !.vscode/c_cpp_properties.json
    !.vscode/launch.json
    ```
    Deze zorgen ervoor dat je lokale VS Code instellingen niet naar GitHub gepusht worden, maar dat de standaard config files wel gepusht worden.  
3. Voeg een collaborator toe via `settings` > `collaborators`
4. Clone je repo lokaal
```bash
$ git clone https://github.ugent.be/username/repo.git
```

**Met vooraf gegeven code**
1. Maak een repo aan zonder files en voeg eventuele collaborators toe
2. Ga naar je lokale map waar deze code staat en open daar Git Bash
3. Initialiseer hier een git repo, voeg alle bestanden toe, commit en zet je remote branch, push daarna alles naar origin master (als je geen .gitignore gekregen hebt, zal je hier zelf een .gitignore file moeten aanmaken)
```bash
$ git init
$ git add .
$ git commit -m "Add all code files"
$ git remote add origin https://github.ugent.be/username/gitworkshop.git
$ git push -u origin master
```
## Bekijken welke files gewijzigd zijn
```bash
$ git status
```

## Files toevoegen voor een volgende commit
*  Alle files in de huidige folder
```bash
$ git add .
```
* Een specifieke file
```bash
$ git add <file>
```
## Commit message toevoegen
```bash
git commit -m "commit message"
```
*Let op: Indien je hier enkel git commit typt, zou het kunnen dat Git Bash je naar een VIM editor stuurt, voor informatie hierover verwijzen we je naar de [VIM sectie](##VIM)*

## Bestand naar je remote repository sturen (na commit)

```bash
$ git push
```
*Indien dit niet lukt, bestaat de upstream branch voor je huidige branch waarschijnlijk niet, [Branching](##Branching) gaat hier dieper op in.*
## Wijzigingen binnenhalen van de remote directory
```bash
$ git pull
```
## Lokale wijzigingen even aan de kant zetten
*Dit commando kan handig zijn indien je nieuwe wijzigingen wil binnenhalen zonder dat je je lokale wijzigingen, die nog niet gecommit zijn, wil committen of als je even naar een andere branch wil zonder je lokale wijzigingen te committen*
```bash
$ git stash
```
## Aan de kant gezette wijzigingen terug plaatsen
```bash
$ git stash pop
```
*Opgepast dit kan leiden tot een merge conflict (meer info over hoe deze op te lossen vind je in de [merge sectie](##Merging))*

## Lokale wijzigingen ongedaan maken 

* Nog niet toegevoegd
```bash
$ git checkout <file>
```

* Toegevoegd, maar nog niet gecommit
```bash
$ git reset HEAD <file>
$ git checkout <file>
```
* Reeds gecommit, maar nog niet gepusht
```bash
$ git reset HEAD~1
$ git checkout <file>
```
## Branching
* Een nieuwe branch aanmaken die aftakt vanop een tweede branch
```bash
$ git branch <new_branch> <branch_2>
```
* Start een nieuwe branch die aftakt vanop een tweede branch en ga er meteen naar toe
```bash
$ git checkout -b <new_branch> <branch_2>
```
* Bekijk alle lokale branches
```bash
$ git branch
```
* Push een nieuwe branch naar de remote
```bash
$ git push --set-upstream origin <branch>
```
* Naar een specifieke branch gaan
```bash
$ git checkout <branch>
```

## Merging
* Merge een branch in de huidige branch
```bash
$ git merge <branch>
```
### Een merge conflict oplossen
Merge conflicten ontstaan wanneer je twee branches wil mergen die dezelfde code aangepast hebben. Git weet bijgevolg niet welke wijzigingen moeten behouden blijven en welke er mogen weggegooid worden.  
 * Lokaal oplossen  
     Indien je lokaal een merge conflict hebt ziet je file er als volgt uit:
     ```bash
     <<<<<<<< <branch>  
     Some Text 1  
     ===========
     Some Text 2
     >>>>>>>> HEAD 
     ```
     Wat onder de ==== lijn staat, zijn de wijzigingen op je huidige branch, wat erboven, staat, zijn de wijzigingen op de branch die je in de huidige branch wil mergen. Nu moet jij zelf beslissen welke wijzigingen je wil behouden.  
     Na het oplossen van het merge conflict moet je de file opnieuw toevoegen en pushen
     ```bash
     $ git add <file>
     $ git commit -m "Solved merge conflict"
     $ git push
     ```
* Oplossen via een pull request  
    Een pull request is een gemakkelijke manier om je merge conflicten op het spoor te komen, zonder dat je eerst lokaal moet mergen. De volgende stappen leggen uit hoe je dit best doet.  

     1.  Push alle (nodige) files van je huidige branch naar de remote repo
     ```bash
     $ git add <file1> <file2> <file3>
     $ git commit -m "Commit message"
     $ git push
     ```
     2. Surf naar je repo op github en ga naar de tab *pull requests*
     3. Open een nieuw pull request met als base branch de branch waarin je wil mergen en compare branch de branch die erin gemerged moet worden.
     4. Klik op create pull request, nu zie je normaal een dat weergeeft of er merge conflicts zijn. Indien dit het geval is, klik op resolve conflicts en los je merge conflicts op zoals hierboven beschreven.
     5. Nadat je je merge conflict opgelost hebt, kan je gewoon op merge pull request klikken om je merge te laten doorgaan.
     6. Haal de nieuwe wijzigingen binnen
     ```bash
     $ git pull
     ```

## VIM
Git Bash gebruikt als standaard text editor VIM. VIM is een tekst editor die volledig bestuurd kan worden met het toetsenbord en dit zorgt soms voor problemen. Git Bash opent VIM automatisch als bij een fast-forward merge na een `git pull` (nieuwe wijzigingen worden dan automatisch in je huidige branch gemerged, zonder merge conflicts) of als je `git commit` typt zonder een commit message. Hieronder worden een paar simpele typs gegeven om met VIM te werken (meer geavanceerde info kan je [hier](https://vim.fandom.com/wiki/Vim_Tips_Wiki) vinden)

### Toevoegen en verwijderen van tekst
* Toevoegen voor de cursor: `i`
* Toevoegen na de cursor: `a`
* Nieuwe lijn starten onder de cursor: `o`
* Nieuwe lijn starten boven de cursor: `O`
* Insert modus verlaten: `ESC`
* Karakter verwijderen dat na de cursor staat: `x`
* Volledig woord verwijderen dat na de cursor staat: `dw`
* De huidige lijn volledig verwijderen: `dd`

## VIM verlaten
1) Zorg ervoor dat je zeker niet meer in Insert modus zit (`ESC`)
* Wijzingen opslaan zonder verlaten: `:w`
* Wijzingen opslaan en VIM verlaten: `:wq`
* VIM verlaten zonder wijzigingen: `:q!`  
(Pas op dit zorgt er vaak voor dat je commit niet doorgaat)


*Voor meer uitegebreidere informatie over git dan wat er in deze cheat sheet staat, verwijzen we je naar de [Git Book](https://git-scm.com/book/en/v2)*