from django.shortcuts import render
from django.views import generic
# Create your views here.


class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_main/index.html'
        return render(request, 'index.html')
