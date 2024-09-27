from fastapi import APIRouter
from app.api.v1.models import Item
from pydantic import BaseModel
from typing import Annotated
from fastapi import Query

router = APIRouter()
item_db=[]

@router.get("/get_item")
def get_item():
    return {"message":"this is get_item message"}

# @router.post("/post_item",response_model=ItemResponse)
# def post_item(name: str,description: str):
#     item = Item(name=name, description=description)
#     item_db.append(item)
#     return item

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
@router.get("/read_items")
def read_item(skip:int=0,limit:int=10):
    return fake_items_db[skip:skip+limit]

@router.get("/read_items/{item_id}")
def read_item_by_id(item_id:str,q:str|None=None):
    if q:
        return {"item_id":item_id,"q":q}
    return {"item_id":item_id,}

@router.get("/read_user_item/{item_id}/")
async def read_user_item(item_id:str,needy:str):
    item={"item_id": item_id, "needy":needy}
    return item

@router.get("/items_by/{item_id}")
async def read_user_by_item(item_id:str,needy:str,skip:int=0,limit:int |None=None):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

@router.post("/create_items")
async def create_item(item:Item):
    return item

@router.post("/new_items")
async def create_item_new(item:Item):
    item_dict=item.dict()
    if item.tax:
        price_with_tax=item.price+item.tax
        item_dict.update({"price_with_tax":price_with_tax})
    return item_dict

@router.put("/update_item/{item_id}")
async def update_item(item_id:int,item:Item):
    return {"item_id":item_id,**item.dict()}

@router.put("/update_item_default/{item_id}")
async def update_item_default(item_id:int,item:Item,q:str |None=None):
    result={"item_id":item_id,**item.dict()}
    if q:
        result.update({"q":q})
    return result

@router.get("/annotate_item")
async def annotate_read_item(q:Annotated[str |None, Query(max_length=50)] = None):
    result={"items":[{"item_id":"For"},{"item_id":"Bar"}]}
    if q:
        result.update({"q":q})
    return result
        
@router.get("/default_item")
async def default_read_item(q:Annotated[str |None, Query(default_length=None,max_length=50)] = None):
    results={"items":[{"item_id":"For"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results 

@router.get("/read_value")
async def read_query_item(q:Annotated[str | None ,Query(min_length=0,max_length=50)]):
    results={"items":[{"item_id":"For"},{"item_id":"Bar"}]}
    if q:
        results.update({"q":q})
    return results

@router.post("/add_data_item")
async def add_item_data(item:Item,q:Annotated[str | None ,Query(min_length=0,max_lengt=100)]):
    return item

@router.get("/default_read_item")
async def default_add_item(q:Annotated[str | None,Query(min_length=0,max_length=100)]="hello"):
    results={"item_id":[{"item_id":"foo"},{"item_id":"bass"}]}
    if q:
        results.update({"q":q})
    return results

@router.get("/item_product")
async def item_product(q:Annotated[str | None,Query(min_length=3)]="..."):
    results={"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results

@router.get("/item_value")
async def item_value(q:Annotated[str | None,Query(min_length=3)] = "..."):
    results={"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results

@router.get("/list_query_item")
async def list_query_item(q:Annotated[list[str] | None,Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        )]=None):
    query_items={"q":q}
    return query_items

