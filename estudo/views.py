from estudo import app, db  #--> importei o db para gravar dados no banco de dados 
from flask import render_template, url_for,request #--> usei o request para pegar dados do formulário, GET e POST

from estudo.models import Contato #--> importei a classe Contato para instaciar ela, criei um objeto para adicionar no banco

@app.route('/')
def index():
    return render_template('index.html')

#criação de uma rota que recebe requisições GET e POST 
@app.route('/contato/', methods=['GET','POST'])
def novapag():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET', pesquisa)
        context.update({'pesquisa':pesquisa})
    
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']
        

        contato = Contato(
            nome = nome,
            email = email,
            assunto = assunto,
            mensagem = mensagem
        )

        db.session.add(contato) 
        db.session.commit()

    return render_template('contato.html', context = context)

    