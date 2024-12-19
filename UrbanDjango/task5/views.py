from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = ['user015']


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if username in users:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')

            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')

            else:
                users.append(username)
                info['respond'] = f'Приветствуем, {username}!'
                return HttpResponse(f'Приветствуем, {username}!')

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
    return render(request, 'fifth_task/registration_pege.html', context)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username in users:
            info['error'] = 'Пользователь уже существует'
            return HttpResponse('Пользователь уже существует')

        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse('Пароли не совпадают')

        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return HttpResponse('Вы должны быть старше 18')

        else:
            users.append(username)
            info['respond'] = f'Приветствуем, {username}!'
            return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_pege.html', {'info': info})


def form_registration(request):
    return render(request, 'fifth_task/registration.html')
