from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,Category,Product,Branche,ParentCategory

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'phone_number', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['username'].validators = []
        self.fields['password1'].validators = []  # Remove any validators for password1
        self.fields['password2'].validators = []  # Remove any validators for password2

    def clean_password2(self):
        # Override the clean_password2 method to bypass validation
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields must match.")
        
        # You can add any custom validation logic here if needed
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['username']  # Example assuming username is email
        if commit:
            user.save()
            Profile.objects.create(
                user=user,
                phone_number=self.cleaned_data['phone_number']
            )
        return user 

    


class BranchForm(forms.ModelForm):

    class Meta:
        model = Branche
        fields = ['name', 'country', 'address','image']

class ParentCategoryForm(forms.ModelForm):

    class Meta:
        model = ParentCategory
        fields = ['branche','name', 'description', 'image']
     
class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['parent_category','name', 'description', 'image']

class ProductForm(forms.ModelForm):

    class Meta:
        model=Product
        fields = ['name','description','price','category','image']   




                  
                