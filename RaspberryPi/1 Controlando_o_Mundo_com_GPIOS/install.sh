echo #Atualizando...
sudo apt-get update

echo Baixando apache2 ...
sudo apt-get install apache2

echo intalando PHP e seu pacote de comunicacao com Apache
sudo apt-get install php5 libapache2-mod-php5

echo verifique seu endereco IP no navegador
hostname -I
