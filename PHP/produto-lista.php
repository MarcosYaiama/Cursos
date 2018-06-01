<?php 
    include("cabecalho.php");
    include("conecta.php");
    include("banco-produto.php");

if(array_key_exists("removido", $_GET) && $_GET["removido"] == true){
?>
    <p class="alert-success">Produto apagado com sucesso!</p>
<?php
}if(array_key_exists("alterado", $_GET) && $_GET["alterado"] == true){
?>
    <p class="alert-success">Produto alterado com sucesso!</p>
<?php
}
?>
<table class="table table-striped table-bordered">
    <?php
        $lista = listaProdutos($conexao);
        foreach ($lista as $produto) :
            
        ?>    
        <tr>             
            <td><?=$produto['id'];?></td>
            <td><?=$produto['nome'];?></td>
            <td><?=$produto['preco'];?></td>
            <td><?=substr($produto['descricao'], 0, 40);?></td>
            <td><?=$produto['categoria_nome'];?></td>
            
            
            
            <td>
                <form action="remove-produto.php" method="post">
                    <input type="hidden" name="id" value="<?=$produto["id"];?>">
                    <button class="btn btn-danger">remover</button>
                    
                </form>
            </td>
            <td>
                <form action="produto-formulario.php" method="post">
                    <input type="hidden" name="id" value="<?=$produto["id"];?>">
                    <input type="hidden" name="alterar" value="true">
                    <button class="btn btn-success">alterar</button>
                </form>
            </td>
        </tr>
        <?php
        endforeach
    ?>
</table>

<?php include("rodape.php");?>