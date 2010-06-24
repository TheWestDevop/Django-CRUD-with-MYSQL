from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm

# Create your views here.
def list_profiles(request):

    profiles = Profile.objects.all()

    return render(request,'profiles.html',{'profiles': profiles})  



def create_profile(request):
    form = ProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_profiles')

    return render(request,'Profile-form.html',{'form': form})   


def update_profile(request,id):
    profile  = Profile.objects.get(id=id) 
    form = ProfileForm(request.POST or None, instance=profile)

    if form.is_valid():
        form.save()
        return redirect('list_profiles')


    return render(request,'Profile-form.html',{'form': form , 'Profile':profile})

    
def delete_profile(request,id):

     profile  = Profile.objects.get(id=id)
     
     if request.method == 'POST':
        profile.delete()
        return redirect('list_profiles')
      

     return render(request,'Profile-delete.html',{'profile': profile}) 
