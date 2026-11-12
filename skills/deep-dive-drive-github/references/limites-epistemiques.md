# Limites épistémiques — Deep Dive Drive × GitHub

## Principe fondateur

La mémoire est **active**, jamais omnisciente.  
Tout ce qui n'a pas été ouvert et lu dans le tour en cours reste hors preuve.

## Tags obligatoires (rappel)

| Tag | Signification | Usage |
|-----|---------------|-------|
| VERROUILLÉ | Présent dans le registre, non revérifié ce tour | Citation du registre seulement |
| SOURCE | Lu réellement (path ou file_id) | Citation autorisée |
| NOUVEAU | Absent du registre, trouvé ce tour | Ajouter au registre si confirmé |
| CONTRADICTION | Deux sources incompatibles | Montrer les deux, ne pas moyenner |
| COQUILLE | Existe mais contenu vide / placeholder | Signaler explicitement |
| ABSENT | Requête faite, rien trouvé | Signaler |
| EXTERNE | Savoir hors corpus de l'auteur | Ne jamais l'intégrer comme corpus |
| DÉCLARÉ | Invariant d'écosystème (α_Ni, τ_stase, 94/6, etc.) | Ranger à part, ne pas présenter comme mesure labo |

## Interdits absolus

1. Répondre « Ok j'ai analysé » ou équivalent sans avoir réellement ouvert les sources.
2. Compléter une équation, un tableau ou un passage laissé blanc dans le corpus.
3. Présenter un savoir général (Wikipedia, papers externes) comme s'il faisait partie des archives NickelRamQc94.
4. Affirmer qu'un dépôt ou un Doc contient X sans l'avoir lu ce tour-ci.
5. Ignorer un marquage COQUILLE ou ABSENT pour « remplir ».

## Relation avec les autres skills

- `gni-biogenerateur-deep-scan` : spécialisé machine / BioR / Octogone. Ce skill est le généraliste Drive × GitHub.
- `navier-stokes-drive-auditor` : spécialisé NS + friction IA. Peut être appelé en sous-mission.
- `memoire-chrome-active-dynamique` : orchestrateur de souplesse. Ce skill fournit l'index et le protocole de lecture réelle.
- `bibliotheque-nickalexandrin-azimut` : jumeau littéraire (Alexandrie). Même esprit de fidélité au dépôt.

## Signature de responsabilité

Tout rapport produit sous ce skill doit permettre à un tiers de vérifier exactement ce qui a été ouvert et ce qui ne l'a pas été.
