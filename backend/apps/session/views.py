from django.contrib.auth import logout
from .models import Session, MaterialSession, Question, Material, Option, CustomUserOption
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import SessionForm, QuestionForm, MaterialForm, OptionForm
from django.shortcuts import render, redirect
from ..course.models import Course

# Create your views here.

@login_required
def show_session(request, session_id):
    """
    Muestra los detalles de una sesión específica, incluyendo los materiales asociados a la sesión.

    Parámetros:
    - session_id: ID de la sesión a mostrar.

    Comportamiento:
    - Recupera la sesión usando el session_id.
    - Obtiene los materiales asociados a esa sesión.
    - Renderiza el template 'show_session.html' con la sesión y los materiales.
    """
    session = get_object_or_404(Session, session_id=session_id)
    materials = Material.objects.filter(materialsession__session_id=session_id)

    return render(request, 'show_session.html', {
        'session': session,
        'materials': materials,
    })

@login_required
def create_session(request, course_id):
    """
    Permite a un profesor o administrador crear una nueva sesión para un curso determinado.

    Parámetros:
    - course_id: ID del curso al que se va a asociar la nueva sesión.

    Comportamiento:
    - Verifica si el usuario es un profesor. Si no lo es, redirige a la página de cursos del estudiante.
    - Si el método HTTP es GET, muestra el formulario de creación de sesión.
    - Si el método HTTP es POST, procesa el formulario y guarda la nueva sesión asociada al curso.
    - Redirige al detalle del curso ('show_course') si la sesión se crea correctamente.
    """
    if not request.user.isTeacher:
        return render(request, 'student_courses.html')

    course = get_object_or_404(Course, course_id=course_id)

    if request.method == 'GET':
        return render(request,'create_session.html',{
            'form': SessionForm, 'course': course,
        })
    else:
        form = SessionForm(request.POST)
        if form.is_valid():
            new_session = form.save(commit=False)
            new_session.course_id = course
            new_session.user = request.user
            new_session.save()
            session_id = new_session.session_id
            return redirect('show_course', course_id=course_id)

        else:
            return render(request, 'create_session.html', {
                'form': form,
                'errors': form.errors
            })

@login_required
def create_material(request, session_id):
    """
    Permite a un profesor o administrador agregar materiales a una sesión.

    Parámetros:
    - session_id: ID de la sesión a la que se agregarán los materiales.

    Comportamiento:
    - Verifica si el usuario tiene permisos para agregar materiales (profesor o administrador).
    - Si el método HTTP es GET, muestra el formulario para agregar materiales.
    - Si el método HTTP es POST, procesa el formulario y guarda el nuevo material asociado a la sesión.
    - Redirige a la vista de la sesión después de guardar el material.
    """
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return render(request, 'student_courses.html', {'session': session})

    session = get_object_or_404(Session, pk=session_id)

    if request.method == 'GET':
        return render(request,'create_material.html',{
            'form': MaterialForm,
            'session': session
        })
    else:
        form = MaterialForm(request.POST)
        if form.is_valid():
            new_material = form.save(commit=False)
            new_material.user = request.user
            new_material.save()
            MaterialSession.objects.create(
                session_id=session,
                material_id=new_material
            )
            return redirect('show_session', session_id=session.session_id)

        else:
            return render(request, 'create_material.html', {
                'form': form,
                'errors': form.errors,
                'session': session
            })

@login_required
def create_question(request, session_id):
    """
    Permite a un profesor o administrador crear una nueva pregunta para una sesión.

    Parámetros:
    - session_id: ID de la sesión a la que se agregará la nueva pregunta.

    Comportamiento:
    - Verifica si el usuario es un profesor o administrador. Si no lo es, redirige a la vista de la sesión.
    - Si el método HTTP es POST, procesa el formulario de pregunta y lo guarda.
    - Redirige a la vista para elegir el número de opciones después de guardar la pregunta.
    """
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    if request.method == 'POST':
        question_form = QuestionForm(request.POST)

        if question_form.is_valid():
            new_question = question_form.save(commit=False)
            new_question.session_id = session
            new_question.user = request.user
            new_question.save()

            return redirect('choose_num_options', session_id=session_id, question_id=new_question.question_id)

        else:
            return render(request, 'create_question.html', {
                'question_form': question_form,
                'session': session,
            })

    else:
        question_form = QuestionForm()
        return render(request, 'create_question.html', {
            'question_form': question_form,
            'session': session
        })

