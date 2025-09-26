from fastapi import FastAPI
from sqlmodel import SQLModel

app = FastAPI(title="API REST mínima - Login demo")

class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


class UserRepository:
    def __init__(self):
        self.usuarios = [
            User("alice", "123"),
            User("bob", "456")
        ]

    def autenticar(self, username: str, password: str):
        for u in self.usuarios:
            if u.username == username and u.password == password:
                return u
        return None

repo = UserRepository()

# --- Endpoints ---
@app.get("/")
def read_root():
    return {"mensaje": "Hola, FastAPI funciona ..."}

@app.post("/login")
def login(username: str, password: str):
    user = repo.autenticar(username, password)
    if user:
        return {"ok": True, "msg": f"Bienvenido {user.username}"}
    return {"ok": False, "msg": "Usuario o contraseña inválidos"}
