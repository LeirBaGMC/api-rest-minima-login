# API REST mínima - Login demo

API mínima construida con **FastAPI** que valida usuario/contraseña contra una lista de usuarios "quemada" en código.  
No utiliza JWT ni sesiones, solo validación simple.

---

## Requisitos

- Python 3.10+
- Git (opcional, para clonar el repositorio)

---

## 1 Clonar el repositorio

```bash
git clone https://github.com/LeirBaGMC/api-rest-minima-login.git
cd api-rest-minima-login

```
## 2 Windows (Git Bash)
python -m venv .venv
source .venv/Scripts/activate

## 3 Instalar dependencias
pip install -r requirements.txt

## 4 Ejecutar el servidor
uvicorn main:app --reload
## 5 Probar página web
En el navegador: http://127.0.0.1:8000/docs
## Endpoints 
Endpoints principales
curl http://127.0.0.1:8000/
curl -X POST "http://127.0.0.1:8000/login?username=alice&password=123"



E
