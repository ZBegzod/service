from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from home_app.models import *
from .forms import *

def index(request):
    resurs =  Resurs.objects.all()  
    context = {'Resurs':resurs}
    return render(request=request, template_name='index.html', context=context)

def fast_food_objects(request):
    fast_food_objects = Fast_food_branch.objects.all()
    context = {'Fast_food':fast_food_objects}
    return render(request, 'fast_food_objects.html', context)

def fast_food_add_or_update(request, pk = 0):
    if request.method == 'GET':
        if pk == 0:
            return render(request, 'fast_food_add_update.html')
        else:
            resurs = get_object_or_404(Fast_food_branch, pk=pk)
            context = {'Fast_food': resurs}
            return render(request, 'fast_food_add_update.html', context)
    elif request.method == 'POST':
        if pk == 0:
            data = request.POST
            fast_food = Fast_food_branch(name = data['title'], rating = data['rating'])
            fast_food.save()
        else:
            data = request.POST
            fast_food = Fast_food_branch.objects.get(pk=data['pk'])
            fast_food.name = data['title']
            fast_food.rating = data['rating']
            fast_food.save()
    return redirect('fast-food')

def fast_food_delete(request,pk=0):
    if request.method == 'GET':
        fast_food = get_object_or_404(Fast_food_branch, pk=pk)
        context = {'Fast_food':fast_food} 
        return render(request, 'fast_food_delete.html', context)
    else:
        pk = request.POST.get('pk')
        fast_food = get_object_or_404(Fast_food_branch, pk=pk)
        fast_food.delete()
    return redirect('fast-food')

def combo_objects(request):
    combo_objects = Combo.objects.all()
    context = {'Combo':combo_objects}
    return render(request=request, template_name='combo_objects.html', context=context)

def combo_add_or_update(request, pk=0):
    if request.method == 'GET':
        if pk == 0:
            return render(request, 'combo_add.html')
        else:
            combo = get_object_or_404(Combo,pk=pk)
            context = {'Combo':combo}
            return render(request, 'combo_add.html', context)
    elif request.method == 'POST':
        if pk == 0:
            data = request.POST
            combo = Combo(name = data['title'])
            combo.save()
        else:
            data = request.POST
            combo = Combo.objects.get(pk=data['pk'])
            combo.name = data['title']
            combo.save()
    return redirect('combo')
    
def combo_delete(request, pk=0):
    if request.method == 'GET':
        combo = get_object_or_404(Combo, pk=pk)
        context = {'Combo':combo}
        return render(request, 'combo_delete.html', context)
    else:
        pk = request.POST.get('pk')
        combo = get_object_or_404(Combo, pk=pk)
        combo.delete()
    return redirect('combo')

class Fast_foodListView(ListView):
    template_name = 'fast_food.html'
    fields = "__all__"
    context_object_name = 'fast_food'

    def get_queryset(self):
        customer = Group.objects.get(name='Customer')
        if self.request.user.has_perm('can_view_fast_food') or customer in self.request.user.groups.all():
            url_data = self.request.GET
            fast_food_objects = Fast_food_branch.objects.all()    
            if 'title' in url_data and url_data['title']:
                fast_food_objects = fast_food_objects.filter(name__icontains = url_data['title'])

            if 'rating' in url_data and url_data['rating']:
                fast_food_objects = fast_food_objects.filter(rating__icontains = url_data['rating'])
            return fast_food_objects

class Fast_food_createView(CreateView):
    queryset = Fast_food_branch.objects.all()
    template_name = 'fast_food_add.html'
    fields = "__all__"
    success_url = '/fast-food-class'

class Fast_food_UpdateView(UpdateView):
    queryset = Fast_food_branch.objects.all()
    template_name = 'fast_food_add.html'
    fields = "__all__"
    success_url = '/fast-food-class'
    
class Fast_food_DeleteView(DeleteView):
    queryset = Fast_food_branch.objects.all()
    template_name = 'fast_food_delete.html'
    fields = "__all__"
    success_url = '/fast-food-class'

