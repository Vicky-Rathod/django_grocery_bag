from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import GroceryBag
from django.http import HttpResponse
from .forms import GroceryBagForm
from django.utils import timezone
# Create your views here.


def grocery_add(request):
    if request.method == 'POST':
        form = GroceryBagForm(request.POST)
        if form.is_valid():
            form.save()
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
def grocery_home(request):

    date = request.POST.get('date',default='{}'.format(timezone.now().date()))
    # print(date)
    daily_list = GroceryBag.objects.filter(product_date = date)
    return render (request,'index.html',{'grocery' : daily_list})