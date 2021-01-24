from time import sleep
from random import randint
from django.shortcuts import render
from django.http import StreamingHttpResponse

# Generation range, both for time and value
MIN_TIME = 1
MAX_TIME = 5
MIN_VALUE = 1
MAX_VALUE = 100

# View to provide main web page, index.html
def index(request):
    return render(request, 'index.html', {})

# Random numbers stream
def stream(request):
    def event_stream():
        while True:
            v = randint(MIN_VALUE, MAX_VALUE)
            yield 'data: %s\n\n' % v
            t = randint(MIN_TIME, MAX_TIME)
            sleep(t)
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
