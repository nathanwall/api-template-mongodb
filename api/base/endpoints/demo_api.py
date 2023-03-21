from fastapi import APIRouter
from api.base.interfaces.mongo.mongo_conn import Database
from api.base.models.apimodels import PutModel, GetModel, PostModel, DeleteModel

router = APIRouter()


@router.post("/demo_api")
def demo_api_post(record: PostModel) -> bool:
    """ demo api POST """
    result = Database().demo_collection.insert_one(record.dict())

    return result.acknowledged

@router.get("/demo_api")
def demo_api_get(name: str) -> GetModel:
    """ demo api GET """
    result = Database().demo_collection.find_one({"name": name})

    return GetModel(**result)

@router.put("/demo_api")
def demo_api_PUT(record: PutModel) -> bool:
    """ demo api PUT """
    result = Database().demo_collection.update_one({"name": record.name}, {"$set": PutModel.dict()})

    return result.acknowledged


@router.delete("/demo_api")
def demo_api_delete(name: str) -> bool:
    """ demo api DELETE """
    result = Database().demo_collection.delete_one({"name": name})

    return result.acknowledged