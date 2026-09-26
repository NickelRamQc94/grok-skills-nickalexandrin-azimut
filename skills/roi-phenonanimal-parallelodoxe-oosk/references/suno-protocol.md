# Suno protocol

## Style line

Build one style string, comma-separated, 3–8 tokens. Canonical home:

`rap-rock, nu-metal, cinematic`

Add at most two textures from: low hum, guitar strike, choir-static, cracked snare, magma kick, industrial drums, baritone choir, Quebec French rap, spoken-word, trap-metal.

Do not dump twenty genres. Do not put lyrics inside the style field.

## Structure tags

Always tag sections. Preferred order:

```
[Intro]
[Verse 1]
[Chorus]
[Verse 2]
[Chorus]
[Bridge]
[Chorus]
[Outro]
```

Mark the singer when it is a band session: `[Verse 1 — Junior]`, `[Verse 2 — Grok]`, `[Verse 3 — DeepSeek]`.

## Title grammar

- English steel + French ember is allowed: `RAM Mode (Born to Break)`
- Or all-FR detonations: `Implosion sonore`, `Algorithme 087`
- Never clickbait (`YOU WON'T BELIEVE`), never SEO stuffing.

## Chorus job

The chorus is the phoenix. It must contain one image that can be filmed in béton/cuivre/cendre. Example from the living catalog:

```
Volcanix Phoenix — I’m rising again!
From the dust, from the doubt, from the end!
```

Write new choruses in that voltage, do not clone the RAM Mode lyric unless the user asks for a sequel.

## Output contract (always)

```
TITLE:
STYLE:
LYRICS:
VIDEO_ALGORITHME:   (3 shots)
CAPTION:
```

If the user only wants lyrics, still include TITLE and STYLE so the track can be forged without a second prompt.
