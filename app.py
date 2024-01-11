from flask import Flask, render_template, request, make_response, redirect
import basedados
import aluno

#Criar a base de dados e as tabelas
ligacao_bd=basedados.criar_conexao("notas.bd")

#alunos(nprocesso<pk>,nome,morada,cp,data_nasc,email)
comando_cria_tabela_alunos="""
CREATE TABLE IF NOT EXISTS Alunos(
    nprocesso INTEGER PRIMARY KEY,
    nome TEXT NOT NULL CHECK(length(nome)>=3),
    morada TEXT,
    cp TEXT,
    data_nasc NUMERIC,
    email TEXT NOT NULL CHECK(email LIKE '%@%.%')
)
"""
basedados.executar_sql(ligacao_bd,comando_cria_tabela_alunos)
#disciplinas(codigo<pk>,nome,ano,nr_modulos,nr_horas,max_faltas)

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

if __name__ == "__main__":
    app.run(debug=True)