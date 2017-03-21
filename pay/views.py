from django.shortcuts import render , get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from .forms import MyRegistrationForm
from .models import User, Pay
from twilio.rest import TwilioRestClient


# Create your views here.

def logout_user(request):
    logout(request)
    form = MyRegistrationForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'pay/trylogin.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #albums = Album.objects.filter(user=request.user)
                return render(request, 'pay/index.html')
            else:
                return render(request, 'pay/trylogin.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'pay/trylogin.html', {'error_message': 'Invalid login'})
    return render(request, 'pay/trylogin.html')

def register(request):
    form = MyRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'pay/index.html')
    return render(request, 'pay/tryregister.html',{'form':form})

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'pay/trylogin.html')
    else:
        data = Pay.objects.filter(user=request.user)
        if request.method == "POST":
            check = request.POST['checkbox']
            if check:
                data.is_yes = "True"
            return render(request, 'pay/gateway.html',{'user':user})
        return render(request, 'pay/index.html',{'data':data})

def bank_detail(request):
    if not request.user.is_authenticated():
        return render(request, 'pay/trylogin.html')
    else:
        return render(request, 'pay/bank_detail.html')

def gateway(request):
    if not request.user.is_authenticated():
        return render(request, 'pay/trylogin.html')
    else:

        account_sid = "ACa6d4cb06b269945f34462a435110511f"
        auth_token = "4c74480dcf8daab2fc8a078e5ca40d43"
        client = TwilioRestClient(account_sid, auth_token)

        message = client.messages.create(to="+917610002521", from_="+13176224171",
                                                 body="you have selected autopay next time you can pay automatically via calling to TOLL FREE no. 1800 1234 5678 ")



        return render(request, 'pay/gateway.html')
