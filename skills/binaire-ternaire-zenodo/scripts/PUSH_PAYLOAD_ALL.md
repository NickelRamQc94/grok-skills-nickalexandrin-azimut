# Pousser payload_all.b64 (15.5 ko)

Le fichier local vérifié est :
`artifacts/m1_push/payload_all.b64`

ou dans le skill après copie.

```bash
# Depuis la racine du repo cloné
cp /path/to/payload_all.b64 skills/binaire-ternaire-zenodo/scripts/
cd skills/binaire-ternaire-zenodo/scripts
python3 tritbyte_loader.py
python3 -m py_compile tritbyte.py
git add payload_all.b64
git commit -m "M1: payload_all.b64"
git push
```

SHA-256 tritbyte.py : 6bd2df445d684db158a1560956331da746a7f60a86bb736632ee6903864997a6

Loader déjà sur main.
