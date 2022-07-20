from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Brand, Product, ProductImage
from django.contrib.auth.models import User

# Create your views here.
def landing_page(request):
    if request.user.is_authenticated:
        return render(request, 'pages/game_page.html')
    else:
        return redirect('login')

def product_page(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'pages/products.html', context=context)
    else:
        return redirect('login')

def single_product_view(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        context = {
            'product': product
        }
        return render(request, 'pages/single_product_view.html', context=context)
    else:
        return redirect('login')

def add_product_view(request):
    if request.user.is_authenticated:
        return render(request, 'pages/add_product.html')
    else:
        return redirect('login')

def handle_add_product(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            bnd = request.POST['brand']
            try:
                brand = Brand.objects.get(brand_name = bnd)
            except:
                brand = Brand.objects.get(id=1)
            product = Product(name=request.POST['name'], description=request.POST['description'], price = request.POST['price'], brand=brand)
            product.save()
            images = request.FILES.getlist('images')
            for image in images:
                img = ProductImage(image=image)
                img.save()
                product.image.add(img)
                product.save()
            return render(request, 'pages/add_product.html')
        else:
            return render(request, 'pages/add_product.html')
    else:
        return redirect('login')

def add_coins(request, user_id, num_coins):
    user = User.objects.get(id=user_id)
    profile = user.profile
    profile.coins += num_coins
    profile.save()
    # return JsonResponse({'final_coins': user.profile.coins})
    return redirect("homepage")

def share_coins(request, user_id, num_coins, reciever_id):
    user = User.objects.get(id=user_id)
    rc = User.objects.get(id=reciever_id)
    #removing coins from sender
    profile = user.profile
    profile.coins -= num_coins
    profile.save()
    #adding coins to the reciever
    profile = rc.profile
    profile.coins += num_coins
    profile.save()
    return JsonResponse({'final_coins': user.profile.coins})

def current_user(request):
    return JsonResponse({'current_user': request.user.id})

def share_coins_view(request):
    if request.user.is_authenticated:
        context = {
            'users': User.objects.all()
        }
        return render(request, 'pages/share_coins.html', context=context)
    else:
        return redirect('login')

def change_share_coin_status(request):
    if request.user.is_authenticated:
        context = {
                'users': User.objects.all()
            }
        if request.method == 'POST':
            print(request.POST)
            user = User.objects.get(id=int(request.user.id))
            rc = User.objects.get(id=int(request.POST['user_id']))
            #removing coins from sender
            profile = user.profile
            profile.coins -= int(request.POST['num_coins'])
            profile.save()
            #adding coins to the reciever
            profile = rc.profile
            profile.coins += int(request.POST['num_coins'])
            profile.save()
            return render(request, 'pages/share_coins.html', context=context)
        else:
            return render(request, 'pages/share_coins.html', context=context)
    else:
        return redirect('login')