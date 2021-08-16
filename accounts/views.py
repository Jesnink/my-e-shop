from django.shortcuts import render
from django.views import View
from .forms import CustomUserRegistrationForm
from django.contrib import messages
# Create your views here.
# def customerregistration(request):
#  if request.method=='GET':
#         context={}
#         context['form']=CustomUserRegistrationForm()
#         return render(request,'customerregistration.html',context)


class customerregistrationView(View):
    def get(self,request):
        form=CustomUserRegistrationForm()
        return render(request, 'customerregistration.html',{'form':form})
    def post(self,request):
        form=CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registered Successfully')
            form.save()
        return render(request, 'customerregistration.html',{'form':form})
   