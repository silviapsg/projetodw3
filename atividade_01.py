from flask import Flask, render_template, request, redirect, flash
import re

site = Flask(__name__)
site.secret_key = 'senhasecreta'

@site.route("/")
def index():
    return render_template('index.html')

@site.route('/login')
def login():
    return render_template('login.html')

@site.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@site.route("/autenticar", methods=['POST', ]) 
def autenticar():
    senha = request.form['senha']
    # Não foi feita nenhum armazenamento em Banco de Dados ou similares AINDA. 
    # A senha só é inválida por causa dos critérios de senha pedidas na atividade.
    if (len(senha) < 6) or (not re.search(r'[A-Z]', senha)) or (not re.search(r'[0-9]', senha)) or (not re.search(r'[!@#$%^&*]', senha)):
        flash('Senha inválida!')
        return redirect('/login')
    else: 
        return redirect ('/')
    
@site.route("/cadastrar", methods=['POST', ]) 
def cadastrar():
    senha = request.form['senha']
    confirmar_senha = request.form['confirmar_senha']
    if (len(senha) < 6) or (not re.search(r'[A-Z]', senha)) or (not re.search(r'[0-9]', senha)) or (not re.search(r'[!@#$%^&*]', senha)):
        flash('Senha inválida! Sua senha deve conter no mínimo 6 dígitos, 1 letra maiúscula, 1 número e 1 caractere especial.')
        return redirect('/cadastro')
    if confirmar_senha != senha:
        flash('Senhas digitadas não correspondem!')
        return redirect('/cadastro')
    else:
        # A princípio, após finalizar o cadastro o usuário será redirecionado a página de Login.
        return redirect ('/login')

if __name__ == "__main__": 
    site.run(port = 8080, debug=True)