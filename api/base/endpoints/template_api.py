from fastapi import APIRouter
from api.base.interfaces.mongo.mongo_conn import Database
from api.base.models.apimodels import (
    PutModel,
    GetModel,
    PostModel,
)

router = APIRouter()


@router.post("/template_api")
def template_api_post(record: PostModel) -> bool:
    """template api POST"""
    result = Database().template_collection.insert_one(record.dict())

    return result.acknowledged


@router.get("/template_api")
def template_api_get(name: str) -> GetModel:
    """template api GET"""
    result = Database().template_collection.find_one({"name": name})

    return GetModel(**result)


@router.put("/template_api")
def template_api_put(record: PutModel) -> bool:
    """template api PUT"""
    result = Database().template_collection.update_one(
        {"name": record.name}, {"$set": PutModel.dict()}
    )

    return result.acknowledged


@router.delete("/template_api")
def template_api_delete(name: str) -> bool:
    """template api DELETE"""
    result = Database().template_collection.delete_one({"name": name})

    return result.acknowledged
