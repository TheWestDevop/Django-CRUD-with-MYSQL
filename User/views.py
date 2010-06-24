from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here.
def list_users(request):

    users = User.objects.all()

    return render(request,'Users.html',{'users': users})  



def create_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request,'User-form.html',{'form': form})   


def update_user(request,id):
    user  = User.objects.get(id=id) 
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('list_users')


    return render(request,'User-form.html',{'form': form , 'user':user})

    
def delete_user(request,id):

     user  = User.objects.get(id=id)
     
     if request.method == 'POST':
        user.delete()
        return redirect('list_users')
      

     return render(request,'User-delete.html',{'user': user}) 

