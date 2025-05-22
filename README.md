# projet 2025 Scooter PMR 

Le scooter PMR est un engin qui permet le déplacement de personne a mobilité réduite. Grace a sa configuration il est bien plus stable qu’un scooter. 
Il est géolocalisable en cas de problème et intègre un GPS sur le poste de pilotage. Ma tache consiste donc à choisir une technologie de géolocalisation et d’intégrer
ce système au scooter, ainsi que de pouvoir envoyer la position du scooter a un tuteur.
Pour réaliser ma tâche j'ai opter pour une programmation en python en utilisant ce code Flask qui permet de créer une petite 
application web où un utilisateur peut partager sa position géographique (latitude et longitude) grâce à son navigateur. 
Quand l’utilisateur clique sur le bouton "Partager", le navigateur utilise la géolocalisation pour récupérer sa position. 
Ensuite, cette position est envoyée au serveur via une requête POST (en JSON). Le serveur, qui fonctionne avec Flask, reçoit 
les coordonnées et les affiche simplement dans la console.L’interface est assez simple : un bouton, un message pour informer 
l’utilisateur, et du JavaScript pour gérer la géolocalisation et l’envoi des données.



