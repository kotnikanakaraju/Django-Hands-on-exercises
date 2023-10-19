from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from .models import PageView


def increment_page_view(request,page_name):
    page,created=PageView.objects.get_or_create(page_name=page_name)
    page.view_count+=1
    page.save()
    try:
        response=HttpResponse(f"page{{page_name}} viewed {{page.view_count}} times")
        response.set_cookie(f"page {{page.name}} views",page.view_count)
    except:
        print("deoesnt contain message")
    return response
    
def display_page_view(request,page_name):
    page=get_object_or_404(PageView,page_name=page_name)
    return render(request,"pagecount_app/page_view.html",{"page":page})


