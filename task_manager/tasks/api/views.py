from rest_framework.decorators import api_view
from rest_framework.response import Response
from tasks.models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getRouts(request):
    routes = [
        'GET api',
        'GET api/tasks',
        'GET /api/tasks/:id',

    ]

    return Response(routes)

@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)