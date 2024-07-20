from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views import View
from ..models import ParentCategory
from ..forms import ParentCategoryForm
from ..decorators import admin_required 

@admin_required
def parent_category_create(request):
    if request.method=='POST':
        form=ParentCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            parent_category = form.save() 
            parent_category.save()  
            return redirect('parent_category_list')
    else:
        form = ParentCategoryForm()  

    return render(request, 'parent_category/parent_category_form.html', {'form': form}) 

@admin_required
def parent_category_update(request, pk):
    parent_category = get_object_or_404(ParentCategory, pk=pk)
    if request.method == 'POST':
        form = ParentCategoryForm(request.POST,request.FILES, instance=parent_category)
        if form.is_valid():
            form.save()
            return redirect('parent_category_list')
    else:
        form = ParentCategoryForm(instance=parent_category)
    return render(request, 'parent_category/parent_category_form.html', {'form': form})


def parent_categories_list(request):
    parent_categories= ParentCategory.objects.all()
    return render(request,'parent_category/parent_category_list.html',{'parent_categories':parent_categories})


@admin_required        
def parent_category_delete(request, pk):
    parentCategory = get_object_or_404(ParentCategory, pk=pk)
    if request.method == 'POST':
        parentCategory.delete()
        return redirect('parent_category_list')
    return render(request, 'parent_category/parent_category_confirm_delete.html', {'ParentCategory': parentCategory})