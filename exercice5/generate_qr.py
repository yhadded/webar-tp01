#!/usr/bin/env python3
"""
Exercice 5 - Génère un QR code (haute correction d'erreur) avec le marqueur Hiro
incrusté au centre.

Pourquoi ça marche :
- Un QR code en correction d'erreur "H" tolère jusqu'à ~30% de zone masquée/abîmée.
- On peut donc coller une image au centre (< ~25% de la surface) sans casser le scan.
- Le marqueur Hiro reste lisible par AR.js car ses coins/contours sont intacts,
  seul le centre du QR code (zone de données redondante) est recouvert.

Usage :
    1) Mets à jour TARGET_URL avec ta vraie URL GitHub Pages (exercice5/).
    2) Place l'image officielle du marqueur Hiro dans assets/hiro.jpg
       (téléchargée depuis https://jeromeetienne.github.io/AR.js/data/images/HIRO.jpg)
    3) Lance :  python3 generate_qr.py
    -> produit assets/qr-with-hiro.png
"""

import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image
import os

# 1) Remplace par l'URL réelle de TON projet une fois publié sur GitHub Pages
TARGET_URL = "https://TON-PSEUDO-GITHUB.github.io/TON-DEPOT/exercice5/"

HERE = os.path.dirname(os.path.abspath(__file__))
HIRO_PATH = os.path.join(HERE, "assets", "hiro.jpg")
OUTPUT_PATH = os.path.join(HERE, "assets", "qr-with-hiro.png")


def build_qr_with_center_image(data: str, center_image_path: str, output_path: str):
    qr = qrcode.QRCode(
        version=6,                       # taille fixe -> zone centrale prévisible
        error_correction=ERROR_CORRECT_H,  # ~30% de tolérance aux erreurs
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    qr_w, qr_h = qr_img.size

    if os.path.exists(center_image_path):
        center_img = Image.open(center_image_path).convert("RGB")
    else:
        # Fallback si le vrai Hiro.jpg n'est pas encore téléchargé :
        # place un carré noir/blanc "placeholder" pour visualiser la mise en page.
        # -> À REMPLACER par le vrai marqueur Hiro avant impression / test réel !
        center_img = Image.new("RGB", (200, 200), "white")
        from PIL import ImageDraw
        d = ImageDraw.Draw(center_img)
        d.rectangle([10, 10, 190, 190], outline="black", width=10)
        d.text((60, 90), "HIRO", fill="black")

    # Taille du marqueur central : ~22% de la largeur du QR code
    # (reste sous les ~30% tolérés par la correction H, marge de sécurité incluse)
    target_size = int(qr_w * 0.22)
    center_img = center_img.resize((target_size, target_size))

    # Bordure blanche autour du marqueur pour ne pas "manger" les modules voisins
    padded = Image.new("RGB", (target_size + 20, target_size + 20), "white")
    padded.paste(center_img, (10, 10))

    pos = ((qr_w - padded.width) // 2, (qr_h - padded.height) // 2)
    qr_img.paste(padded, pos)

    qr_img.save(output_path)
    print(f"OK -> {output_path}  ({qr_w}x{qr_h}px, data='{data}')")


if __name__ == "__main__":
    build_qr_with_center_image(TARGET_URL, HIRO_PATH, OUTPUT_PATH)
