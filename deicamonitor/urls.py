#Django lib
from django.urls import path
from django.http import HttpResponse
#localViews
from lines import views as line_views
from users import views as user_views



def main(request):
    """Return Greattin"""
    return HttpResponse('Start_Service')


urlpatterns = [
      path('main/',main),
      path('lines/',line_views.list_lines),
]
