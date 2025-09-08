# 🎌 Sistema de Recomendación Híbrido de Anime — *MAL 2020*

[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)]()
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange.svg)]()
[![Polars](https://img.shields.io/badge/Polars-✅-brightgreen.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()

> **Trabajo final — Curso de IA (Sistemas de Recomendación)**  
> Documentación redactada en **tercera persona**.

## 🧭 Resumen
El proyecto desarrolla un **sistema de recomendación híbrido** para anime sobre el dataset **Anime Recommendation Database 2020 (MyAnimeList)**. El sistema combina **Filtrado Colaborativo (CF)** y **Contenido** (géneros, estudios y **sinopsis** con embeddings) para producir recomendaciones **Top‑N** y predicción de **ratings**. Se contemplan prácticas de **reproducibilidad**, **evaluación rigurosa** y **documentación clara**.

---

## 📚 Dataset
- **Nombre:** *Anime Recommendation Database 2020* (MAL)
- **Kaggle (enlace directo):** https://www.kaggle.com/datasets/hernan4444/anime-recommendation-database-2020
- **Componentes principales:**
  - `animelist.csv`: ~109M interacciones (implícitas y explícitas parciales).
  - `rating_complete.csv`: ~57M **ratings completos** (usuarios que finalizaron el anime y calificaron).
  - `anime.csv`: metadatos (géneros, estudios, etc.).
  - `anime_with_synopsis/`: sinopsis (texto) para embeddings.

> Se prioriza `rating_complete.csv` para explícito y `animelist.csv` para señales implícitas.

---

## 🎯 Objetivos
- Construir un pipeline de **ingesta → limpieza → features**.
- Entrenar **baselines** y modelos **colaborativos** (explícito/implícito).
- Generar **embeddings de sinopsis** y vectores de **género/estudio**.
- Integrar un **modelo híbrido** y **evaluar** con métricas de rating y ranking.
- Entregar un **producto tecnológico** (notebooks, scripts, documentación).

---

## 🧪 Métricas
- **Rating:** RMSE, MAE.  
- **Top‑N:** Recall@K, **NDCG@K**, MAP@K.  
- **Ablaciones:** CF vs. Contenido vs. Híbrido.

---

## 🏗️ Arquitectura del sistema
```
           Datos (MAL 2020)
                  │
        ┌─────────┴─────────┐
        │                   │
   CF Explícito        CF Implícito          +  Contenido (NLP + categorías)
 (ALS/Autoencoder)   (BPR/implicit MF)       +  Embeddings de sinopsis / géneros / estudios
        │                   │                 │
        └──────────┬────────┘                 │
                   ▼                          │
            Fusión Híbrida  →  Rankeos Top‑N / Predicción de Rating
                 s(u,i) = α·s_CF(u,i) + (1−α)·s_Content(i)
```
> Por defecto, `α = 0.65` (configurable en `config/config.yaml`).

---

## 🚀 Inicio rápido

### 1) Crear entorno
```bash
python -m venv .venv && source .venv/bin/activate   # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

### 2) Descargar datos (Kaggle CLI)
```bash
pip install kaggle
mkdir -p ~/.kaggle && chmod 700 ~/.kaggle
# Copiar su kaggle.json a ~/.kaggle/kaggle.json y aplicar:
chmod 600 ~/.kaggle/kaggle.json

kaggle datasets download -d hernan4444/anime-recommendation-database-2020 -p data/raw
unzip -o data/raw/anime-recommendation-database-2020.zip -d data/raw/mal2020
```

### 3) Ejecutar notebooks (orden sugerido)
1. `notebooks/01_eda_preprocesamiento.ipynb`
2. `notebooks/02_modelos_cf_explicito.ipynb`
3. `notebooks/03_modelos_implicito.ipynb`
4. `notebooks/04_contenido_embeddings.ipynb`
5. `notebooks/05_hibrido_y_evaluacion.ipynb`

---

## 🗂️ Estructura
```
anime-recsys/
├─ config/config.yaml
├─ data/
│  ├─ raw/            # CSV originales (no versionados)
│  ├─ processed/      # Parquets/derivados (no versionados)
│  └─ external/
├─ notebooks/
├─ src/
│  ├─ features/
│  ├─ models/
│  ├─ eval/
│  └─ utils/
├─ REPORT.md
├─ README.md
└─ requirements.txt
```

---

## ⚙️ ¿Cómo funciona el sistema?
1. **EDA & Limpieza:** inspección de nulos, duplicados y distribución de ratings; filtrado de usuarios/ítems muy escasos.
2. **Features (Contenido):** one‑hot/embeddings para géneros/estudios; **embeddings semánticos** de sinopsis (Sentence‑Transformers).
3. **Modelos CF:**
   - *Explícito:* ALS / Autoencoder (TF) sobre `rating_complete.csv`.
   - *Implícito:* BPR/implicit MF con binarización de `animelist.csv`.
4. **Fusión Híbrida:** combinación ponderada `α·CF + (1−α)·Contenido` con calibración simple.
5. **Evaluación:** RMSE/MAE (predicción) y Recall/NDCG/MAP (Top‑N) con splits estratificados.
6. **Reporte:** tablas comparativas, curva de rendimiento y análisis de cobertura.

---

## 🧑‍⚖️ Licencia y atribución
- Código: **MIT** (ver `LICENSE`).
- Datos: revisar licencias del **owner en Kaggle** y documentación asociada.

---

> *Para reproducibilidad, se recomienda registrar versiones de librerías y fijar semillas en los entrenamientos.*
