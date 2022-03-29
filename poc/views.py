from django.http import HttpResponse
import requests
bye_url = 'http://localhost'

def hello(request):
    text = 'Hello World <br><br>'
    r = requests.get(bye_url)
    text = text + r.text

    print(text)

    return HttpResponse(text)
