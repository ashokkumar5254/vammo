from .models import category
def category_list(request):
    data=category.objects.all()
    return {"links":data}