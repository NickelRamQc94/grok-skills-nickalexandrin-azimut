# Colombo / Horus — operating notes

## Why first-page search lies on this Drive

- OR-clusters often return empty even when single terms hit.
- Titles are truncated conversation prompts. Full-text on Docs works; title_only on `2.txt` often misses.
- Memory disk mixes folders, HTML clones of Colab ids, and five copies of the same PDF.
- Beacon is small and high-signal (GoldNi, NS preprint, constantes).
- `#1.txt` `#2.txt` `#4.txt` `texte 155.txt` are the likely graves of unindexed neologisms.

## Order of operations

1. Beacon list (cheap, named PDFs).
2. Recent `modified_after` 2025-08-01, paginate.
3. Memory disk list, paginate.
4. Exact_name for mailbox `.pb787b893bc7b`.
5. Single-term searches.
6. GitHub `user:NickelRamQc94`.
7. Gmail `after:2025/08/01` only if the question needs unpublished drafts.

## Dedup rule

`normalize(name) + mime` → keep max(modified_time). Report `copies: N`.

## Output

Cluster first. Then zoom. File ids always. Missing claims listed last, never omitted.
