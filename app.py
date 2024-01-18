from flask import Flask, render_template, request, make_response, redirect
import basedados
import aluno
import disciplina
import tabelas
import nota

app = Flask(__name__)

#Rotas
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aceitar_cookies',methods=['POST'])
def aceitar_cookies():
    resposta = make_response(redirect("/"))
    #cookie com prazo de validade de 30 dias
    resposta.set_cookie('aviso','aceitou',max_age=30*24*60*60)
    return resposta

# Rotas do aluno
@app.route('/aluno/adicionar',methods=["GET","POST"])
def aluno_adicionar():
    return aluno.aluno_adicionar()

@app.route('/aluno/listar')
def aluno_listar():
    return aluno.aluno_listar()

#TODO: pesquisar alunos com base no nome => opção para ver notas

@app.route('/aluno/apagar',methods=["POST"])
def aluno_apagar():
    return aluno.aluno_apagar()

@app.route('/aluno/apagar_confirmado',methods=["POST"])
def aluno_apagar_confirmado():
    return aluno.aluno_apagar_confirmado()

@app.route('/aluno/editar',methods=["POST"])
def aluno_editar():
    return aluno.aluno_editar()

@app.route('/aluno/editar_confirmado',methods=["POST"])
def aluno_editar_confirmado():
    return aluno.aluno_editar_confirmado()

#Rotas das disciplinas
#################################################################
@app.route('/disciplina/adicionar',methods=["GET","POST"])
def disciplina_adicionar():
    return disciplina.disciplina_adicionar()

@app.route('/disciplina/listar')
def disciplina_listar():
    return disciplina.disciplina_listar()

@app.route('/disciplina/apagar',methods=["POST"])
def disciplina_apagar():
    return disciplina.disciplina_apagar()

@app.route('/disciplina/apagar_confirmado',methods=["POST"])
def disciplina_apagar_confirmado():
    return disciplina.disciplina_apagar_confirmado()

@app.route('/disciplina/editar',methods=["POST"])
def disciplina_editar():
    return disciplina.disciplina_editar()

@app.route('/disciplina/editar_confirmado',methods=["POST"])
def disciplina_editar_confirmado():
    return disciplina.disciplina_editar_confirmado()

#Rotas das notas
################################################################
@app.route('/nota/adicionar',methods=["GET","POST"])
def nota_adicionar():
    return nota.nota_adicionar()

if __name__ == "__main__":
    app.run(debug=True)