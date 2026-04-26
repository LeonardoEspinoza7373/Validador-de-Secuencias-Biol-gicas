import uvicorn
from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="Validador de ADN API")

# Incluir las rutas
app.include_router(health.router)

@app.get("/")
async def root():
    return {"message": "Bienvenidos al Backend del Validador de ADN"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)