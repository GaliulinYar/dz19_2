from django.shortcuts import render, get_object_or_404

from main.models import Product


# Create your views here.
def index(request):
    cat_list = Product.objects.all()
    context = {
        'object_list': cat_list
    }
    return render(request, 'main/index.html', context)


def contacts(request):
    """Контроллер, который отвечает за отображение контактной информации."""

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    return render(request, 'main/contacts.html')


def product(request, product_id):
    prod_get = get_object_or_404(Product, pk=product_id)

    return render(request, 'main/product.html', {'product': prod_get})


