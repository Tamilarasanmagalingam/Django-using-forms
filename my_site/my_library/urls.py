from django.urls import path
from .import views

# register the app namespace
# URL names

app_name = 'my_library'

urlpatterns = [
#     path('simple_view/',views.simple_view)
#     path('<topic>/',views.lib_news)
#     path('<event>',views.journolism)
#     path('<int:num1>/<int:num2>/',views.add_views)
#     path('simple_view/',views.template_simple_view)
#     path('variable/',views.variable_view,name='variable'),
      path('thankyou/',views.thank_you,name='thank_you'),
      path('list_person/',views.list_customers),
      path('add/',views.add,name='add'),
      path('delete/',views.delete,name='delete'),
      path('rental_review/',views.rental_review,name='rental_review')
]
