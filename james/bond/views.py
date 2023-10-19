from django.shortcuts import render

def login_view(request):
    if request.method=='POST':
        form=CustomAuthenticationForm(request,data=request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=authenticate(email=email,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else
        form=CustomUserAuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=CustomUserCreationForm()
    return render(request,'register.html',{'form':form})