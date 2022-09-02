from .models import Category 

#TODO: show all categories in category
def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)