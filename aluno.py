from flask import Flask, render_template, request, make_response, redirect
import basedados

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

def aluno_listar():
    ligacao_bd = basedados.criar_conexao("notas.bd")
    sql = "SELECT * FROM Alunos"
    dados = basedados.consultar_sql(ligacao_bd,sql)
    return render_template('aluno/listar.html',registos = dados)

def aluno_apagar():
    #nprocesso
    nprocesso = request.form.get("nprocesso")
    #consulta à bd para recolher os dados aluno selecionado
    sql = "SELECT * FROM Alunos WHERE nprocesso=?"
    parametros=(nprocesso,)
    #executar a consulta
    ligacao_bd = basedados.criar_conexao("notas.bd")
    dados =  basedados.consultar_sql(ligacao_bd,sql,parametros)
    return render_template("aluno/apagar.html",registo = dados[0])

def aluno_apagar_confirmado():
    #nprocesso
    nprocesso = request.form.get("nprocesso")
    print(nprocesso)
    sql = "DELETE FROM Alunos WHERE nprocesso=?"
    parametros=(nprocesso,)
    ligacao_bd = basedados.criar_conexao("notas.bd")
    basedados.executar_sql(ligacao_bd,sql,parametros)
    #redirecionar para a pagina de listar alunos
    return redirect("/aluno/listar")

def aluno_editar():
    #nprocesso
    nprocesso = request.form.get("nprocesso")
    #consulta à bd para recolher os dados aluno selecionado
    sql = "SELECT * FROM Alunos WHERE nprocesso=?"
    parametros=(nprocesso,)
    #executar a consulta
    ligacao_bd = basedados.criar_conexao("notas.bd")
    dados =  basedados.consultar_sql(ligacao_bd,sql,parametros)
    return render_template("aluno/editar.html",registo = dados[0])

def aluno_editar_confirmado():
    ligacao_bd = basedados.criar_conexao("notas.bd")
    nprocesso = request.form.get("nprocesso")
    #consulta à bd para recolher os dados aluno selecionado
    sql = "SELECT * FROM Alunos WHERE nprocesso=?"
    parametros=(nprocesso,)
    #executar a consulta
    dados =  basedados.consultar_sql(ligacao_bd,sql,parametros)
    if request.method=="POST":
        #validar os dados
        nome = request.form.get("input_nome")
        if not nome:
            return render_template('aluno/editar.html',registo=dados[0],mensagem="Tem de preencher o campo do nome")
        if len(nome)<3:
            return render_template('aluno/editar.html',registo=dados[0],mensagem="Nome muito pequeno. Deve ter pelo menos 3 letras")
        morada = request.form.get("input_morada")
        cp = request.form.get("input_cp")
        data_nasc = request.form.get("input_data")
        email = request.form.get("input_email")
        nprocesso = request.form.get("nprocesso")
        #TODO: guardar fotografia e fazer mais validações
        #editar o aluno na bd
        sql = "UPDATE Alunos SET nome=?, morada=?, cp=?, data_nasc=?, email=? WHERE nprocesso=?"
        parametros = (nome,morada,cp,data_nasc,email,nprocesso)
        basedados.executar_sql(ligacao_bd,sql,parametros)
        return redirect("/aluno/listar")