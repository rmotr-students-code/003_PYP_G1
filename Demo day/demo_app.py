import os
from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
from savings import Savings

app = Flask(__name__) 
app.config.from_object('config.DevConfig')
Bootstrap(app)

@app.route('/')
def home():
    form = Savings()
    if request.method == 'POST':
        if request.form['submit'] == 'calculate' and form.validate_on_submit():
            savings_program()
            return render_template('home.html', variable1 = variable1, variable2 = variable2)
            
   

if __name__ == '__main__':
    app.debug = True
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)