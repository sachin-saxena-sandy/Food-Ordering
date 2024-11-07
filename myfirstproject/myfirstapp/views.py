from django.shortcuts import render, HttpResponse
from datetime import datetime
from myfirstapp.models import Contact 
from django.contrib import messages
from myfirstapp.models import Destination
from .forms import ImageForm
from .models import Image



 


# Create your views here.

def index(request):
   ''' context = {
        'variable1':'This is sent',
        'variable2':'This is already sent',
    }'''
   dest1 = Destination()
   dest1.name = 'TATA'
   dest1.desc = 'Tata Motors, Indias largest commercial vehicle manufacturer, today introduced its technologically-advanced engine.'
   dest1.img = 'static/4.jpg'
  
   
   
   dest2 = Destination()
   dest2.name = 'ASHOK LEYLAND'
   dest2.desc = 'Ashok Leyland, flagship of the Hinduja group, is the 2nd largest manufacturer of commercial vehicles in India, the 4th largest manufacturer of buses in the world, and the 19th largest manufacturers of trucks.'
   dest2.img = 'static/5.jpg'

   
   
   dest3 = Destination()
   dest3.name = 'EICHER'
   dest3.desc = 'Eicher Motors Limited is an Indian multinational automotive company that manufactures motorcycles and commercial vehicles, headquartered in New Delhi.'
   dest3.img = 'static/6.jpg'
 
   
   
   dests = [dest1, dest2, dest3]

   return render(request, 'index.html', {'dests': dests})
    #return HttpResponse("This is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is about page")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is services page")


def addvehicle(request):
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ImageForm()
    return render(request, 'addvehicle.html', context={'form': form}) 




'''def image_request(request):  
    if request.method == 'POST':  
        form = UserImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = UserImageForm()  
  
    return render(request, 'image_form.html', {'form': form}) '''
'''try:
    def addvehicle(request):
        if request.method == "POST":
            name = request.POST.get("name")
            img = 
            img = request.POST.get("img")
            desc = request.POST.get("desc")
            addvehicle = Addvehicle(name=name, img=img, desc=desc, date = datetime.today())
            addvehicle.save()
            messages.success(request, 'Your Vehicle Added Sucessfully!')

        return render(request, 'addvehicle.html')
        #return HttpResponse("This is services page")
except Exception:
    print(Exception)'''

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been Sent!')
    
    return render(request, 'contact.html')
    #return HttpResponse("This is contact page")


