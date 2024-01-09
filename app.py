from flask import Flask, render_template, request, make_response, redirect
import basedados

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
    ligacao_bd = basedados.criar_conexao("notas.bd")
    #verificar se o método é GET
    if request.method=="GET":   
        return render_template('aluno/adicionar.html')
    if request.method=="POST":
        #validar os dados
        nome = request.form.get("input_nome")
        if not nome:
            return render_template('aluno/adicionar.html',mensagem="Tem de preencher o campo do nome")
        if len(nome)<3:
            return render_template('aluno/adicionar.html',mensagem="Nome muito pequeno. Deve ter pelo menos 3 letras")
        morada = request.form.get("input_morada")
        cp = request.form.get("input_cp")
        data_nasc = request.form.get("input_data")
        email = request.form.get("input_email")
        #TODO: guardar fotografia e fazer mais validações
        #adicionar à bd
        sql = "INSERT INTO Alunos(nome,morada,cp,data_nasc,email) VALUES (?,?,?,?,?)"
        parametros = (nome,morada,cp,data_nasc,email)
        basedados.executar_sql(ligacao_bd,sql,parametros)
        return redirect("/aluno/listar")

@app.route('/aluno/listar')
def aluno_listar():
    ligacao_bd = basedados.criar_conexao("notas.bd")
    sql = "SELECT * FROM Alunos"
    dados = basedados.consultar_sql(ligacao_bd,sql)
    return render_template('aluno/listar.html',registos = dados)

#TODO: pesquisar alunos com base no nome

@app.route('/aluno/editar')
def aluno_editar():
    pass

@app.route('/aluno/apagar')
def aluno_apagar():
    pass

if __name__ == "__main__":
    app.run(debug=True)