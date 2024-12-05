from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("todos/", views.todos, name="Todos"), 
    path('booking/', views.booking, name='booking'),
    path('barber/', views.barber, name='barber'),
    path('book-appointment/', views.book_appointment, name='book_appointment'),  
    path('appointment/', views.appointment, name='appointment'),
    path('appointments/edit/<int:appointment_id>/', views.edit_appointment, name='edit_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)