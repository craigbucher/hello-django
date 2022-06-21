"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from urllib.parse import urlparse
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math

def rectArea(request):
    print('rectangleArea route')
    height = int(request.GET.get('height'))
    width = int(request.GET.get('width'))
    area = height * width
    response = HttpResponse(f'<h1>The area of a rectangle with height: {height} and width: {width} is {area}</h1>')
    return response

def rectPerim(request):
    print('rectangleArea route')
    height = int(request.GET.get('height'))
    width = int(request.GET.get('width'))
    perimeter = (2* height) + (2 * width)
    response = HttpResponse(f'<h1>The perimeter of a rectangle with height: {height} and width: {width} is {perimeter}</h1>')
    return response

def circArea(request):
    radius = int(request.GET.get('radius'))
    # print('radius')
    area = (math.pi * radius) ** 2
    response = HttpResponse(f'<h1>Area of the circle is {area}</h1>')
    return response

def circPerim(request):
    radius = int(request.GET.get('radius'))
    # print('radius')
    perimeter = 2 * math.pi * radius
    response = HttpResponse(f'<h1>Area of the circle is {perimeter}</h1>')
    return response

def rectangleArea(request, height, width):
    print('rectangleArea route')
    area = height * width
    response = HttpResponse(f'<h1>The area of a rectangle with height: {height} and width: {width} is {area}</h1>')
    return response

def rectanglePerim(request, height, width):
    print('rectanglePerim route')
    perimeter = (2 * height) + (2 * width)
    response = HttpResponse(f'<h1>The perimeter of a rectangle with height: {height} and width: {width} is {perimeter}</h1>')
    return response

def circleArea(request, radius):
    print('circleArea route')
    area = (math.pi * radius) ** 2
    response = HttpResponse(f'<h1>The area of a circle with radius: {radius} is {area}</h1>')
    return response

def circlePerimeter(request, radius):
    print('circlePerimeter route')
    perimeter = 2 * math.pi * radius
    response = HttpResponse(f'<h1>The perimeter of a circle with radius: {radius} is {perimeter}</h1>')
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/', rectArea),
    path('rectangle/perimeter/', rectPerim),
    path('circle/area/', circArea),
    path('circle/perimeter/', circPerim),
    path('rectangle/area/<int:height>/<int:width>/', rectangleArea),
    path('rectangle/perimeter/<int:height>/<int:width>/', rectanglePerim),
    path('circle/area/<int:radius>/', circleArea),
    path('circle/perimeter/<int:radius>/', circlePerimeter),
]
