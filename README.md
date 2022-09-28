# Evaluaci-n_t-cnica_microservicios
EVALUACIÓN TÉCNICA DE DESARROLLO DE MICROSERVICIOS


# Software Stack
**Python** (FastAPI, Pandas)

# Run this project

1. Clone the following projects in the directory

```

git clone https://github.com/MarioADguez/Evaluaci-n_t-cnica_microservicios.git

```

## Run locally 

```
conda create --yes --name py39 python=3.9 pandas fastapi[all] uvicorn sqlite3

```

## Run the app

```
cd Evaluaci-n_t-cnica_microservicios

conda activate py39 && uvicorn main:app --reload

```