@login_required
def choose_num_options(request, session_id, question_id):
    """
    Permite al profesor elegir cuántas opciones (por defecto 4) tendrá una pregunta.

    Parámetros:
    - session_id: ID de la sesión donde está la pregunta.
    - question_id: ID de la pregunta a la que se agregarán las opciones.

    Comportamiento:
    - Si el método HTTP es POST, redirige al formulario de opciones con el número elegido.
    """
    session = get_object_or_404(Session, pk=session_id)
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    if request.method == 'POST':
        num_options = int(request.POST.get('num_options', 4))

        return redirect('create_options', session_id=session_id, question_id=question_id, num_options=num_options)

    return render(request, 'choose_num_options.html', {
        'question': question,
        'session': session
    })

@login_required
def show_questions(request, session_id):
    """
    Muestra todas las preguntas de una sesión.

    Parámetros:
    - session_id: ID de la sesión a la que pertenecen las preguntas.

    Comportamiento:
    - Si el usuario es profesor o administrador, muestra todas las preguntas de la sesión.
    - Si no, redirige a la vista de la sesión.
    """
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    questions = Question.objects.filter(session_id=session_id)

    return render(request, 'show_questions.html', {'questions': questions, 'session': session})

@login_required
def show_options(request, session_id, question_id):
    """
    Muestra las opciones para una pregunta específica de una sesión.

    Parámetros:
    - session_id: ID de la sesión.
    - question_id: ID de la pregunta a la que se agregarán las opciones.

    Comportamiento:
    - Si el usuario es profesor o administrador, muestra las opciones de la pregunta.
    """
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=question.session_id)

    options = Option.objects.filter(question_id=question_id)
    return render(request, 'show_options.html', {'options': options})

@login_required
def create_options(request, session_id, question_id, num_options):
    """
    Permite crear las opciones para una pregunta específica de una sesión.

    Parámetros:
    - session_id: ID de la sesión.
    - question_id: ID de la pregunta.
    - num_options: Número de opciones a crear.

    Comportamiento:
    - Si el usuario es profesor o administrador, se permite la creación de opciones para la pregunta.
    """
    session = get_object_or_404(Session, pk=session_id)
    question = get_object_or_404(Question, pk=question_id)

    if not request.user.isTeacher and not request.user.isAdmin:
        return redirect('show_session', session_id=session_id)

    form_options = [OptionForm(prefix=f"option_{i}") for i in range(num_options)]

    if request.method == 'POST':
        for form in form_options:
            form = OptionForm(request.POST, prefix=form.prefix)
            if form.is_valid():
                option = form.save(commit=False)
                option.question_id = question
                option.save()

        return redirect('show_session', session_id=session_id)

    return render(request, 'create_options.html', {
        'question': question,
        'session': session,
        'form_options': form_options,
        'num_options': num_options
    })

@login_required
def answer_questions(request, session_id):
    """
    Permite a un estudiante responder las preguntas de una sesión.

    Parámetros:
    - session_id: ID de la sesión.

    Comportamiento:
    - Si el método HTTP es POST, guarda las respuestas del estudiante en el modelo `CustomUserOption`.
    - Redirige al detalle de la sesión después de guardar las respuestas.
    """
    session = get_object_or_404(Session, pk=session_id)

    if not request.user.isStudent:
        return redirect('show_session', session_id)

    questions = Question.objects.filter(session_id=session_id)

    selected_options = {}

    if request.method == 'POST':
        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.question_id}')
            if selected_option_id:
                option = get_object_or_404(Option, pk=selected_option_id)
                CustomUserOption.objects.create(
                    custom_user_id=request.user,
                    option_id=option
                )

        return redirect('show_session', session_id=session_id)

    return render(request, 'answer_questions.html', {
        'session': session,
        'questions': questions,
    })

def exit(request):
    """
    Cierra la sesión del usuario y redirige a la página de inicio.
    """
    logout(request)
    return redirect('home')
