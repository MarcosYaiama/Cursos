<?php

    function soma($numero){
        $soma = 0;
        for($i = 0; $i < sizeof($numero); $i++){
            $soma += $numero[$i];
        }
        return  $soma;
    }

    $somatorio = soma(array(30, 20, 40)); 
    echo $somatorio;
?>