class ProductListView(ListView):
    template_name = 'product.html'
    fields =  "__all__"
    context_object_name = 'product'
    def get_queryset(self):
        customer = Group.objects.get(name='Customer')
        if self.request.user.has_perm('can_view_product') or customer in self.request.user.groups.all():
            url_data = self.request.GET
            product_objects = Product.objects.all()
            if 'combo' in url_data and url_data['combo']:
                product_objects = product_objects.filter(combo__name__icontains = url_data['combo'])

            if 'resurs' in url_data and url_data['resurs']:
                product_objects = product_objects.filter(resurs__name__icontains = url_data['resurs'])

            if 'product_size' in url_data and url_data['product_size']:
                product_objects.filter(product_size__icontains = url_data['product_size'])
            return product_objects

class ProductAddView(CreateView):
    queryset = Product.objects.all()
    template_name = 'product_add.html'
    fields = "__all__"
    success_url = '/product'

class ProductUpdateView(UpdateView):
    queryset = Product.objects.all()
    template_name = 'product_add.html'
    fields = "__all__"
    success_url = '/product'

class ProductDeleteView(DeleteView):
    queryset = Product.objects.all()
    template_name = 'product_delete.html'
    fields = "__all__"
    success_url = '/product'

class ResursListView(ListView):
    template_name = 'resurs.html'
    fields =  "__all__"
    context_object_name = 'resurs'

    def get_queryset(self):
        url_data = self.request.GET 
        resurs_objects = Resurs.objects.all()
        
        if 'title' in url_data and url_data['title']:
            resurs_objects = resurs_objects.filter(name__icontains = url_data['title'])
            
        if 'product_quantity' in url_data and url_data['product_quantity']:
            resurs_objects = resurs_objects.filter(product_quantity__icontains = url_data['product_quantity'])

        if 'price' in url_data and url_data['price']:
            resurs_objects = resurs_objects.filter(price__icontains = url_data['price'])
        
        return resurs_objects

class ResursCreateView(CreateView):
    queryset = Resurs.objects.all()
    template_name = 'resurs_add.html'
    fields =  "__all__"
    success_url = '/resurs'

class ResursUpdateView(UpdateView):
    queryset = Resurs.objects.all()
    template_name = 'resurs_add.html'
    fields =  "__all__"
    success_url = '/resurs'

class ResursDeleteView(DeleteView):
    queryset = Resurs.objects.all()
    template_name = 'resurs_delete.html'
    fields =  "__all__"
    success_url = '/resurs'

class OrdersListView(ListView):
    template_name = 'orders.html'
    fields =  "__all__"
    context_object_name = 'orders'

    def get_queryset(self):
        url_data = self.request.GET
        order_objects = Orders.objects.all()
        if 'fast_food' in url_data and url_data['fast_food']:
            order_objects = order_objects.filter(fast_food_branch__name = url_data['fast_food'])
        
        if 'combo_name' in url_data and url_data['combo_name']:
            order_objects = order_objects.filter(product__combo__name__icontains = url_data['combo_name'])

        if 'resurs_name' in url_data and url_data['resurs_name']:
            order_objects = order_objects.filter(product__resurs__name__icontains = url_data['resurs_name']) 
        
        if 'resurs_size' in url_data and url_data['resurs_size']:
            order_objects = order_objects.filter(product__product_size__icontains = url_data['resurs_size'])
        return order_objects

class OrdersCreateView(CreateView):
    queryset = Orders.objects.all()
    template_name = 'orders_add.html'
    fields =  "__all__"
    success_url = '/orders'  

class OrdersUpdateView(UpdateView):
    queryset = Orders.objects.all()
    template_name = 'orders_add.html'
    fields =  "__all__"
    success_url = '/orders'

class OrdersDeleteView(DeleteView):
    queryset = Orders.objects.all()
    template_name = 'orders_delete.html'
    fields =  "__all__"
    success_url = '/orders'
 
def user_register_view(request):
    if request.method == 'GET':
        userform = UserRegisterModelform()
        return render(request, 'user-register.html', context={'form':userform})
    else:
        form = UserRegisterModelform(data = request.POST)
        password = request.POST['password']
        confirm = request.POST['confirm']
        if form.is_valid() and confirm == password:
            form.save()
            user = form.instance
            user.groups.add(Group.objects.get(name = 'Customer'))
            user.save()
            login(request, user)
            return redirect('fast-food-class')
        else:
            return render(request, 'user-register.html', context={'form':form})

def user_login_view(request):
    if request.method == 'GET':
        form = UserLoginform()
        return render(request, 'user-login.html', {'form':form})
    else:
        form = UserLoginform(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request, user)
                return redirect('fast-food-class')
            else:
                return render(request, 'user-login.html', {'form':form})