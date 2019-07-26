from django.shortcuts import render
from shop.models import Category
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import send_mail



def order_create(request):
    cart = Cart(request)
    categories = Category.objects.all()
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            send_mail('New Order','Please check admin page','vivuvoveva1991@gmail.com',['vivuvoveva1991@gmail.com'],fail_silently=False,)
            return render(request, 'orders/order/created.html', {'order': order, 'categories': categories})
    else:
        form = OrderCreateForm()
        return render(request, 'orders/order/create.html', {'form': form, 'categories': categories})
