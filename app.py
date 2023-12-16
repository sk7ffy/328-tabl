from flask import Flask,session
from sigma import get_question
count = 0
def index ():
    session['counter'] = 0
    return '<a href="/test">Hello</a>'
def test ():
    
    data = get_question(1,1)
    return f"<h1>{str(data)}</h1>"
def results ():
    return '<h1>Results</h1>'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'aaaa111'
app.add_url_rule('/','home',index)
app.add_url_rule('/test','test',test)
app.add_url_rule('/results','results',results)
app.run()
