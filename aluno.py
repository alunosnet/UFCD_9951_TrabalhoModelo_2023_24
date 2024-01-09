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
