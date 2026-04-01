from fastapi import FastAPI

app=FastAPI()

@app.get("/queryparam/{name}")
async def queryparam(name:str,age:int):
    return {"name": name, "age":age}
