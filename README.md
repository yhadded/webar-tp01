# ST2AWD - TP01 - WebAR

Projet WebAR (A-Frame + AR.js) réalisé pour le TP01. Chaque exercice est un dossier
autonome avec son propre `index.html`, pour pouvoir les tester/noter séparément et
avoir une URL GitHub Pages par exercice.

```
webar-tp01/
├── index.html            # page d'accueil qui liste les 6 exercices
├── exercice1/index.html  # scène 3D A-Frame (pas d'AR, juste la scène)
├── exercice2/index.html  # AR.js + marqueur Hiro, boîte semi-transparente animée
├── exercice3/index.html  # interaction clic/tap (couleur + vitesse/échelle)
├── exercice4/            # marqueur personnalisé
│   ├── index.html
│   └── assets/README.txt # comment générer TON .patt
├── exercice5/            # QR code + marqueur Hiro combinés
│   ├── index.html
│   ├── generate_qr.py    # script Python qui génère le QR avec Hiro au centre
│   └── assets/
└── exercice6/index.html  # UI DOM overlay (slider taille + palette couleurs)
```

## 1. Créer le dépôt GitHub

1. Sur GitHub, crée un nouveau dépôt (public), par ex. `webar-tp01`.
2. En local, dans ce dossier :
   ```bash
   git init
   git add .
   git commit -m "TP01 WebAR - exercices 1 à 6"
   git branch -M main
   git remote add origin https://github.com/TON-PSEUDO/webar-tp01.git
   git push -u origin main
   ```

## 2. Activer GitHub Pages

1. Sur GitHub : `Settings` → `Pages`.
2. Source : `Deploy from a branch` → branche `main`, dossier `/ (root)`.
3. Après ~1 minute, ton site est en ligne à :
   `https://TON-PSEUDO.github.io/webar-tp01/`

Chaque exercice est alors accessible à :
`https://TON-PSEUDO.github.io/webar-tp01/exerciceN/`

**Important : AR.js a besoin de HTTPS pour accéder à la caméra sur mobile.**
GitHub Pages sert en HTTPS par défaut, donc pas de configuration supplémentaire.

## 3. Tester sur mobile

1. Ouvre l'URL GitHub Pages de l'exercice sur ton smartphone (Chrome/Safari).
2. Autorise l'accès à la caméra quand le navigateur le demande.
3. Imprime (ou affiche sur un second écran) le marqueur Hiro :
   https://jeromeetienne.github.io/AR.js/data/images/HIRO.jpg
4. Pointe la caméra vers le marqueur → la boîte doit apparaître.

## Détail par exercice

- **Exercice 1** : scène A-Frame pure (pas d'AR). 3 boîtes de couleurs différentes
  à y=2 (2 unités au-dessus du plan), caméra fixe à `(0, 10, 15)` inclinée de
  `-33.69°` pour cadrer toute la scène (angle = atan(10/15)).
- **Exercice 2** : ajout d'AR.js (`arjs` sur `<a-scene>`), marqueur `preset="hiro"`,
  boîte `transparent + opacity` qui tourne en continu (`animation` component).
- **Exercice 3** : ajout d'un `cursor` (`rayOrigin: mouse`, marche aussi au tap sur
  mobile) + composant custom `tap-color-change` qui change la couleur et accélère
  la rotation + déclenche un pulse d'échelle au clic/tap.
- **Exercice 4** : marqueur `type="pattern" url="assets/custom-marker.patt"` —
  **tu dois générer ton propre `.patt`** avec l'outil du sujet et le placer dans
  `exercice4/assets/` (voir `exercice4/assets/README.txt`). Affiche un
  `a-torus-knot` (objet différent de la boîte) en rotation.
- **Exercice 5** : `generate_qr.py` génère un QR code (correction d'erreur "H",
  tolère ~30% de zone masquée) avec le marqueur Hiro incrusté au centre
  (~22% de la surface). Avant de lancer le script :
  1. Télécharge le vrai `HIRO.jpg` dans `exercice5/assets/hiro.jpg`.
  2. Mets à jour `TARGET_URL` dans `generate_qr.py` avec ta vraie URL GitHub Pages.
  3. `python3 generate_qr.py` → produit `assets/qr-with-hiro.png`, à imprimer.
  Scanner ce QR code avec l'appli caméra ouvre le site ; pointer ensuite la webcam
  AR de la page vers le même QR détecte le Hiro caché au centre et affiche la boîte.
- **Exercice 6** : UI HTML par-dessus le canvas WebGL (`position: fixed`), cachée
  par défaut, affichée/masquée via les events `markerFound`/`markerLost` émis par
  AR.js sur `<a-marker>`. Slider → `box.setAttribute('scale', ...)` en temps réel,
  boutons de couleur → `box.setAttribute('color', ...)`.

## Dépannage

- **Rien ne s'affiche / caméra noire** : vérifie que l'URL est bien en `https://`
  et que la permission caméra a été accordée (icône dans la barre d'adresse).
- **Le marqueur n'est jamais détecté** : bonne lumière, marqueur bien à plat,
  bordure blanche visible autour, pas trop loin de la caméra.
- **Sur desktop pour tester vite** : Chrome autorise la webcam en HTTPS ou sur
  `localhost` (donc un `python3 -m http.server` en local fonctionne aussi pour
  les exercices 2, 3, 5, 6 sans passer par GitHub Pages).
