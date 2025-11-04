# {{ cookiecutter.project_name }} 

Author: {{ cookiecutter.project_author_name }}.

Version: {{ cookiecutter.project_version }}

{{ cookiecutter.project_description }}

## Prerequisites

- [Anaconda](https://www.anaconda.com/download/) >=4.x
- Optional [Mamba](https://mamba.readthedocs.io/en/latest/)

## Create environment

```bash
conda env create -f environment.yml
activate {{ cookiecutter.project_slug }}
```

or 

```bash
mamba env create -f environment.yml
activate {{ cookiecutter.project_slug }}
```

## Project organization

    {{ cookiecutter.project_slug }}
        ├── data
        │   ├── processed      <- Los conjuntos de datos finales y canónicos para el modelado.
        │   └── raw            <- Los datos originales e inmutables.
        │
        ├── notebooks          <- Cuadernos Jupyter. Convención de nombres: un número (para ordenar),
        │                         las iniciales del creador y una breve descripción separada por `-`, por ejemplo
        │                         `1.0-{{ cookiecutter.project_author_name }}-initial-data-exploration`.
        │
        ├── .gitignore         <- Archivos a ignorar por `git`.
        │
        ├── environment.yml    <- El archivo de requisitos para reproducir el entorno de análisis.
        │
        └── README.md          <- El README de alto nivel para desarrolladores que usan este proyecto.