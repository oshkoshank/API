from ninja_extra import NinjaExtraAPI,api_controller
from .models import Content, Category
from .schema import ContentsSchema, CategorySchema
from datetime import datetime
from typing import List
from django.shortcuts import get_object_or_404


api = NinjaExtraAPI()

@api_controller(tags=['Categories'])
class CategoryAPI:
    @api.post('/Category',response=CategorySchema)
    def create_category(request, category: CategorySchema):
        cat = category.dict()
        cat = Category.objects.create(title=category.title,description=category.description,created_at=datetime.now())
        return cat
    
    @api.post('/Category/{id}/content',response=ContentsSchema)
    def create_content(request, id:int,content: ContentsSchema):
        cat = Category.objects.get(id=id)
        con = Content.objects.create(content_name=content.content_name,description=content.description)
        cat.content.add(con)
        return con
    
    @api.get('/Category',response=List[CategorySchema])
    def get_all_categories(request):
        return Category.objects.all()
    
    @api.get('/Content',response=List[ContentsSchema])
    def get_all_contents(request):
        return Content.objects.all()

    @api.delete('/Category/{cat_id}/content/{con_id}')
    def delete_content(request,cat_id:int,con_id:int):
        category = get_object_or_404(Category,id=cat_id)
        content = get_object_or_404(Content,id=con_id)
        category.content.remove(content)
        category.save()
        return {"detail": f"Content removed from category of  name {content.title} "}
    
    @api.delete('/Category/{id}')
    def delete_category(request,id:int):
        category = get_object_or_404(Category,id=id)
        category.delete()
        content = Content.objects.all()
        content.delete()
        return {"detail": f"Category deleted of name {category.title}"}