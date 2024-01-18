from flask import Flask, render_template, request, make_response, redirect
import basedados
import aluno
import disciplina

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

comando_cria_tabela_disciplinas="""
CREATE TABLE IF NOT EXISTS Disciplinas(
    codigo INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    ano INTEGER CHECK (ano>0),
    nr_modulos INTEGER CHECK (nr_modulos>0),
    nr_horas INTEGER CHECK (nr_horas>0),
    max_faltas INTEGER CHECK (max_faltas)
)
"""
basedados.executar_sql(ligacao_bd,comando_cria_tabela_disciplinas)

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


if __name__ == "__main__":
    app.run(debug=True)