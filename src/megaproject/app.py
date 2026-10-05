from fastapi import FastAPI
from pydantic import BaseModel
from .agent import Agent
from .sandbox import Workspace
app=FastAPI(title="Sandboxed Tool Agent")
class Step(BaseModel): tool:str; args:dict={}
class Run(BaseModel): steps:list[Step]
@app.get("/health")
def health(): return {"ok":True}
@app.post("/run")
def run(body:Run): return Agent(Workspace(".")).run([x.model_dump() for x in body.steps])
