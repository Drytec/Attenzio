from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import StudentRegisterForm, TeacherRegisterForm

def home(request):
    """
    Vista para la página de inicio.

    Esta vista devuelve la página principal del sitio (home.html).
    No requiere que el usuario esté autenticado.
    """
    return render(request, 'home.html')

@login_required
def logout_view(request):
    """
    Vista para desloguear a un usuario.

    - Cierra la sesión del usuario actual.
    - Redirige al usuario a la página de inicio de sesión u otra página definida.

    Requiere que el usuario esté autenticado antes de acceder.
    """
    if request.method == 'GET':
        logout(request)
        return redirect('login')

def select_user_type_view(request):
    """
    Vista para que el usuario seleccione el tipo de cuenta (estudiante o profesor).

    Cuando el usuario selecciona un tipo de cuenta (student o teacher), lo redirige a la vista de registro correspondiente.
    """
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type in ['student', 'teacher']:
            return redirect(f'/signup/?type={user_type}')
    return render(request, 'select_user_type.html')

def user_singup_view(request):
    """
    Vista para el registro de nuevos usuarios (estudiantes o profesores).

    - Si el tipo de usuario es 'teacher', se muestra el formulario de registro para profesores.
    - Si el tipo de usuario es 'student', se muestra el formulario de registro para estudiantes.

    El formulario guarda los datos del nuevo usuario y redirige al inicio de sesión si el registro es exitoso.
    """
    user_type = request.GET.get('type', None)

    # Selección del formulario dependiendo del tipo de usuario
    if user_type == 'teacher':
        form_class = TeacherRegisterForm
    else:
        form_class = StudentRegisterForm

    if request.method == 'GET':
        form = form_class()
        return render(request, 'signup.html', {'form': form, 'user_type': user_type})

    # Procesar los datos del formulario
    form = form_class(request.POST, request.FILES)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])  # Cifrar la contraseña
        user.save()
        return redirect('login')

    return render(request, 'signup.html', {'form': form, 'user_type': user_type})

def user_login_view(request):
    """
    Vista para el inicio de sesión del usuario.

    - Si el método es GET, se muestra el formulario de inicio de sesión.
    - Si el método es POST, se autentica al usuario con los datos proporcionados.
    - Si la autenticación es exitosa, el usuario es redirigido a la página de inicio.
    - Si la autenticación falla, se muestra un mensaje de error.
    """
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    elif request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        # Validación de los campos
        if not email or not password:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Ambos campos son obligatorios'
            })

        user = authenticate(request, username=email, password=password)

        # Verificación de credenciales incorrectas
        if user is None:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrecto'
            })

        """if not user.validate:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Tu cuenta necesita ser validada por un administrador.'
            })"""

        # Autenticación exitosa
        login(request, user)
        return redirect('home')

