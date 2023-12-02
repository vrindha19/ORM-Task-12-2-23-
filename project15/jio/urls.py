from django.urls import path


# # urlpatterns = [
# #     path('members/', views.members, name='members'),
# # ]
# # yourapp/urls.py

from .views import student_list

urlpatterns = [
    path('students/', student_list, name='student_list'),
   
]


# modelform command

# from django.urls import path

# from .views import student_view

# urlpatterns = [
#     # path('members/', views.members, name='members'),
#     path('students/',student_view,name='student_view'),
# ]

