<?php 
    include("cabecalho.php");
    include("conecta.php");
    include("banco-produto.php");
    
    $id = $_POST["id"];
    $nome = $_POST["nome"];
    $preco = $_POST["preco"];
    $descricao = $_POST["descricao"];
    $categoria_id = $_POST["categoria_id"];
    
    $usado = array_key_exists("usado" ,$_POST)? 1: 0;
    
    $alterado = false;
    if(alteraProduto($conexao, $id, $nome, $preco, $descricao, $categoria_id, $usado)){
        $alterado = true;
    }else{
        $msg = mysqli_error($conexao);
    }
    header("Location: produto-lista.php?alterado={$alterado}");
    die();