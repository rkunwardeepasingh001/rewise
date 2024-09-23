from fastapi import FastAPI

app = FastAPI()

@app.get('/first_route/{item_id}')
def func_1(item_id:str):
    return {"message": "Hello from func_1","item_id":{item_id}}


@app.get('/second_route')
def func_2():
    return {"message": "Hello from func_2"}