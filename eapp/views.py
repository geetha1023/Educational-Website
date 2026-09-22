
from django.shortcuts import render, redirect
from .models import ParentRegistration



# Create your views here.

def homeview(request):
    return render(request,'eapp/home.html')

def aboutview(request):
    return render(request,'eapp/about.html')

def cseview(request):
    return render(request,'eapp/cse.html')

def eceview(request):
    return render(request,'eapp/ece.html')

def eeeview(request):
    return render(request,'eapp/eee.html')


def photoview(request):
    return render(request,'eapp/photos.html')

def videoview(request):
    return render(request,'eapp/videos.html')

def latestnewsview(request):
    return render(request,'eapp/latestnews.html')


def parent_register(request):
    if request.method == "POST":
        ParentRegistration.objects.create(
            parent_name=request.POST.get("parent_name"),
            contact=request.POST.get("contact"),
            email=request.POST.get("email"),
            student_name=request.POST.get("student_name"),
            address=request.POST.get("address"),
        )

        return redirect('admin_page')

    return render(request, 'eapp/parent_reg.html')


def admin_page(request):
    parents = ParentRegistration.objects.all()

    return render(request, 'eapp/admin.html', {"parents": parents})

from django.shortcuts import render, redirect
from .models import ContactMessage


from django.shortcuts import render, redirect
from .models import ParentRegistration, ContactMessage


def contact(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            contact=request.POST.get("contact"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )

        return redirect("admin_page")

    return render(request, 'eapp/contact.html')


def admin_page(request):
    parents = ParentRegistration.objects.all().order_by("-id")
    contacts = ContactMessage.objects.all().order_by("-id")

    return render(
        request,
        'eapp/admin.html',
        {
            "parents": parents,
            "contacts": contacts
        }
    )











