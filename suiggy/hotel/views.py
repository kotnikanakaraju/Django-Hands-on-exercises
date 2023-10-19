from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from suiggy.hotel.forms import HotelForm
from suiggy.hotel.models import Hotel

def hotel_list(request):
    hotels=Hotel.objects.all()
    return render(request,'hotel/hotel_list.html',{'hotels':hotels})

@login_required
def hotel_details(request,name):
    hotel=get_object_or_404(Hotel(Hotel,pk=name))
    return render(request,'hotel/hotel_details.html',{'hotel':hotel})

@staff_member_required
def hotel_create(request):
    if request.method == 'POST':
        form=HotelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hotel_list')
    else:
        form=HotelForm()
    return render(request,'hotel/hotel_create.html',{'form':form})

@staff_member_required
def hotel_update(request,name):
    hotel=get_object_or_404(Hotel,pk=name)
    if request.method == 'POST':
        form=HotelForm(request.POST,instance=hotel)
        form.save()
        return redirect('hotel_list')
    else:
        form=HotelForm(instance=hotel)
    return render(request, 'hotel/hotel_update.html',{'form':form})

@staff_member_required
def hotel_delete(request,name):
    hotel=get_object_or_404(Hotel,pk=name)
    if request.method == 'POST':
        hotel.delete()
        return redirect('hotel_list')
    return render(request, 'hotel/hotel_delete.html',{'hotel':hotel})
        
    



    
