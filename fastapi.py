import enum
import random
import typing
import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from fastapi.responses import ORJSONResponse
from fastapi.responses import UJSONResponse

app = FastAPI()


class ItemList(BaseModel):
    instances: List[float]


@app.post("/items/operations")
def operations(operators: ItemList):
    extracted_list = operators.instances
    sumac = np.sum(extracted_list)


    resta = extracted_list[0]
    for x in extracted_list:
        resta = resta - x

    #rest = np.subtract(extracted_list)
    multiplicacion = np.prod(extracted_list)
    return [{"suma": sumac}, {"resta": resta},{"multiplicacion":multiplicacion}]


@app.get("/items/all", response_class=ORJSONResponse)
def read_all_items():
    return [{"item_id": "un item"}, {"item_id": "un item"}, {"item_id": "un item"}, {"item_id": "un item"},
            {"item_id": "un item"}, {"item_id": "un item"}]


@app.get("/items/all/alternative", response_class=UJSONResponse)
def read_all_items_alternative():
    return [{"item_id": "un item"}, {"item_id": "un item"}, {"item_id": "un item"}, {"item_id": "un item"},
            {"item_id": "un item"}, {"item_id": "un item"}]


@app.get("/")
def root():
    return {"Message": "hello World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/users/{user_id}")
def read_current_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/current")
def read_current_user():
    return {"user_id": "the current user"}


class RoleName(str, enum.Enum):
    admin = 'admin'
    writer = 'writer'
    reader = 'reader'


class Item(BaseModel):
    name: str
    description: typing.Optional[str] = None
    price: float
    tax: typing.Optional[float] = None


@app.post("/items/")
def create_item(item: Item):
    if not item.tax:
        item.tax = item.price * 0.12

    return {"item_id": random.randint(1, 100), **item.dict()}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"msg": f"el item {item_id} fue actualizado", "item": item.dict()}


@app.get("/roles/{rolename}")
def get_role_permissions(rolename: RoleName):
    if rolename == RoleName.reader:
        return {"role": rolename, "permisions": "you are allowed only to read"}

    if rolename == RoleName.writer:
        return {"role": rolename, "permisions": "you are allowed to read and write"}

    if rolename == RoleName.admin:
        return {"role": rolename, "permisions": "you are allowed to read and write"}


fake_items_db = [{"item_name": "uno"}, {"item_name": "dos"}, {"item_name": "tres"}]


@app.get("/items")
def read_all_itemes(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get("/items2/{item_id}")
def read_item(item_id: int, query: typing.Optional[str] = None):
    if query:
        return {"item_id": item_id, "query": query}

    return {"item_id": item_id}


@app.get("/users/{user_id/items/{item_id}")
def read_user_items(user_if: int, item_id: int, query: typing.Optional[str] = None, shot: bool = False):
    item = {"item_id": item_id, "owner": user_id}

    if query:
        item.update({"query": query})
    if not short:
        item.update({"description": "this is a long description for the item selected"})

    return item
