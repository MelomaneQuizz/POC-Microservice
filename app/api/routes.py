from typing import List
from fastapi import Header, APIRouter

routes = APIRouter()


@routes.get('/')
async def index():
    return {"Real": "Python"}
