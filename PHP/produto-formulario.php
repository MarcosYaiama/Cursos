<?php
    include("cabecalho.php");
    include("conecta.php");
    include("banco-produto.php");
    include("banco-categoria.php");
    $categorias = listaCategorias($conexao);
    $alterar = array_key_exists("alterar", $_POST) ?true : false;
    $usado = "";
    $categoria_nome = "";
    if($alterar){
        
        $dadosBD = buscaProduto($conexao, $_POST["id"]);
        $categoria_nome = buscaCategoria($conexao, $dadosBD["categoria_id"]);
        $usado = $dadosBD["usado"] ? "checked='checked'": "";
    }
    $acao = $alterar ? "altera-produto.php" : "adiciona-produto.php";
    $nome_submit = $alterar ? "Alterar" : "Cadastrar";
    $nomeForm = $alterar ? "Alterar Produto": "Produto Formulário";
    $nome = $alterar ? $dadosBD["nome"] : "";
    $preco = $alterar ? $dadosBD["preco"] : "";
    $descricao = $alterar ? $dadosBD["descricao"] : "";

    ?>
    <h1><?=$nomeForm?></h1>
    <form action="<?=$acao?>" method="post">
        <table class="table">
        
        <tr>
            <td>Nome:</td>
            <td><input class="form-control" type="text" name="nome" value="<?=$nome?>"></td>
        </tr>
        <tr>   
            <td>Preço:</td>
            <td><input class="form-control" type="number" name="preco" value=<?=$preco?>></td>
        </tr>
        <tr>   
            <td>Descrição: </td>
            <td><textarea class="form-control" name="descricao"><?=$descricao?></textarea><td>
        </tr>
        <?php 
            if($alterar){
        ?>
            <input type="hidden" name="id" value=<?=$_POST["id"]?>>
            <?php } ?>
        <tr>
            <td><input type="checkbox" name="usado" <?=$usado?>>Usado</td>
        </tr>
        <tr>
            <td>Categoria:</td>
            <td>
            <select name="categoria_id" class="form-control">
                <?php
                foreach($categorias as $categoria):
                    $selecao = $categoria_nome == $categoria ? "selected='selected'" : ""; 
                ?>
                    <option value=<?=$categoria['id']?> <?=$selecao?>><?=$categoria['nome'];?></option>
                <?php
                endforeach
                ?>
            </td>
            </select>
        </tr>

        <tr>
            <td>
                <button class="btn btn-primary" type="submit" value=<?=$nome_submit?>><?=$nome_submit?></button>
            </td>
        </tr>
    </form>
<?php include("rodape.php");?>