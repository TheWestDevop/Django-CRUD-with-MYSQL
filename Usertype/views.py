from django.shortcuts import render, redirect
from .models import UserType
from .forms import UserTypeForm

# Create your views here.
def list_usertypes(request):

    usertypes = UserType.objects.all()

    return render(request,'UserTypes.html',{'userTypes': usertypes})  



def create_usertype(request):
    form = UserTypeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_usertypes')

    return render(request,'UserType-form.html',{'form': form})   


def update_usertype(request,id):
    usertype  = UserType.objects.get(id=id) 
    form = UserTypeForm(request.POST or None, instance=usertype)

    if form.is_valid():
        form.save()
        return redirect('list_usertypes')


    return render(request,'UserType-form.html',{'form': form , 'usertype':usertype})

    
def delete_usertype(request,id):

     usertype  = UserType.objects.get(id=id)
     
     if request.method == 'POST':
        userType.delete()
        return redirect('list_usertypes')
      

     return render(request,'UserType-delete.html',{'UserType': usertype}) 