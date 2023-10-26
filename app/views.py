from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.
def near_view(request:HttpRequest, n:int) -> HttpResponse:
    if n >= 90 and n <= 110:
        answer = True
    elif n >= 190 and n <= 210:
        answer = True
    else:
        answer = False
    return HttpResponse(f"{answer}")
def string_view(request:HttpRequest, string:str) -> HttpResponse:
    newString = ""
    for i in range(len(string) + 1):
        newString += string[:i]
    return HttpResponse(newString)
def cat_dog_view(request:HttpRequest, usr_input:str) -> HttpResponse:
    cat_count = usr_input.count('cat')
    dog_count = usr_input.count('dog')
    return HttpResponse(cat_count == dog_count)
def lone_view(request:HttpRequest, x:int, y:int, z:int) -> HttpResponse:
    if x == y and y == z :
        return HttpResponse('0')
    elif x == y :
        return HttpResponse(z)
    elif x == z :
        return HttpResponse(y)
    elif y == z :
        return HttpResponse(x)
    else:
        return HttpResponse(x+y+z)