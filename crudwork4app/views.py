# views.py

from django.shortcuts import redirect, render
from .models import student
from django.core.files import File
import imghdr  

def crud(request):
    return render(request, 'crud 1.html')
def add_product(request):
    if request.method == 'POST':
        pname = request.POST.get('pname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        qualification = request.POST.get('qualification')
        gender = request.POST.get('gender')
        image = request.FILES.get('file')

       
        if age is not None and dob is not None:
            try:
                age = float(age)
                dob = float(dob)
            except ValueError:
              
                pass

        prd = student(
            first_name=pname,
            last_name=lname,
            age=age,
            dob=dob,
            qualification=qualification,
            gender=gender,
            image=image
        )
        prd.save()
        return redirect('show_products')




def show_products(request):
    prdts = student.objects.all()
    return render(request, 'show_product.html', {'prdts': prdts})

def edit_product_details(request, pk):
    pr = student.objects.get(id=pk)

    if request.method == 'POST':
        pr.first_name = request.POST.get('first_name')
        pr.last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        
       
        if age is not None and dob is not None:
            try:
                pr.age = int(age)
                pr.dob = int(dob)
            except ValueError:
               
                pass
        
        pr.qualification = request.POST.get('qualification')
        pr.gender = request.POST.get('gender')

        pr.save()
        return redirect('show_products')

    return render(request, 'edit.html', {'product': pr})

def deletepage(request, pk):
    product_detail = student.objects.get(id=pk)
    product_detail.delete()
    return redirect('show_products')

def update_product_image(request, pk):
    if request.method == 'POST':
        pr = student.objects.get(id=pk)
      

        pr.first_name = request.POST.get('first_name')
        pr.last_name = request.POST.get('last_name')
        pr.age = request.POST.get('age')
        pr.dob = request.POST.get('dob')
        
        pr.qualification = request.POST.get('qualification')
        pr.gender = request.POST.get('gender')
        old=pr.image
        new=request.FILES.get('file')
        if old !=None and new==None:
            pr.image=old
        else:
            pr.image=new
        pr.save()
        return redirect('show_products')

    return render(request, 'edit.html', {'product': pr})






