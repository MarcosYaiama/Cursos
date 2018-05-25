cd ~
cd ../..
cd var/www/html/

echo Deletando pasta index colocada
sudo rm index.php
echo Alterando o nome da original
sudo mv index.old index.php

