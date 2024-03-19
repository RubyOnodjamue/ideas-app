from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login

from .models import Record

from django.contrib import messages

# - Homepage

def base(request):
    
    return render(request, 'newapps/appendices.html')

# -Registering a user

def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your account has been successfully created!")

            return redirect("login")

    context = {'form':form}

    return render(request, 'newapps/register.html', context=context)


# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("controlpanel")

        context = {'form':form}

        return render(request, 'newapps/register.html', context=context)


# - Dashboard

@login_required(login_url='login')
def controlpanel(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/controlpanel.html', context=context)


# - Create a record 

@login_required(login_url='login')
def add_idea(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record has been created!")

            return redirect("controlpanel")

    context = {'form': form}

    return render(request, 'newapps/add-idea.html', context=context)


# - Update a record 

@login_required(login_url='login')
def update_idea(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record has been updated!")

            return redirect("controlpanel")
        
    context = {'form':form}

    return render(request, 'webapp/update-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context=context)


# - Delete a record

@login_required(login_url='login')
def delete_record(request, pk):

    record = Record.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("controlpanel")



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success! We look forward to your return with fresh new ideas soon!")

    return redirect("login")