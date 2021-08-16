

from django.shortcuts import redirect, render
from .models import Cart, Customer,Product,User,Order
from .forms import CustomerProfileForm
from django.contrib import messages

from django.views import View
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



def home(request):
    context={}
    mobile=Product.objects.filter(Category='MO')
    laptop=Product.objects.filter(Category='LA')
    women_ethnics=Product.objects.filter(Category__in=['WEC','WES','WWT'])
    men=Product.objects.filter(Category__in=['MT','MB'])
   
   
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
     
    
    return render(request, 'app/home.html',{'mobile_list':mobile,'laptop_list':laptop,'women_eth':women_ethnics,'men_list':men,'count':count})

def search(request):
   
    data=request.GET['search']
    search_result=Product.objects.filter(Title__icontains=data).order_by('-Id')
   
   
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
     
    
    return render(request, 'app/search.html',{'search_result':search_result,'count':count,'data':data})

class Product_detailView(View):
    def get(self,request,id):
        details=Product.objects.get(Id=id)
        if request.user.is_authenticated:
            count=len(Cart.objects.filter(User=request.user))
        
        return render(request, 'app/productdetail.html',{'product_det':details,'count':count})

@login_required
def add_to_cart(request,id):
    if request.user.is_authenticated:
        user=request.user
        cart_check=Cart.objects.filter(Q(User=request.user) & Q(Product=id)).first()
        count=len(Cart.objects.filter(User=request.user))
        
       
        if cart_check:
            
            cart_check.Quantity+=1
            cart_check.save()
        else:
            product=Product.objects.get(Id=id)
            Cart(User=user,Product=product).save()
        return redirect('/cart')
    
@login_required
def show_cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(User=user).order_by('-Id')
        count=cart.count()
        
        tot_cost=0.00
        shipping=70.00
        grand_cost=0.00
        if cart:
            for item in cart:
                single_cost=item.Quantity * item.Product.Discounted_Price
                tot_cost=tot_cost+single_cost
                grand_cost=tot_cost+shipping
            
        
        return render(request, 'app/addtocart.html',{'carts':cart,'count':count,'grand_cost':grand_cost,'tot_cost': tot_cost})


def pluscart(request):
    if request.method=='GET':
        pro_id=request.GET['prod_id']
        c=Cart.objects.get(Q(User=request.user) & Q(Product=pro_id))
        c.Quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(User=user)
        count=cart.count()
        
        tot_cost=0.00
        shipping=70.00
        grand_cost=0.00
        if cart:
            for item in cart:
                single_cost=item.Quantity * item.Product.Discounted_Price
                tot_cost=tot_cost+single_cost
                grand_cost=tot_cost+shipping
            data={
                'quantity':c.Quantity,
                'amount':tot_cost,
                'tot_amount':grand_cost

            }
            return JsonResponse(data)
           
def minuscart(request):
    if request.method=='GET':
        pro_id=request.GET['prod_id']
        c=Cart.objects.get(Q(User=request.user) & Q(Product=pro_id))
        c.Quantity-=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(User=user)
        count=cart.count()
        
        tot_cost=0.00
        shipping=70.00
        grand_cost=0.00
        if cart:
            for item in cart:
                single_cost=item.Quantity * item.Product.Discounted_Price
                tot_cost=tot_cost+single_cost
                grand_cost=tot_cost+shipping
            data={
                'quantity':c.Quantity,
                'amount':tot_cost,
                'tot_amount':grand_cost

            }
            return JsonResponse(data)
           

def removecart(request):
    if request.method=='GET':
        pro_id=request.GET['prod_id']
        c=Cart.objects.get(Q(User=request.user) & Q(Product=pro_id))
       
        c.delete()
     
        user=request.user
        cart=Cart.objects.filter(User=user)
        count=cart.count()
        
        
        tot_cost=0.00
        shipping=70.00
      
        if cart:
            for item in cart:
                single_cost=item.Quantity * item.Product.Discounted_Price
                tot_cost=tot_cost+single_cost
               
        data={
            'amount':tot_cost,
            'tot_amount':tot_cost+70,
            'cart_count':count
        }  

            
        return JsonResponse(data)
           


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self,request):
          form=CustomerProfileForm()
          if request.user.is_authenticated:
            count=len(Cart.objects.filter(User=request.user))
          return render(request,'app/profile.html',{'form':form,'active':'btn-primary','count':count})

    def post(self,request):
            form=CustomerProfileForm(request.POST)
            if form.is_valid():
              user=request.user
              name=form.cleaned_data['Name']
              locality=form.cleaned_data['Locality']
              city=form.cleaned_data['City']
              state=form.cleaned_data['State']
              zipcode=form.cleaned_data['ZipCode']
              reg=Customer(User=user,Name=name,Locality=locality,City=city,State=state,ZipCode=zipcode)
              reg.save()
              messages.success(request,'Profile updated Successfully')
            
            return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})
            
