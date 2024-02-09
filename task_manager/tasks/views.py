from django.shortcuts import render

# Create your views here.

data = [
    {'id': 1, 'title': 'read book', 'description': 'Read a nice book', 'priority':'Low', 'due_date': '1/1/2023', 'completed': 'Completed', 'created_at': '1/1/2023', 'updated_at': '1/1/2023'},
    {'id': 2, 'title': 'Cook food', 'description': 'Cook a nice lunch', 'priority':'Medium', 'due_date': '1/1/2023', 'completed': 'Remaining', 'created_at': '1/1/2023', 'updated_at': '1/1/2023'},
    {'id': 3, 'title': 'Go to gym', 'description': 'Fitness for the body', 'priority':'High', 'due_date': '1/1/2023', 'completed': 'Completed', 'created_at': '1/1/2023', 'updated_at': '1/1/2023'},
    {'id': 4, 'title': 'Code', 'description': 'Always gotta code', 'priority':'Low', 'due_date': '1/1/2023', 'completed': 'Remaining', 'created_at': '1/1/2023', 'updated_at': '1/1/2023'},
]

def home(request):
    return render(request, 'tasks/home.html', {'data': data})

def tasks(request, pk):
    task = None
    for i in data:
        if i['id'] == int(pk):
            task=i
    
    return render(request, 'tasks/tasks.html', {'data': task})