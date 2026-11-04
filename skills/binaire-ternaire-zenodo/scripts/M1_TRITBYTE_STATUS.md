# M1 — tritbyte COMPRESSED (fonctionnel)

## Problème
`tritbyte.py` ≈ 44 ko dépassait confortablement les limites de payload API pour un push texte unique.

## Solution
`tritbyte_loader.py` : charge utile **gzip niveau 9 + base64** + vérification SHA-256 + écrit `tritbyte.py`.

| Forme | Taille |
|-------|--------|
| tritbyte.py brut | ~44021 octets |
| gzip | ~11594 |
| loader (b64 inclus) | ~16 ko |

## Usage
```bash
python3 tritbyte_loader.py
python3 -m py_compile tritbyte.py
```

SHA-256 attendu du raw : `6bd2df445d684db158a1560956331da746a7f60a86bb736632ee6903864997a6`

Page download (artefacts locaux) : `m1_download.html`

NickelRamQc94 · Free gift · LOCKÉ EN TABARNAK.