@login_required      
def address(request):
    address=Customer.objects.filter(User=request.user)
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
    return render(request, 'app/address.html',{'address':address,'active':'btn-primary','count':count})

@login_required
def orders(request):
    op=Order.objects.filter(User=request.user)
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
    return render(request, 'app/orders.html',{'orders':op,'count':count})



def mobile(request,data=None):
    if data==None:
        mobile_list=Product.objects.filter(Category='MO')
    
    elif data=='Samsung' or data=='Redmi' or data=='Apple':
        mobile_list=Product.objects.filter(Category='MO').filter(Brand=data)

    elif data=='rate30000':
        mobile_list=Product.objects.filter(Category='MO').filter(Discounted_Price__gt=10000).filter(Discounted_Price__lt=30000)

    elif data=='rate60000':
        mobile_list=Product.objects.filter(Category='MO').filter(Discounted_Price__gt=30000).filter(Discounted_Price__lt=60000)
    elif data=='rate90000':
        mobile_list=Product.objects.filter(Category='MO').filter(Discounted_Price__gt=60000).filter(Discounted_Price__lt=90000)
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
    return render(request, 'app/mobile.html',{'mobile':mobile_list,'count':count})

def laptop(request,data=None):
    if data==None:
        laptop_list=Product.objects.filter(Category='LA')
    
    elif data=='Dell' or data=='Lenovo' or data=='HP':
        laptop_list=Product.objects.filter(Category='LA').filter(Brand=data)

    elif data=='above50000':
        laptop_list=Product.objects.filter(Category='LA').filter(Discounted_Price__gt=50000)

    elif data=='below50000':
        laptop_list=Product.objects.filter(Category='LA').filter(Discounted_Price__lt=50000)
    
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
    return render(request, 'app/laptop.html',{'laptop':laptop_list,'count':count})

def women(request,data=None):
    if data==None:
        women_list=Product.objects.filter(Category__in=['WEC','WES','WWT'])
    
    elif data=='WEC' or data=='WES' or data=='WWT':
        women_list=Product.objects.filter(Category__in=['WEC','WES','WWT']).filter(Category=data)
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
    
    return render(request, 'app/women.html',{'women':women_list,'count':count})

def men(request,data=None):
    if data==None:
        men_list=Product.objects.filter(Category__in=['MT','MB'])
    
    elif data=='MT' or data=='MB':
        men_list=Product.objects.filter(Category__in=['MT','MB']).filter(Category=data)
    elif data=='AllenSolly' or data=='Tommy' or data=='Adidas':
        men_list=Product.objects.filter(Category__in=['MT','MB']).filter(Brand=data)
  
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user))
    
    return render(request, 'app/men.html',{'men':men_list,'count':count})





@login_required
def checkout(request):
   
    cart_items=Cart.objects.filter(User=request.user)
    tot_cost=0.00
    shipping=70.00
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user)) 
    if cart_items:
        for item in cart_items:
            single_cost=item.Quantity * item.Product.Discounted_Price
            tot_cost=tot_cost+single_cost
            grand_tot=tot_cost+70
              
    return render(request, 'app/checkout.html',{'cart_items':cart_items,'tot_cost':tot_cost,'grand_tot':grand_tot,'count':count})

@login_required
def order_placed(request):
   
        customer_id=request.GET.get('address')
        print(customer_id)
        if customer_id==None:
            address=Customer.objects.filter(User=request.user)
            cart_items=Cart.objects.filter(User=request.user)
            tot_cost=0.00
            shipping=70.00
            if request.user.is_authenticated:
                count=len(Cart.objects.filter(User=request.user)) 
            if cart_items:
                for item in cart_items:
                    single_cost=item.Quantity * item.Product.Discounted_Price
                    tot_cost=tot_cost+single_cost
                    grand_tot=tot_cost+70
            message="Please select Address"      
            return render(request, 'app/address_select.html',{'address':address,'cart_items':cart_items,'tot_cost':tot_cost,'grand_tot':grand_tot,'count':count,'message':message})

        else:
            customer=Customer.objects.get(Id=customer_id)
            #print(customer_id)
            c=Cart.objects.filter(User=request.user)
            for items in c:
                Order(User=request.user,Product=items.Product,Customer=customer,Quantity=items.Quantity).save()
                items.delete()
            
            return redirect("orders")

def orderaddress(request):
    address=Customer.objects.filter(User=request.user)
    if request.user.is_authenticated:
        count=len(Cart.objects.filter(User=request.user)) 
    return render(request,'app/address_select.html',{'address':address,'count':count})