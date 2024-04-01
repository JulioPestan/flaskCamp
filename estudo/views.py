from estudo import app
from flask import render_template, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nova/')
def novapag():
    return 'Outra rota'