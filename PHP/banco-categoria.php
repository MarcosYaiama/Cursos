<?php
    include("conecta.php");

    function listaCategorias($conexao){
        $categorias = array();
        $resultado = mysqli_query($conexao, "select * from categorias");
        while($lista = mysqli_fetch_assoc($resultado)){
            array_push($categorias, $lista);
        } 
        return $categorias;
    }

    function buscaCategoria($conexao,  $id){
        $categoria = mysqli_query($conexao, "SELECT * FROM `categorias` WHERE id = {$id}");
        return mysqli_fetch_assoc($categoria);        
    }