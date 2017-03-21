from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(forms.ModelForm):
    re_password = forms.CharField(widget = forms.PasswordInput(attrs = {'placeholder':'Confirm your Password','class':'form-control','name':'confirm'}))


    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'mobile_number', 'email', 'password']
        widgets = {
                'first_name' : forms.TextInput(attrs = {'placeholder':'Enter your First-Name','type':'text','class':'form-control','name':'first_name','id':'first_name'}),
                'last_name': forms.TextInput(attrs = {'placeholder':'Enter your Last-Name','type':'text','class':'form-control','name':'last_name'}),
                'username': forms.TextInput(attrs = {'placeholder':'Enter your Username','type':'text','class':'form-control','name':'username'}),
                'mobile_number': forms.TextInput(attrs = {'placeholder':'Enter your Mobile Number','type':'text','class':'form-control','name':'mobile_number'}),
                'email': forms.EmailInput(attrs = {'placeholder':'Enter your Email','class':'form-control','name':'email'}),
                'password': forms.PasswordInput(attrs = {'placeholder':'Enter your Password','class':'form-control','name':'password'}),
        }
    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 6:
            raise forms.ValidationError('Password not long enough. Should be >= 6')
        return password

    def clean(self):
        if not self.cleaned_data['password'] == self.cleaned_data['re_password']:
            raise forms.ValidationError("Passwords should match")
        return self.cleaned_data










'''
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True,widget=forms.TextInput(attrs={'class' : 'form-control','type':'text','placeholder':'Enter your Email'}))
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    #date_of_birth = forms.DateField(required = True)
    mobile_number = forms.CharField(required = True)


    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'mobile_number', 'email', 'password1', 'password2')


    def save(self, commit = True):
        user = super(UserCreationForm, self).save(commit = False)
        user.password = self.cleaned_data['password']
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        #user.date_of_birth = self.cleaned_data['date_of_birth']
        user.mobile_number = self.cleaned_data['mobile_number']

        if commit:
            user.save()

        return user

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')
'''
'''
class RegisterForm1(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password','first_name','last_name']

class RegisterForm2(forms.ModelForm):
    dob = forms.DateField()

    class Meta:
        model = UserProfile
        fields = ['phonenumber','dob']
'''
