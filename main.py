from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
  return {"hello" : "world"}
  # 8000 port