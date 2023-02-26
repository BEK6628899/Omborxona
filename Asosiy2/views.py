from django.shortcuts import render,redirect
from django.views import View
from .models import *
from Asosiy.models import *




class StatistikaView(View):
    def get(self,request):
        if request.user.is_authenticated:
            stats = request.GET.get('qidirish')
            if stats:
                mahsulot = Statistika.objects.filter(mahsulot__nom__contains=stats,ombor__user=request.user)
                client = Statistika.objects.filter(client__ism__contains=stats,ombor__user=request.user)
                statistika = Statistika.objects.filter(sana__contains=stats,ombor__user=request.user)
                data = {'statistikalar':mahsulot|client|statistika}
            else:
                data = {"statistikalar":Statistika.objects.filter(ombor__user=request.user),
                        "mahsulotlar":Mahsulot.objects.filter(ombor__user=request.user),
                        "clients":Client.objects.filter(ombor__user=request.user)}
            return render(request,'stats.html',data)
        return redirect('login')
    def post(self,request):
        Statistika.objects.create(
            mahsulot = Mahsulot.objects.get(id=request.POST.get('pr')),
            client = Client.objects.get(id=request.POST.get('cl')),
            miqdor = request.POST.get('miqdor'),
            umumiy_summa = request.POST.get('u_s'),
            tolandi = request.POST.get('tolandi'),
            nasiya = request.POST.get('nasiya'),
            ombor = Ombor.objects.get(user=request.user)
        )
        m = Mahsulot.objects.get(id=request.POST.get('pr'))
        m.miqdori = int(m.miqdori) - int(request.POST.get('miqdor'))
        m.save()
        C = Client.objects.get(id=request.POST.get('cl'))
        C.qarz = int(C.qarz) + int(request.POST.get('nasiya'))
        C.save()
        return redirect('statistika')



class StatistikaOchir(View):
    def get(self,request,pk):
        stats = Statistika.objects.get(id=pk)
        if Ombor.objects.get(user=request.user) == stats.ombor:
            stats.delete()
        return redirect('statistika')



# class StatistikaUpdate(View):
#     def get(self,request,pk):
#         stats = Statistika.objects.get(id=pk)
#         if stats.ombor == Ombor.objects.get(user=request.user):
#             data = {"client": stats}
#             return render(request, 'stats_update.html', data)
#         return redirect('statistika')
#     def post(self, request, pk):
#         Statistika.objects.filter(id=pk).update(
#              miqdor=request.POST.get('miqdor'),
#              umumiy_summa=request.POST.get('u_s'),
#              tolandi=request.POST.get('tolandi'),
#              nasiya=request.POST.get('nasiya')
#         )
#         return redirect('statistika')





