from django.shortcuts import render,redirect
from .models import *
from .forms import userform
# Create your views here.
def ordrlist(request):
    data=order.objects.all()
    return render(request,"orderlist.html",{'my':data})
def dele(request,id):
    dlt=order.objects.get(orid=id)
    dlt.delete()
    return redirect('o')
def addordr(request):
    data=customer.objects.all()
    if request.method =='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        ordr_obj=order()
        ordr_obj.orid=id
        ordr_obj.orname=name
        ordr_obj.cust=customer.objects.get(id=request.POST.get('userid'))
        ordr_obj.save()
        return redirect('o')
    return render(request,"addorder.html",{'data1':data})
def updat(request,id):
    data=customer.objects.all()
    dataa=order.objects.get(orid=id)
    if request.method =='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        ordr_obj=order()
        ordr_obj.orid=id
        ordr_obj.orname=name
        ordr_obj.cust=customer.objects.get(id=request.POST.get('userid'))
        ordr_obj.save()
        return redirect('o')
    return render(request,"addorder.html",{'data1':data,'data2':dataa})
def fm(request):
    if request.method =='POST':
        form=userform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = userform()
    return render(request,"forms.html",{'form':form})
def login(request):
    return render(request,"static.html")

    
      
   
    