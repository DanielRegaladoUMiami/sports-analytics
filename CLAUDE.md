# CLAUDE.md

EDA de NFL y LaLiga con enfoque de casa de apuestas (mercado como benchmark, números clave,
favorito-longshot, señal vs. ruido, Dixon-Coles). Notebook-first, sin paquete.

- Notebooks en `notebooks/` (01 NFL, 02 LaLiga, `espn_api/` exploradores de la API de ESPN).
- Figuras para el README en `docs/img/`; predicciones fechadas en `predicciones/YYYY-MM-DD.csv`.
- Datos descargados (`data_*`, `espn_cache`, `*.parquet`) están en `.gitignore`; nunca commitearlos.
- Deps con `uv` (`pyproject.toml`, `package = false`); Python 3.11+.
- Commits solo con Daniel como autor, sin Co-Authored-By.
- Es investigación, no recomendación de apuestas: mantener ese disclaimer en el README.
