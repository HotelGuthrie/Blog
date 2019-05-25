from django.http import HttpReponse


def index(request):
    return HttpResponse(
        'Helloworld rom Django!\n',
        content_type='text/plain'
    )
