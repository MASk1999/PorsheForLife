from django.shortcuts import render, redirect
from .models import cars
from .forms import car_registration, owner_registration
from django.contrib import messages
    
# Create your views here.
#This is the view that handles the home page
def home(request):
    return render(request, 'taycan/home.html')

#This is just a demo page that shows that we can have two forms embedded in a page
def nextpage(request):
    form1=car_registration()
    form2=owner_registration()
    return render(request, 'taycan/nextpage.html', {'form1':form1, 'form2':form2})

#This is a page that has a form created using django forms library. This saves the data entered to the cars model in models.py file
def CR(request):
    if request.method == 'POST':
        form = car_registration(request.POST)

        if form.is_valid():
            chass = form.cleaned_data["chass_num"]
            car_m = form.cleaned_data["car_model"]
            colour = form.cleaned_data["color"]
            messages.success(request, f' Registration Successful! ')
            Q = cars(chass_num=chass, car_model=car_m, color=colour)    #Creating an object for the cars model, hence saving data
            Q.save()    #Changes are updated only after saving the object
            return redirect('taycan-home')
    else:
        form = car_registration()
    return render(request,'taycan/CR.html',{'form':form})

#This is a page that has a form created using model forms 
def OR(request):
    if request.method == 'POST':
        form = owner_registration(request.POST)

        if form.is_valid():
            messages.success(request,f'Registration Successful !')
            form.save()     #We don't need to create object in this case. It will be directly saved to the database using form.save()
            return redirect('taycan-home')
    else:
        form=owner_registration()
    return render(request,'taycan/OR.html', {'form':form})

