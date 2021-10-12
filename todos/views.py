from django.shortcuts import render
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Todo
# from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class TodosAPIView(ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = [ filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'title','description', 'is_complete']
    search_fields = ['id', 'title','description', 'is_complete']
    ordering_fields = ['id', 'title','description', 'is_complete']


    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)

class TodoDetailAPIVIEw(RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = "id"
    def get_queryset(self):
        return Todo.objects.filter(owner = self.request.user)
    

    


# class CreateTodoAPIView(CreateAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)

#     def perform_create(self, serializer):
#         return serializer.save(owner = self.request.user)

    

# class TodoListAPIView(ListAPIView):
#     serializer_class = TodoSerializer
#     permission_classes = (IsAuthenticated,)
#     def get_queryset(self):
#         return Todo.objects.filter(owner = self.request.user)