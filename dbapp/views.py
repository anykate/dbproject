from django.shortcuts import render
from .models import Category, Item


# Create your views here.
def index(request):
    categories = Category.objects.all()
    return render(request, 'dbapp/index.html', {'categories': categories})


def details(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        item = None

    return render(request, 'dbapp/item_details.html', {'item': item})
