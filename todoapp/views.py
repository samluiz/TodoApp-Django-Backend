from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET', 'POST', 'DELETE'])
def taskApi(request):
  if request.method == 'GET':
    tasks = Task.objects.all()
    tasks_serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(tasks_serializer.data, safe=False)

  elif request.method == 'POST':
    task_data = JSONParser().parse(request)
    task_serializer = TaskSerializer(data = task_data)
    if task_serializer.is_valid():
      task_serializer.save()
      return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def taskApiFiltered(request, id):
  try:
    task = Task.objects.get(pk=id)
  except Task.DoesNotExist():
    return JsonResponse({'message': 'This task does not exist'}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    task_serializer = TaskSerializer(task)
    return JsonResponse(task_serializer.data)

  elif request.method == 'PUT':
    task_data = JSONParser().parse(request)
    task_serializer = TaskSerializer(task, data = task_data)
    if task_serializer.is_valid():
      task_serializer.save()
      return JsonResponse(task_serializer.data)
    return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method == 'DELETE': 
        task.delete() 
        return JsonResponse({'message': 'Task deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)