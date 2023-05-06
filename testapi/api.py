from ninja_extra import NinjaExtraAPI,api_controller
from .models import Content, Category
from .schema import ContentsSchema, CategorySchema,CreateCategory,CreateContent,ContentInCategorySchema
from datetime import datetime
from typing import List
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist


api = NinjaExtraAPI()

@api_controller(tags=['Categories'])
class CategoryAPI:
    @api.post('/list/',response=CategorySchema)
    def create_category(request, category: CreateCategory):
        cat = category.dict()
        cat = Category.objects.create(title=category.title,description=category.description)
        return cat
    
    @api.post('/explore/list/{id}/',response=ContentsSchema)
    def create_content(request,id:int, content: CreateContent):
        cat = Category.objects.get(id=id)
        con = Content.objects.create(content_name=content.content_name,description=content.description)
        cat.content.add(con)
        return con
    
    @api.get('/explore/',response=List[CategorySchema])
    def get_all_categories(request):
        category =  Category.objects.all()
        return category
    
    
    @api.get('/explore/list/{id}',response=List[ContentsSchema])
    def get_all_contents(request,id:int):
        qs = Category.objects.get(id=id)
        con = qs.content.all()
        return con

    @api.delete('/explore/list/{cat_id}/content/{con_id}')
    def delete_content(request,cat_id:int,con_id:int):
        try:
            category = Category.objects.get(id = cat_id)
            content = Content.objects.get(id = con_id)
            content.delete()
            return {"detail": f"Content removed from category {category.title} of  name {content.content_name} "}
        except ObjectDoesNotExist:
                return{"Detail": "Category or Content Not Found !"}
        
    
    @api.delete('/explore/list/{id}')
    def delete_category(request,id:int):
        category = Category.objects.get(id=id)
        category.content.all().delete()
        category.delete()
        return {"detail": f"Category deleted of name {category.title}"}