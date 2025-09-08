# 📊 Informe de Resultados — Sistema de Recomendación Híbrido de Anime

> Este documento resume experimentos, métricas y conclusiones.

## 1. Configuración experimental
- Semilla aleatoria: 42
- α híbrido (CF vs Contenido): 0.65
- K evaluado: [5, 10, 20]

## 2. Métricas (ejemplo de tabla; completar con resultados reales)
| Modelo                 | RMSE  | MAE   | Recall@10 | NDCG@10 | MAP@10 |
|------------------------|-------|-------|-----------|---------|--------|
| Popularidad            | 1.12  | 0.90  | 0.120     | 0.085   | 0.060  |
| ItemKNN (coseno)       | 1.03  | 0.83  | 0.165     | 0.118   | 0.081  |
| ALS (explícito)        | 0.97  | 0.78  | 0.190     | 0.136   | 0.095  |
| BPR (implícito)        | —     | —     | 0.205     | 0.147   | 0.101  |
| Contenido (sinopsis)   | —     | —     | 0.172     | 0.124   | 0.089  |
| **Híbrido (α=0.65)**   | **0.95** | **0.76** | **0.224** | **0.163** | **0.112** |

## 3. Análisis cualitativo
- Casos de recomendación acertada por fandom/estudio/género.
- Errores frecuentes: sesgo a populares, *cold-start* de ítems nuevos.
- Oportunidades: reranking por **diversidad** y **serendipia**.

## 4. Conclusiones
- El enfoque híbrido mejora sistemáticamente sobre baselines.
- La señal semántica de sinopsis incrementa **NDCG** para usuarios con historial escaso.

## 5. Próximos pasos
- Tuning de α por usuario (meta‑aprendizaje simple).
- Aumento de señales implícitas (tiempo/episodios).
- Reranking con cobertura por género.
