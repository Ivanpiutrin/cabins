from django.shortcuts import render, redirect
from cabin_APP.forms import FormRegion, FormCity, FormUserLogin, FormUserRegistration, FormCreateProject, FormPaymenMethod, FormWorker
from cabin_APP.models import Region, City, User, Project, PaymentMethod, Worker

# Create your views here.

def listado_regiones(request):
    regiones = Region.objects.all()
    context = {'regiones': regiones}
    return render(request, 'regiones.html', context)

def ingresar_region(request):
    form = FormRegion()
    if request.method == 'POST':
        form = FormRegion(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_regiones)
    context = {'form': form}
    return render(request, 'ingresar_region.html', context)

def listado_ciudades(request):
    ciudades = City.objects.all()
    context = {'ciudades': ciudades}
    return render(request, 'ciudades.html', context)

def ingresar_ciudades(request):
    form = FormCity()
    if request.method == 'POST':
        form = FormCity(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_ciudades)
    context = {'form': form}
    return render(request, 'ingresar_ciudad.html', context)

def iniciar_sesion(request):
    form = FormUserLogin()
    if request.method == 'POST':
        form = FormUserLogin(request.POST)
        if form.is_valid():
            user = form.data['username']
            password = form.data['password']
            if User.objects.filter(username=user).exists():
                user_consult = User.objects.get(username=user)
                if (user, password) == user_consult.getToLogin():
                    return redirect(main_menu)  
    context = {'form' : form}
    return render(request, 'login.html', context)

def resgistrar_usuario(request):
    form = FormUserRegistration()
    if request.method == 'POST':
        form = FormUserRegistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect(main_menu)
    context = {'form': form}
    return render(request, 'registro.html', context)

def crear_proyecto(request):
    form = FormCreateProject()
    if request.method == 'POST':
        form = FormCreateProject(request.POST)
        if form.is_valid():
            form.save()
            return redirect()
    context = {'form': form}
    return render(request, 'proyecto_nuevo.html', context)

def main_menu(request):
    return render(request, 'menu_principal.html')

def payment_method(request):
    form = FormPaymenMethod()
    if request.method == 'POST':
        form = FormPaymenMethod(request.POST)
        if form.is_valid():
            form.save()
            return redirect(main_menu)
    context = {'form': form}
    return render(request, 'metodo_pago.html', context)
    

def ingresar_maestro(request):
    form = FormWorker()
    if request.method == 'POST':
        form = FormWorker(request.POST)
        if form.is_valid():
            form.save()
            return redirect(listado_maestro)
    context = {'form': form}
    return render(request, 'ingresar_maestro.html', context)

def listado_maestro(request):
    maestros = Worker.objects.all()
    context = {'maestros': maestros}
    return render(request, 'listar_maestro.html', context)