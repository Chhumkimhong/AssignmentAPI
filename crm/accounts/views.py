from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from rest_framework import generics
from .serializers import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():  # Make sure to call is_valid() as a method
            form.save()
            return redirect("/accounts/login/")
    else:
        form = UserCreationForm()  # Move this to the else clause for GET request
    return render(request, "registration/signup.html", {"form": form})

# ListCreateAPIView provides GET (list) and POST (create) actions

class ProductsListCreate(generics.ListCreateAPIView):
    queryset = tblProducts.objects.all()    
    serializer_class = ProductSerializer

# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions

class ProductsDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblProducts.objects.all()
    serializer_class = ProductSerializer

# ============ Category =============
class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()    
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ============ Best Seller =============
class BestSellerListCreate(generics.ListCreateAPIView):
    queryset = BestSeller.objects.all()    
    serializer_class = BestSellerSerializer

class BestSellerDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = BestSeller.objects.all()
    serializer_class = BestSellerSerializer

# ============ Customer =============
class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()    
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# ============ Supplier =============
class SupplierListCreate(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()    
    serializer_class = SupplierSerializer

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


# ============ Clients =============
class ClientsListCreate(generics.ListCreateAPIView):
    queryset = tblClients.objects.all()    
    serializer_class = ClientsSerializer

class ClientsDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblClients.objects.all()
    serializer_class = ClientsSerializer

# ============ FreshOrganics =============
class FreshOrganicsListCreate(generics.ListCreateAPIView):
    queryset = tblFreshOrganic.objects.all()    
    serializer_class = FreshOrganicsSerializer

class FreshOrganicsDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblFreshOrganic.objects.all()
    serializer_class = FreshOrganicsSerializer

# ============ Sildes =============
class SildesListCreate(generics.ListCreateAPIView):
    queryset = tblSlides.objects.all()    
    serializer_class = SildesSerializer

class SildesDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSlides.objects.all()
    serializer_class = SildesSerializer

# ============ SupTopMenu =============
class SubTopMenuListCreate(generics.ListCreateAPIView):
    queryset = tblSubTopMenu.objects.all()    
    serializer_class = SubTopMenuSerializer

class SubTopMenuDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblSubTopMenu.objects.all()
    serializer_class = SubTopMenuSerializer

# ============ TopMenu =============
class TopMenuListCreate(generics.ListCreateAPIView):
    queryset = tblTopMenu.objects.all()    
    serializer_class = TopMenuSerializer

class TopMenuDetail(generics.RetrieveUpdateDestroyAPIView):    
    queryset = tblTopMenu.objects.all()
    serializer_class = TopMenuSerializer




# Create your views here.
@login_required
def Index(request):
    Product=tblProducts.objects.all()
    category=Category.objects.all()
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    Slide=tblSlides.objects.all()
    FreshOrganic=tblFreshOrganic.objects.all()
    Client=tblClients.objects.all()
    BestSellers=BestSeller.objects.all()
  


    context={
        'Products':Product,
        'Categorys':category,
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'Slides':Slide,
        'Organic':FreshOrganic,
        'Clients':Client,
        'BestSeller':BestSellers,

    }

    return render(request,'accounts/index.html',context)

# def Cart(request, product_id):
#     product=tblProducts.objects.get(id=product_id)
#     TopMenu=tblTopMenu.objects.all()
#     SubTopMenu=tblSubTopMenu.objects.all()
    
#     cart = get_object_or_404(ListCart, user=request.user)
#     if not request.user.is_authenticated:
#         return redirect('/accounts/login/')  # Redirect if user is not logged in

#     cart, created = ListCart.objects.get_or_create(user=request.user)

#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
#     total_price = 0
#     for item in cart.items.all():
#         total_price += float(item.total_price()) 
    
#     context={
       
#         'TopMenus':TopMenu,
#         'SubTopMenus':SubTopMenu,
#         'Products':product,
#         'totalprice':total_price,

#     }


#     return render(request,'accounts/cart.html',context)

# Assuming you're using Django or Flask for your web framework
def Cart(request, product_id):
    product=tblProducts.objects.get(id=product_id)
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'Products':product,
        
       
    }

    return render(request,'accounts/cart.html',context)

def AddtoCart(request,pk):
    
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    Organic=tblFreshOrganic.objects.get(id=pk)
    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        
        'Organics':Organic,
       
    }

    return render(request,'accounts/Organic.html',context)

