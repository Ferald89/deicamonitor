"""Post Views"""
#Django
from django.http import HttpResponse
from django.shortcuts import render
#utilates
from datetime import datetime
pruebas = "hello world"
posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1004'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQyAu_8yQ3ki3xQw5R8lfK50nU0y8YOOIOE2H14WCW3iVt3qwb6',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://scontent.fmex10-1.fna.fbcdn.net/v/t1.0-9/s960x960/76730698_10220545338168117_4212649351509442560_o.jpg?_nc_cat=101&_nc_ohc=5eQlPnEEujwAQkk9zAEwM9rnaG_aLGHQirj4FrSAe88AJv2w6hTcL7Y4g&_nc_ht=scontent.fmex10-1.fna&oh=0c659fb40d23a9c957c0c9939e4a960f&oe=5E777AE5',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://scontent.fmex10-1.fna.fbcdn.net/v/t1.0-9/s960x960/68583519_2428552510559157_2329846881351368704_o.jpg?_nc_cat=100&_nc_ohc=jGR8iLxAJp0AQmu9rFRwZLaTs3fNSjL4zNPao-65B7obkhz6EuO0WC0vA&_nc_ht=scontent.fmex10-1.fna&oh=8b5a791a8f2b6fc241961814aee82de1&oe=5E7D467A',
    }
]


def list_lines(request):

    return render(request,'lines/feed.html',{'posts':posts,'prueba':pruebas})
