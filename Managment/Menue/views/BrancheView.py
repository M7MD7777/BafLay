from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View   
from ..models import Branche
from ..forms import BranchForm
from ..decorators import admin_required 

@admin_required
def branche_create(request):
    if request.method=="POST":
        form=BranchForm(request.POST,request.FILES)
        if form.is_valid():
            branche=form.save()
            branche.save()
            return redirect('branche_list')
        
    else:
        form=BranchForm()
    return render(request,'branche/branche_form.html',{'form':form})        

@admin_required
def branche_update(request,pk):
    branche=get_object_or_404(Branche,pk=pk)
    if request.method=="POST":
        form=BranchForm(request.POST,request.FILES,instance=branche)
        if form.is_valid():
            form.save()
            return redirect('branche_list')
    else:
        form=BranchForm(instance=branche)
    return render(request,'branche/branche_form.html',{'form':form}) 

def branche_list(request):
    branches=Branche.objects.all()
    return render(request,'branche/branche_list.html',{'branches':branches})

@admin_required
def branche_delete(request, pk):
    branche = get_object_or_404(Branche, pk=pk)
    if request.method == 'POST':
        branche.delete()
        return redirect('branche_list')
    return render(request, 'branche/branche_confirm_delete.html', {'branche': branche})



