<?php
    include("cabecalho.php");
    include("conecta.php");
    include("banco-produto.php"); 
    
    $id = $_POST['id'];
    $removido = false;
    if(removeProduto($conexao, $id)){
        $removido = true;
    }
    header("Location: produto-lista.php?removido={$removido}");
    die();

    