from django.contrib.auth import authenticate, login


"""
Logueo users
"""
def set_authenticate(request):
    username = request.POST["username"]
    password = request.POST["password"]
    result = {
        'msj': None,
        'error': None
    }
    try:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            result['msj'] = 'Logueado Satisfactoriamente'
        else:
            result['error'] = 'Credenciales Inválidos'
    except Exception as e:
        result['error'] = f'An ocurre an error -> {e}'
        
    return result



"""
Register User
"""
def set_register(request):
    username = request.POST['']
    password = request.POST['']
    password_confirme = request.POST['']
    email = request.POST['']
    result = {
        'msj': None,
        'error': None
    }