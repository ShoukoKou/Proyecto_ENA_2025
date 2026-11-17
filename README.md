# ✦ Proyecto ENA 2025

Proyecto final grupal del curso **Programación para Ciencia de Datos**.

Trabajamos con los microdatos de la **Encuesta Nacional Agropecuaria (ENA) 2025** para preparar, explorar y analizar información de las **unidades agropecuarias (UA) del Perú** mediante tablas estadísticas, gráficos y, cuando corresponde, mapas.

El propósito es que cada resultado pueda relacionarse con una pregunta de la encuesta, su código en el diccionario y una interpretación clara de los datos.

## ✦ Tecnologías utilizadas

- **Lenguaje:** Python.
- **Entorno de trabajo:** Jupyter Notebook y Visual Studio Code.
- **Bibliotecas principales:** pandas, NumPy y Matplotlib; herramientas geoespaciales cuando el análisis lo requiere.
- **Formatos:** Excel (`.xlsx`), Apache Parquet (`.parquet`) y archivos geográficos (`.json` / GeoJSON).

## ✦ Estructura del proyecto

```text
proyecto_pcda/
├── data/
│   ├── raw/                  # Datos originales (Excel y Parquet)
│   └── processed/            # Datos preparados e insumos geográficos
├── scripts/                  # Notebooks del equipo
├── src/                      # Funciones Python reutilizables
├── documentos/               # Diccionario y documentos del proyecto
├── outputs/
│   ├── figures/              # Gráficos y mapas generados
│   └── tables/               # Tablas exportadas
├── .gitignore                # Exclusiones de Git
├── requirements.txt          # Dependencias de Python
└── README.md                 # Documentación
```

## ✦ Módulos de análisis

| Módulo | Tema | Enfoque |
| :--- | :--- | :--- |
| **08 — Buenas Prácticas Agrícolas** | `08_CAP300AB` | Prácticas declaradas sobre suelo, agua, cultivos e insumos. |
| **14 — Inocuidad** | `14_CAP600` | Información, conocimientos y certificación declarados en relación con la inocuidad. |

Los análisis son **descriptivos**, sus porcentajes corresponden a los registros considerados en cada pregunta y no deben interpretarse automáticamente como estimaciones nacionales!

## ✦ Criterios de análisis

Para cada resultado procuramos documentar **el código de la pregunta, su significado, las respuestas válidas, el denominador y la interpretación breve**. Las gráficas complementan las tablas y permiten reconocer diferencias sin sustituir su explicación estadística. Los gráficos han de incluir títulos claros, leyendas y etiquetas legibles cuando corresponda.