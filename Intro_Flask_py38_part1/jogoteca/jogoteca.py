from flask import Flask, render_template, request, redirect, session, flash, url_for
from Jogo import Jogo
from Usuario import Usuario

# __name__= Indica que a aplicacao ira executar neste mesmo codigo
app = Flask(__name__)
# 'secret_key'= necessario para utilizar os cookies (session) o que indica uma "assinatura" de criptografia
app.secret_key = "alura"

# Creation of Games from type "Jogo"
jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Ação', 'SNES')

lista = [jogo1, jogo2, jogo3]

# Creation of User from type "Usuario"
usuario1 = Usuario('levy', 'levy berto', '1234')
usuario2 = Usuario('nico', 'Nico Steppat', '7a1')
usuario3 = Usuario('luan', 'luan marques', '321')

usuarios = {usuario1.id: usuario1,
            usuario2.id: usuario2,
            usuario3.id: usuario3}

@app.route("/")
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo'))) #'/login?proxima=novo'
    return render_template('novo.html', titulo='Novo jogo')

@app.route("/criar", methods=['POST',])
# Function chamada pelo 'novo.html' como action='/criar'
def criar():
# request = Helper do Flask para obter o valor do campo dentro do form (HTML), de acordo com o "name" da tag
    nome = request.form['nome']
# O 'form'= retorna um dicionario e o acesso eh feito pela key
# ['categoria'] refere-se pelo campo ('name="categoria"') do HTML
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_novo = Jogo(nome, categoria, console)
    lista.append(jogo_novo)
    return redirect(url_for('index'))

@app.route("/login")
def login():
# "request.args"= Captura os argumentos/parametros passados na url (\login?proxima=novo)
    proxima = request.args.get('proxima')
    return render_template("login.html", proxima=proxima)
# o parm "proxima" foi passado ao html, onde necessitou incluir o seguinte codigo:
##          <input type="hidden" name="proxima" value="{{% proxima %}}" >
# Desta forma a pagina guardou a informacao da proxima pagina que sera mostrada, sem mostrar ao usuario (type="hidden")

@app.route("/autenticar", methods=['POST',])
def autenticar():
# Verifica se o usuario existe no dict usuarios
    if request.form['usuario'] in usuarios:
        user = usuarios[request.form['usuario']]
# Verifica se a senha do usuario (Key) do dicionario eh == a passada no form (HTML)
        if user.senha == request.form['senha']:
# 'sesion'= armazena informacoes por mais de 1 ciclo de request (cria coockie no client)
            session['usuario_logado'] = user.id
            flash(f'Usuário \"{user.nome}\" logou com sucesso!!!')
# Captura o conteudo da tag "input tupe='hidden'" que guarda a info de prox_pag (origem: app.route(/novo))
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash(f'Nenhum usuário está logado!!!')
        return redirect(url_for('login'))

@app.route("/logout")
def logout():
    session['usuario_logado'] = None
    flash(f'Nenhum usuário está logado!!!')
    return redirect(url_for('index'))

app.run(debug=True)
