from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def henlo_worudo():
    return {"Henlo":"Worudo"}
