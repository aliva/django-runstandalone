from django.http.response import HttpResponse

def root(request):
    return HttpResponse('''Hello!
        <hr>
        <img src='/static/django.png' />
    ''')
