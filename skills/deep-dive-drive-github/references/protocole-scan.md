# Protocole de scan — Deep Dive Drive × GitHub

## Ordre des opérations (ne pas sauter)

1. **Clarifier le périmètre**  
   Demander ou déduire : quel sujet / quels mots-clés / quels dépôts ou dossiers prioritaires. Ne jamais lancer un scan « tout » sans borne.

2. **Index rapide**  
   - GitHub : `github___search_repositories` query `user:NickelRamQc94` + `github___search_code` scoped.  
   - Drive : `google_drive_search` avec query ciblée + éventuellement `folder_name` ou `modified_after`.  
   - HF : noter les modèles/datasets connus du registre (pas d'API HF native ici).

3. **Lecture ciblée**  
   - GitHub : `github___get_repository_tree` puis `github___get_file_contents` sur les chemins prometteurs (README, docs/, src/ clés).  
   - Drive : `google_drive_read_file` ou download + skill approprié (pdf/docx).  
   Limiter à 3-8 fichiers réels par tour sauf demande explicite d'exhaustivité.

4. **Marquage**  
   Appliquer strictement les tags : VERROUILLÉ / SOURCE / NOUVEAU / CONTRADICTION / COQUILLE / ABSENT / EXTERNE / DÉCLARÉ.

5. **Synthèse**  
   Matrice ou liste structurée. Toujours indiquer :  
   - Périmètre réellement ouvert ce tour-ci  
   - Ce qui reste non lu  
   - Aucune prétention d'audit complet

## Anti-patterns interdits

- Inventer un file_id ou un SHA
- Compléter une coquille vide
- Dire « j'ai tout analysé » ou « Ok j'ai analysé » sans preuve
- Mélanger données EXTERNES (connaissances générales) avec le corpus comme si elles en faisaient partie
- Lancer des scans massifs non bornés qui saturent le contexte

## Sortie type

```
## Deep Dive [sujet] — [date]

### Périmètre réel
- Repos ouverts : ...
- Fichiers Drive lus : ...
- Non lus / non accessibles : ...

### Faits marqués
- [SOURCE] ...
- [COQUILLE] ...
- [ABSENT] ...

### Matrice croisée (si demandée)
...

### Limites
Ce tour n'a pas audité l'intégralité du corpus. Mémoire active seulement.
```
