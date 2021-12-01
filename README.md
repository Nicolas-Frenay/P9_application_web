# P9_application_web
P9_OC-developpeur_python


## Instructions :


1) Installation python :
- Allez sur [https://www.python.org/downloads/](url) , et télécharger la dernière version de python, puis lancez le fichier 
  téléchargé pour l'installer.

2) Télécharger le code :
- Sur le repository github, cliquez sur le bouton "Code", puis "Download ZIP".
- Ensuite décompressez le fichier dans votre dossier de travail.

3) creation environnement virtuel :
- Ouvrez un terminal, puis allez dans votre dossier de travail avec la commande cd.
- Dans le terminal, tapez : ``` python3 -m venv env ```

4) Activer l'environnement virtuel :
  - Si vous êtes sous mac, ou linux :
    - tapez : ```source env/bin/activate ```
  - Si vous êtes sous windows :
    - tapez ```env/Scripts/activate.bat```

5) Installer les modules necessaires :
  - tapez ```pip install -r requirements.txt```
 
6) lancer le server local :
- dans le terminal tapez : ```python3 manage.py runserver```
- Une fois le serveur lancé, vous pourrez accéder au site à l'adresse indiquée dans le terminal ( par defaut : http://127.0.0.1:8000/ )

7) pour couper le serveur local taper <kbd>Ctrl</kbd> + <kbd>C</kbd>

8) Pour fermer l'environnement virtuel :
- Dans le terminal, tapez : ```deactivate ```

(L'environnement virtuel et les modules n'ont besoin d'etre installés qu'une seul fois, par la suite, vous devez juste activer l'environnement virtuel et lancer le serveur.)


comptes de tests/passwords:
- toto : totototo1
- tata : tatatata1
- tutu : tutututu1

compte admin/password :
- LITReview : LITReview
