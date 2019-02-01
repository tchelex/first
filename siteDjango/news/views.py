from django.shortcuts import render
from .models import ListOfStudents

students = [
    {
        'surname': 'Иванов',
        'name': 'Иван',
        'section': 'среда'
    },
    {
        'surname': 'Сидоров',
        'name': 'Дэн',
#        'section': 'четверг'
    }
]

students1 = [
    {
        'surname': 'Петров',
        'name': 'Петр',
        'section': 'понедельник'
    },
    {
        'surname': 'Дуров',
        'name': 'Эдуард',
        'section': 'воскресенье'
    }
]


def home(request):
    data = {                    #словарь
        'students': ListOfStudents.objects.all(),
        'title':'Список учеников'
    }
    return render(request, 'news/home.html', data)

def list(request):
    data = {                    #словарь
        'students1': students1,
        'title':'Другой список учеников'
    }
    return render(request, 'news/list.html', data)