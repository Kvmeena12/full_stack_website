# # home/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#    path('', views.index, name='home'),  # Home page mapped to the `index` view
#     path('about/', views.about_view, name='about'),
#     path('contact/', views.contact, name='contact'),
#     path('register/', views.registerPage, name='register'),
#     path('login/', views.loginPage, name='login'),
#     path('logout/', views.logoutPage, name='logout'),
#     path('', views.index, name='index'),  # Add this line to define the 'index' URL
#     # 
#     # path('post-work/', views.post_work, name='post_work'),
#     path('post-work/', views.post_work, name='post_work'),
#     path('accept-work/<int:work_id>/', views.accept_work, name='accept_work'),

# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This maps to the home view that uses index.html
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('post-work/', views.post_work, name='post_work'),
    path('accept-work/<int:work_id>/', views.accept_work, name='accept_work'),
    path('', views.index, name='index'),  # Home page pattern

]
