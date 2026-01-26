from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Product, Order
import stripe

# Stripe secret key set
stripe.api_key = settings.STRIPE_SECRET_KEY


# def home(request):
#     products = Product.objects.all()
#     orders = Order.objects.filter(paid=True).order_by('-created_at')
    
#     for product in products:
#         product.ui_price = product.price / 100

#     return render(request, "home.html", {
#         "products": products,
#         "orders": orders
#     })


def home(request):
    products = Product.objects.all()
    orders = Order.objects.filter(paid=True).order_by('-created_at')

    # Products: paise → rupees
    for product in products:
        product.ui_price = product.price / 100

    # 🔥 Orders: paise → rupees
    for order in orders:
        order.ui_amount = order.amount / 100

    return render(request, "home.html", {
        "products": products,
        "orders": orders
    })



def create_checkout(request):
    """
    Create Stripe checkout session
    """
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        quantity = int(request.POST.get("quantity", 1))

        product = Product.objects.get(id=product_id)

        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "inr",
                    "product_data": {
                        "name": product.name
                    },
                    "unit_amount": product.price,
                },
                "quantity": quantity,
            }],
            mode="payment",
            success_url="http://127.0.0.1:8000/success/?session_id={CHECKOUT_SESSION_ID}",
            cancel_url="http://127.0.0.1:8000/",
        )

        # Create order BEFORE redirect (important)
        Order.objects.create(
            stripe_session_id=session.id,
            amount=product.price * quantity
        )

        return redirect(session.url)

    return redirect("home")


def payment_success(request):
    """
    Mark order as paid (idempotent)
    """
    session_id = request.GET.get("session_id")

    if not session_id:
        return redirect("home")

    try:
        order = Order.objects.get(stripe_session_id=session_id)
    except Order.DoesNotExist:
        return redirect("home")

    # Prevent double processing
    if not order.paid:
        order.paid = True
        order.save()

    return redirect("home")
