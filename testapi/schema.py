from ninja import Schema,ModelSchema
from typing import List
from .models import Content, Category


class ContentsSchema(Schema):
    id : int
    content_name: str
    description: str


class ContentInCategorySchema(Schema):
    content_id : int
    category_id : int

class CategorySchema(ModelSchema):
    content : List[ContentsSchema]
    class Config:
        model = Category
        model_fields = ['title','description','id','created_at','content']


class CreateCategory(Schema):
    title: str
    description: str

class CreateContent(Schema):
    content_name: str
    description: str