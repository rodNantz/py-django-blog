from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        "alunos": [
            "michael",
            "dwight",
            "pam",
            "jim"
        ]
    }
    return render(request, 'aula4.html', context)

#class MeuTemplate(TemplateView)
