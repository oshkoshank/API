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
    class Config:
        model = Category
        model_fields = ['id','title','description','created_at','content']