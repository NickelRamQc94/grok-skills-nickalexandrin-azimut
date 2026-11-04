# M1 — tritbyte remote status

**Local** : `/skills/binaire-ternaire-zenodo/scripts/tritbyte.py` — `python3 -m py_compile` **OK**

**Remote strategy** :
1. `join_tritbyte.sh` — reconstructeur
2. Full source remains authoritative in the Grok skill workspace and local clone
3. Optional: upload `tritbyte.py` as a GitHub **Release asset** (bypasses API content size limits)

## Validation locale (FAIT)
```bash
python3 -m py_compile scripts/tritbyte.py   # exit 0
python3 scripts/test_tritbyte.py            # si présent
```

## BioSKU companion (déjà sur remote)
- BioSKU_Engine.py v2
- BioSKU_Binary.py / BioSKU_Ternary.py
- test_biosku_v2.py

**Auteur** : NickelRamQc94 · Free gift  
LE SYSTÈME EST TOTAL. LOCKÉ EN TABARNAK.
