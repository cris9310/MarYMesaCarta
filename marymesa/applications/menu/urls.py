from django.urls import path
from . import views
app_name = 'menu_app'

urlpatterns = [
   
   path(
      '',
      views.RedirectView,
   ),

   path(
      'letter/',
      views.DishesListview.as_view(), 
      name='letter'
   ),
    
]

