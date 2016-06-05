from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    #return "Hello, World!"
    user = {'nickname': 'John'}
    # return '''
    # <html>
    #     <head>
    #         <title>Home Page</title>
    #     </head>
    #     <body>
    #         <h1>Hello, ''' + user['nickname'] + '''</h1>
    #     </body>
    # </html>
    # '''
    user = {'nickname': 'John'}
    posts = [
        {'author': {'nickname': 'John'}, 'body': 'Beautiful day in Portland!'},
        {'author': {'nickname': 'Susan'}, 'body': 'The Avengers movie was cool!'}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)