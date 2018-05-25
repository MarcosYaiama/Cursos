cd
cd ../..

cd var/www/html

echo Trocando nome da pasta Index antiga
sudo mv index.php index.old

echo Copiando nosso arquivo index para acionar via php
sudo cp ~/cursos/RaspberryPi/1\ Controlando_o_Mundo_com_GPIOS/index-script-python.php .
#cp ~/cursos/RaspberryPi/1\ Controlando_o_Mundo_com_GPIOS/index-direto-terminal.php .

echo Mudando o nome do arquivo copiado para index.php
sudo mv index-script-python.php index.php
#mv index-direto-terminal.php index.php

echo Verifique se esta no ar no seguinte endereco:
hostname -I
