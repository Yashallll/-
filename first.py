from bottle import post, request, template
from datetime import datetime

@post('/first', method='post')
def first():    
    year = datetime.now().year