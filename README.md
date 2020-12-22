# Trajectory
Algorithme de calcul de trajets basé sur Dijkstra

# Back
Utilisation de l'environnement de dev :  
    - Installer pip pour python 3 : sudo apt-get install python3-pip  
    - Installer VirtualEnv : pip3 install virtualenv  
    - Créer l'environnement virtuel : virtualenv pyenv  
Sous Linux :  
    - Se placer dans le folder ./Back et lancer l'environement de dev : source pyenv/bin/activate  
Sous Windows :  
    - Se placer dans le folder ./Back et lancer l'environement de dev : pyenv\Scripts\activate  

Installation des dépendances par l'utilisation de : pip install -r requirements.txt  
  
Lancer le serveur Back :   
    - cd ./Back/DAO/  
    - gunicorn -b 127.0.0.1:5100 server:app  

# Trajectory API  
Lancer l'API : npm start  
