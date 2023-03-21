from pydantic import BaseModel

class PutModel(BaseModel):
    name: str
    statement: str

class GetModel(BaseModel):
    name: str

class PostModel(BaseModel):
    name: str
    statement: str

class DeleteModel(BaseModel):
    name: str