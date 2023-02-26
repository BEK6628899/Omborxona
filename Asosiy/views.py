from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *


class Loginview(View):
    def post(self,request):
            user = authenticate(username=request.POST.get('l'),
                         password=request.POST.get('p'))
            if user:
                login(request, user)
                return redirect('bolim')
            return redirect('login')
    def get(self,request):
        return render(request,"home.html")


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')



class BolimlarView(View):
    def get(self,request):
        return render(request,"bulimlar.html")



class ClientView(View):
    def get(self,request):
        # client1 = Client.objects.filter(ombor__user=request.user)
        # data = {'client':client1}
        client = request.GET.get("qidirish")
        if client is None or client == "":
            client1 = Client.objects.filter(ombor__user=request.user)
        else:
            client1 = Client.objects.filter(ism__contains=client)
        data = {'client': client1}
        return render(request,"clients.html",data)
    def post(self,request):
        Client.objects.create(
            ism = request.POST.get('client_name'),
            nom = request.POST.get('client_shop'),
            manzil = request.POST.get('client_address'),
            tel = request.POST.get('client_phone'),
            qarz = request.POST.get('client_debt'),
            ombor = Ombor.objects.get(user=request.user)
        )
        return redirect('client')


class ClientOchir(View):
    def get(self,request,pk):
        client = Client.objects.get(id=pk)
        if Ombor.objects.get(user=request.user) == client.ombor:
            client.delete()
        return redirect('client')


class ClientUpdate(View):
    def get(self,request,pk):
        client = Client.objects.get(id=pk)
        if client.ombor == Ombor.objects.get(user=request.user):
            data = {"client":client}
            return render(request,'client_update.html',data)
        return redirect('client')
    def post(self,request,pk):
        Client.objects.filter(id=pk).update(
            tel = request.POST.get('client_phone'),
            qarz = request.POST.get('client_qarz')
        )
        return redirect('client')



class MahsulotlarView(View):
    def get(self,request):
        # ombor1 = Mahsulot.objects.filter(ombor__user=request.user)
        # data = {'mahsulot':ombor1}
        mahsulot = request.GET.get("qidirish")
        if mahsulot is None or mahsulot == "":
            ombor1 = Mahsulot.objects.filter(ombor__user=request.user)
        else:
            ombor1 = Mahsulot.objects.filter(nom__contains=mahsulot)
        data = {'mahsulot': ombor1}
        return render(request,"products.html",data)
    def post(self,request):
        Mahsulot.objects.create(
            nom = request.POST.get('pr_name'),
            brend = request.POST.get('pr_brend'),
            narx = request.POST.get('pr_price'),
            berilgan_sana = request.POST.get('pr_date'),
            miqdori = request.POST.get('pr_amount'),
            olchov = request.POST.get('pr_measurement'),
            ombor = Ombor.objects.get(user=request.user)
        )
        return redirect('mahsulotlar')



class MahsulotOchir(View):
    def get(self,request,pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        if Ombor.objects.get(user=request.user) == mahsulot.ombor:
            mahsulot.delete()
        return redirect('mahsulotlar')


class MahsulotUpdate(View):
    def get(self,request,pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        if mahsulot.ombor == Ombor.objects.get(user=request.user):
            data = {"product":mahsulot}
            return render(request,'product_update.html',data)
        return redirect('mahsulotlar')
    def post(self,request,pk):
        Mahsulot.objects.filter(id=pk).update(
            narx=request.POST.get('price'),
            miqdori = request.POST.get('amount')
        )
        return redirect('mahsulotlar')





# mahsulot = request.GET.get("qidirish")
# if mahsulot is None or mahsulot == "":
#     ombor1 = Mahsulot.objects.all()
# else:
#     ombor1 = Mahsulot.objects.filter(nom__contains=mahsulot)
# data = {'mahsulot': ombor1}



