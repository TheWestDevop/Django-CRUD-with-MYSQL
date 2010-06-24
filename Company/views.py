from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm

# Create your views here.
def list_companies(request):

    companies = Company.objects.all()

    return render(request,'companies.html',{'companies': companies})  



def create_company(request):
    form = CompanyForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_companies')

    return render(request,'company-form.html',{'form': form})   


def update_company(request,id):
    company  = Company.objects.get(id=id) 
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect('list_companies')


    return render(request,'company-form.html',{'form': form , 'Company':company})

    
def delete_company(request,id):

     company  = Company.objects.get(id=id)
     
     if request.method == 'POST':
        company.delete()
        return redirect('list_companies')
      

     return render(request,'company-delete.html',{'company': company}) 
