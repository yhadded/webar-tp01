Comment générer TON marqueur personnalisé (Exercice 4)
=======================================================

1. Choisis une image avec beaucoup de contraste et de détails asymétriques
   (les logos ronds/symétriques ou trop simples sont mal détectés par AR.js).

2. Va sur l'outil officiel AR.js :
   https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html

3. Upload ton image -> l'outil génère un aperçu en noir et blanc (le "pattern").
   Vérifie que le pattern reste lisible/contrasté après conversion.

4. Clique sur "Download pattern file" -> un fichier "pattern-xxx.patt" est téléchargé.

5. Renomme-le en :  custom-marker.patt
   et place-le dans ce dossier (exercice4/assets/custom-marker.patt).

6. Imprime aussi l'image ORIGINALE (pas le .patt qui est juste des données) :
   c'est cette image imprimée sur papier que la caméra doit détecter.
   Garde une bordure blanche autour, comme pour le marqueur Hiro.

7. Une fois le fichier .patt en place, exercice4/index.html fonctionnera tel quel :
   il pointe déjà vers "assets/custom-marker.patt".
