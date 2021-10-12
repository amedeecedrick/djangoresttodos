from todos.views import TodosAPIView, TodoDetailAPIVIEw
from django.urls import path



urlpatterns = [
     path("", TodosAPIView.as_view(), name = "todos"),
     path("<int:id>", TodoDetailAPIVIEw.as_view(), name = "todo"),
      
     # path('create/', CreateTodoAPIView.as_view(),name = "create-todo"),
     # path('list/', TodoListAPIView.as_view(),name = "list-todos")
  
]