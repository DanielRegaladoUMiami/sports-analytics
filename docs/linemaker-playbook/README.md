# linemaker-playbook

Base de conocimiento local (vault de Markdown estilo Obsidian) del canal de YouTube **LINEMAKER SPORTS**, de Frank Civittolo según el título oficial de su clip en Dr. Phil (los captions lo transcriben mal como “Frank LaManna” o “Frank Linemaker”).

El objetivo es **absorber todo lo que enseña** y **convertir cada regla en una hipótesis que se pueda probar** con datos de mercado.

## Qué hay

| Ruta | Contenido |
|---|---|
| [index.md](index.md) | El mapa general: tabla de hipótesis, temas y cobertura. **Empieza aquí.** |
| [timeline.md](timeline.md) | Cómo fue cambiando su método de 2020 a 2026. |
| [contradictions.md](contradictions.md) | En qué se contradice, sus errores de matemática y las alertas sobre la evidencia. |
| `hypotheses/` | 48 fichas, `H-###` (mercado) y `P-###` (prácticas). Cada una tiene qué dice, lectura previa, plan de prueba y variantes con los videos que las mencionan. |
| `topics/` | 20 temas, cada uno con una síntesis breve y la lista cronológica de videos. |
| `videos/` | *(no incluido en este repo)* 414 notas, una por video. Se quedan en local; cada referencia enlaza al video en YouTube. |
| `raw/` | *(no incluido en este repo)* Transcripts, VTT, metadata y reportes de los agentes. Los scripts lo regeneran localmente. |
| `scripts/` | El pipeline (ver abajo). |

## Cómo se construyó

1. `scripts/fetch_subs.sh`: yt-dlp baja los subtítulos en inglés de los 418 videos largos. 4 no tienen transcript.
   `scripts/fetch_missing.py`: segundo intento con youtube-transcript-api para los que falten.
2. `scripts/clean_vtt.py`: convierte cada VTT en un transcript con bloques de ~30 s y timestamps `[mm:ss]`.
3. 12 subagentes escribieron las notas de `videos/` siguiendo [CONVENTIONS.md](CONVENTIONS.md), en español y en paráfrasis.
4. `scripts/extract_rules.py`: extrae los slugs de las reglas.
   `scripts/clusters.py`: agrupa los 347 slugs en 48 hipótesis.
   `scripts/hypotheses_text.py`: la síntesis escrita a mano para cada hipótesis.
5. `scripts/build_vault.py`: genera `hypotheses/`, `topics/` e `index.md`. Se puede volver a correr.

```bash
python3 -I scripts/extract_rules.py .
python3 -I scripts/build_vault.py .
```

## Pendientes
- Re-transcribir con Whisper 3 videos cuyo transcript es basura: X0AF830t56c, 4y5BbDgCHmA, BKfBmR6t5EU.
- Probar las hipótesis de MLB (H-020 a H-027) en `mlb-canes-analytics`.
- `videos/` y `raw/` no se publican: las notas por video y los transcripts se quedan en local. Los scripts de `scripts/` necesitan esas carpetas para regenerar el vault.
