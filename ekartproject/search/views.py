from django.shortcuts import render
from ekart.models import Product
from django.db.models import Q


# Create your views here.
def result(request):
    products= None
    query= None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))

    return render(request, 'search.html', {'querry': query, 'products': products})
