from django.shortcuts import render
from .models import Product,Contact
from math import ceil
import time
# Create your views here.
from django.http import HttpResponse

def index(request):
  # products = Product.objects.all()
   # print(products)
   # n = len(products)
   # nSlides = n//4 + ceil((n/4)-(n//4))
    #params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
   # allProds = [[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    allProds=[]
    catprods= Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod,range(1,nSlides),nSlides])
    params={'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method=="POST":
        #print(request)
        name=request.POST.get('name','')
        #print(name)
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        """b = time.localtime()
        if (b[3] > 12 and b[3] < 17):
            print("Hello " + name + " Good afternoon.", end="")
        elif (b[3] >= 17 and b[3] < 24):
            print("Hello " + name + " Good Evening.", end="")
        else:
            print("Hello " + name + " Good Morning.", end="")
        print(
            "Thanks for contacting you . We will reply you back soon . After replying we will give you form regarding feedback. It will be pleasure for us if you give your time in replying that.")
        print("Regards")
        print("Rohan Pahwa")
        print("[CEO and founder of Healthy Foods]")"""

        print(email)
        print(phone)
        print(desc)
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request,myid):
    #Fetching Products using id
    product = Product.objects.filter(id=myid)
    print(product)
    params={'product':product[0]}
    return render(request, 'shop/ProdView.html',params)

def checkout(request):
    return render(request, 'shop/checkout.html')