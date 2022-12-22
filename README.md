# genExam
Le principal objectif de `genExam` est de générer deux documents pdf 
(énoncé et corrigé) d'examen QCM à partir d'une banque de questions au 
format $\LaTeX$.
Le fonctionnement globale est décrit par le diagramme suivant :
``` 
       .tex_ => .tex => .pdf
```
Un ensemble de questions dans un format spécifique `tex_` sont filtrés pour
produire un fichier `tex` de questions individuelles à partir d'un template afin 
d'enrichir un fichier `tex` global. Ce dernier est finalement compilé pour obtenir 
le fichier `pdf` final.

### Exemples de documents générés par `genExam` au format $\LaTeX$ :

#### Enoncé : 
![exemple_enonce_genExam](https://github.com/FilipeVasconcelos/genExam/blob/main/fig/exemple_enonce_genExam.png)
#### Corrigé :
![exemple_corrige_genExam](https://github.com/FilipeVasconcelos/genExam/blob/main/fig/exemple_corrige_genExam.png)


### help :  

L'option `--help` affiche l'ensemble des paramètres du script :
```bash
$ bin/genExam 

Usage : bin/genExam OPTIONS
------------------------------------------------------------------------------
-h/--help            : cette aide
-v/--english         : english version (default non)
-n/--nbQ    [nbQ]    : nombre de questions (default = all of them)
-o/--order  [file]   : fichier donnant l'ordre des questions (default random)
-q/--qtex   [rep]    : répertoire des questions à utliser (default qtex ou qtex_english)
-e/--examen [examen] : nom de l'examen (default = Examen final)
-m/--module [module] : module de l'examen (default = UNIX)
-p/--promo  [promo]  : promotion (default = INGE1)
-a/--annee  [annee]  : année scolaire (default = 2022-2023)
-d/--date   [date]   : date de l'examen (default = None)
```

### Exemples d'appel :
```bash
$ bin/genExam --nbQ 80 --examen="Examen final" --module=UNIX --promo=INGE1 --annee=2022-2023 --date="6 janvier 2023"
```
80 questions sont choisies aléatoirement parmi les questions du répertoire `qtex/`

Avec l'option `--english` ce sont les questions du repertoire `qtex_english/` qui sont
utilisées. 
```bash
$ bin/genExam --english --nbQ 80 --examen="Final exam" --module=UNIX --promo=INGE1 --annee=2022-2023 --date="January 6th 2023"
```

Il est possible de générer un examen à partir d'un fichier listant les questions 
que l'on souhaite utiliser (option `--order`).

### À propos de la banque de questions

La banque de questions est dans un format spécifique (extension `tex_`).

Ce format `.tex_`, qui se veut simple, permet d'envisager deux
types questions/réponses :

- Question à Choix Multiples (CM) :
```
       #Q Une question
       #ANS CM
       A. <réponse_1> ✓
       B. <réponse_2> ✓
       C. <réponse_3>
       D. <réponse_4>
       #TAGS
```
- Question d'Appariement  (A) :
```
       #Q Une question
       #ANS A
       A. <énoncé_1>  1. <réponse_1>
       B. <énoncé_2>  2. <réponse_2>
       C. <énoncé_3>  3. <réponse_3>
       D. <énoncé_4>  4. <réponse_4>
       #TAGS
```

Les `<énoncé_i>` et `<réponse_i>` peuvent contenir des commandes $\LaTeX$. On
terminera la ligne par `✓` pour selectionner la ou les bonnes réponses.

#### Exemple de question de la banque de questions :

##### Choix Multiples
```
#Q Parmi les systèmes d'exploitation ci-dessous, lesquel(s) appartien(nent)t à la famille des systèmes Unix ?
#ANS CM
A. Linux \newline ✓
B. MacOS  \newline ✓
C. Android \newline  ✓
D. MS-DOS \newline
#TAGS #Unix #OS #cours01
```

```
#Q  Which of these syntaxes is correct?
#ANS CM
A. \texttt{if [ \$x -gt \$y ]} \newline ✓
B. \texttt{if \$x -gt \$y} \newline
C. \texttt{if ( \$x -gt \$y )} \newline
D. None of them \newline
#TAGS #if #script #variable #syntaxe #cours08
```
##### Appariement 

```
#Q Associer la commande de filtre avec son résultat
#ANS A
A. \texttt{echo "ab cdef" | cut -d " " -f 2}       1. \texttt{cdef}
B. \texttt{echo "ab cdef" | cut -d " " -f 1}       2. \texttt{ab}
C. \texttt{echo "ab cdef" | cut -c -4}             3. \texttt{ab c}
D. \texttt{echo "ab cdef" | cut -c 3}              4. \texttt{b}
#TAGS #filtre #commandesDeBase #echo #cut #cours11
```

```
#Q  Match commands to their \texttt{man} descriptions
#ANS A
A. \texttt{ls} 1. List directory contents
B. \texttt{cat} 2. Concatenate files and print on the stdout
C. \texttt{rm} 3. Remove files or directories
D. \texttt{cp} 4. Copy files and directories
#TAGS #commandesDeBase #ls #cat #rm #cp #cours01
```

# Credits
- **Filipe Vasconcelos** 
