from flask import Flask, render_template, request, redirect
from Jogo import Jogo

app = Flask(__name__)

jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
jogo3 = Jogo('Mortal Kombat', 'Ação', 'SNES')
lista = [jogo1, jogo2, jogo3]

@app.route("/")
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route("/novo")
def novo():
    return render_template('novo.html', titulo='Novo jogo')

@app.route("/criar", methods=['POST',])
def criar():
# request = Helper do Flask para obter o valor do campo dentro do form (HTML), de acordo com o "name" da tag
    nome = request.form['nome']
    # O 'form'= retorna um dicionario e o acesso eh feito pela key
    # ['categoria'] refere-se pelo campo ('name="categoria"') do HTML
    categoria = request.form['categoria']
    console = request.form['console']
    jogo_novo = Jogo(nome, categoria, console)
    lista.append(jogo_novo)
    return redirect('/')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=['POST', ])
def autenticar():
    if 'mestra' == request.form['senha']:
        return redirect('/')
    else:
        return redirect('/login')
    
app.run(debug=True)
