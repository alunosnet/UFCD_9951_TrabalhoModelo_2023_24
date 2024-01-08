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
    #verificar se o método é GET
    if request.method=="GET":   #TODO: fazer o form e o POST
        return render_template('aluno/adicionar.html')

if __name__ == "__main__":
    app.run(debug=True)