def AddtoCartBestSeller(request,pk):
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    BestSellers=BestSeller.objects.get(id=pk)
    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'BestSeller':BestSellers,
       
    }

    return render(request,'accounts/TopProduct.html',context)

# def AddCart(request, product_id):
#     # Get the cart object
#     # cart = get_cart_object(request)
#     # product = get_product_by_id(product_id)
#     cart = get_object_or_404(ListCart, user=request.user)
#     product = get_object_or_404(tblProducts, id=product_id)
#     # Check if the product is already in the cart
#     cart_item = cart.items.filter(product=product).first()
    
#     if cart_item:
#         # Increment the quantity
#         cart_item.quantity += 1
#     else:
#         # Create a new cart item if it doesn't exist
#         cart_item = CartItem(product=product, quantity=1)
#         cart.items.add(cart_item)
    
#     # Calculate total price
#     # total_price = sum(int(item.product.PriceOut * item.quantity for item in cart.items.all()))
#     total_price = sum(float(item.product.PriceOut * item.quantity)  for item in cart.items.all())
#     cart.total_price = total_price
#     cart.save()

#     return redirect('Cart')
# def AddCart(request, product_id):
#     product = get_object_or_404(tblProducts, id=product_id)
#     if not request.user.is_authenticated:
#         return redirect('/accounts/login/')  # Redirect if user is not logged in

#     cart, created = ListCart.objects.get_or_create(user=request.user)

#     cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     return redirect('Cart')
    # return render(request,'accounts/cart.html',context)

# def cart_view(request):

#     cart = get_object_or_404(ListCart, user=request.user)
#     total_price = sum(float(item.total_price())  for item in cart.items.all())
#     return render(request, 'accounts/cart.html', {'Cart': cart, 'total_price': total_price})
    


# def cart_view(request):
#     cart = get_object_or_404(ListCart, user=request.user)
#     total_price = 0
#     for item in cart.items.all():
#         # print(f"Item price: {item.total_price()}, Type: {type(item.total_price())}")  # Debug line
#         total_price += float(item.total_price()) 
#     return render(request, 'accounts/cart.html', {'Cart': cart, 'total_price': total_price})

# def cart_view(request):
#     cart = get_object_or_404(ListCart, user=request.user)
#     total_price = 0
#     for item in cart.items.all():
#         item_price = item.total_price()
#         total_price += item_price  # Ensure this is adding numbers

#     return render(request, 'accounts/cart.html', {'Cart': cart, 'total_price': total_price})
# def authView(request):
#     if request.method=="POST":
#         form=UserCreationForm(request.POST or None)
#     if form.is_valid:
#         form.save()
#     else:
#         form =UserCreationForm()
#     return render(request,"registration/signup.html",{"form":form})




def Shop(request):
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    Product=tblProducts.objects.all()

    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'Products':Product,
       

    }
    return render(request,'accounts/shop.html',context)

def ShopDetail(request):
     
   
   
    return render(request,'accounts/shop-Detail.html')

def Shopdetail(request,pk):
    Product=tblProducts.objects.get(id=pk)
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    Client=tblClients.objects.all()
    FreshOrganic=tblFreshOrganic.objects.all()
   
    

    context={

        'Products':Product,
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'Clients':Client,
        'Organic':FreshOrganic,
       

    }
    return render(request,'accounts/shop-detail.html',context)



def Pages(request):
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()

    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
       

    }
    return render(request,'accounts/pages.html',context)

def CheckOut(request):
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    
    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        
       

    }
    return render(request,'accounts/chackout.html',context)

def Testimonial(request):

    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    Client=tblClients.objects.all()

    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'Clients':Client,
       

    }
    return render(request,'accounts/testimonial.html',context)

def Contact(request):

    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()

    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
       

    }
    return render(request,'accounts/contact.html',context)




def home(request):
    return HttpResponse('Home_page')

def products(request):
    return HttpResponse('Products_page')

def customer(request):
    return HttpResponse('Customer_page')

def payment(request):
    return render(request,'accounts/payment_success.html')

def bestSeller(request):
    TopMenu=tblTopMenu.objects.all()
    SubTopMenu=tblSubTopMenu.objects.all()
    BestSellers=BestSeller.objects.all()
    Client=tblClients.objects.all()

    context={
       
        'TopMenus':TopMenu,
        'SubTopMenus':SubTopMenu,
        'BestSeller':BestSellers,
        'Clients':Client,

    }
    return render(request,'accounts/BestProduct.html',context)