
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


from restasite.models import MenuItem


def index(request):

    menu_brk = MenuItem.objects.filter(type__exact='BRK').order_by('?')[:6]
    menu_lun = MenuItem.objects.filter(type__exact='LUN').order_by('?')[:6]
    menu_din = MenuItem.objects.filter(type__exact='DIN').order_by('?')[:6]
    context = {'menu_brk': menu_brk, 'menu_lun' : menu_lun, 'menu_din' : menu_din}
    return render(
        request,
        'index.html',
        context=context
    )

def about(request):
    return render(
        request,
        'about.html'

    )
def register(request):
    # Массив для передачи данных шаблонны
    data = {}
    # Проверка что есть запрос POST
    if request.method == 'POST':
        # Создаём форму
        form = UserCreationForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохраняем пользователя
            form.save()
            # Передача формы к рендару
            data['form'] = form
            # Передача надписи, если прошло всё успешно
            data['res'] = "Всё прошло успешно"
            # Рендаринг страницы
            return render(request, 'register.html', data)
    else: # Иначе
        # Создаём форму
        form = UserCreationForm()
        # Передаём форму для рендеринга
        data['form'] = form
        # Рендаринг страницы
    return render(request, 'register.html', data)

def login(request):
    return render(
        request,
        'login.html'
    )
