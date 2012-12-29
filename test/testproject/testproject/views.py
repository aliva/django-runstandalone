from django.http.response import HttpResponse

def root(request):
    return HttpResponse('''
        <title>Django Run Stand Alone Test project</title>
        Hello!
        <hr>
        <img src='/static/django.png' />
    ''')
