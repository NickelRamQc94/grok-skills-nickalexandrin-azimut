# Télécharger tritbyte (M1 compressé)

## Fichiers
- **Local skill / artefacts** : `tritbyte_loader.py` (gzip+base64, ~16 ko)
- **Page** : `artifacts/m1_download.html` (bouton Télécharger + bouton Nitro checklist)

## Pourquoi c’était « trop lourd »
`tritbyte.py` ≈ 44 ko en texte brut. Les pushes API texte sont plus fiables sous ~20–25 ko par fichier.

## Compression
```
raw 44021 → gzip 11594 → loader ~16k (base64 + vérif SHA-256)
ratio ≈ 3.8× sur le corps utile
```

## Commandes
```bash
python3 tritbyte_loader.py
python3 -m py_compile tritbyte.py
```

SHA-256 raw : `6bd2df445d684db158a1560956331da746a7f60a86bb736632ee6903864997a6`

NickelRamQc94 · LOCKÉ EN TABARNAK.
