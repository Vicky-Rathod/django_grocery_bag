from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import GroceryBag
from django.http import HttpResponse
from .forms import GroceryBagForm
from django.contrib.auth.decorators import login_required



def grocery_add(request):
    if request.method == 'POST':
        
        form = GroceryBagForm(request.POST, request.FILES or None)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            print(product.user)
            product.save()
            return HttpResponseRedirect("/")
        else:
            print(form.errors)
            return  HttpResponse(form.errors)
    else:
        form = GroceryBagForm ()
    return render(request, 'add.html', {'form' : form })

def grocery_update(request,pk):
    obj = get_object_or_404(GroceryBag, id = pk)
    form = GroceryBagForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "update.html", {'form':form})
def grocery_details(request,pk):
    obj = get_object_or_404(GroceryBag, id = pk)
    form = GroceryBagForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    return render(request, "detail.html", {'form':form,'obj':obj})



@login_required(login_url='/user/login/')
def grocery_home(request):

    product_list = GroceryBag.objects.all()
    return render (request,'index.html',{'grocery' : product_list})