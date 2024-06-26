from estudo import app, db  
from flask import render_template, url_for, request, redirect

from estudo.models import Contato, Post
from estudo.forms import ContatoForm, UserForm, LoginForm, PostForm, PostComentarioForm

from flask_login import login_user, logout_user, current_user


@app.route('/', methods=['GET','POST'])
def index():
    
    form = LoginForm()
    if form.validate_on_submit():
        user = form.login()
        login_user(user, remember=True)
   
    return render_template('index.html',  form=form)



@app.route('/cadastro/', methods=['GET','POST'])
def cadastro():
    form = UserForm()
    if form.validate_on_submit():
        user = form.save()
        login_user(user, remember=True)
        return redirect(url_for('index'))
    return render_template('cadastro.html', form=form)


@app.route('/sair/')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/post/novo/', methods=['GET','POST'])
def PostNovo():
    form = PostForm()
    if form.validate_on_submit():
        form.save(current_user.id)
        return redirect(url_for('index'))
    return render_template('post_novo.html', form=form)

@app.route('/post/lista/')
def PostLista():
    posts = Post.query.all()

    print(current_user.posts)
    return render_template('post_lista.html', posts=posts)

@app.route('/post/<int:id>/', methods=['GET','POST'])
def PostDetail(id):
    post = Post.query.get(id)
    form = PostComentarioForm()
    if form.validate_on_submit():
        form.save(current_user.id, id)
        return redirect(url_for('PostDetail', id=id))
    return render_template('post.html', post=post, form=form)

@app.route('/contato/', methods=['GET','POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('index'))

    return render_template('contato.html', context = context, form=form)



@app.route('/contato/lista/')
def contatoLista():

    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa', '')

    dados = Contato.query.order_by('nome')
   #dados = Contato.query.all()

    if pesquisa != '':
        dados = dados.filter_by(nome=pesquisa)
    print(dados.all())
    context={'dados': dados.all()}
    return render_template('contato_lista.html', context=context)

@app.route('/contato/<int:id>/')
def contatoDetail(id):
    obj= Contato.query.get(id)

    return render_template('contato_detail.html', obj=obj)


#criação de uma rota que recebe requisições GET e POST
#formato não recomendado. 
@app.route('/contato_old/', methods=['GET','POST'])
def contato_old():
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

    return render_template('contato_old.html', context = context)

# @app.route('/contato/lista/')
# def contatoLista():
#     dados = Contato.query.all()
#     print(dados)
#     context={'dados': dados}
#     return render_template('contato_lista.html', context=context)