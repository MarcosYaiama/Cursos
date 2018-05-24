#!/bin/bash

echo Fazendo download do TomCat
wget http://mirror.nbtelecom.com.br/apache/tomcat/tomcat-8/v8.5.31/bin/apache-tomcat-8.5.31.tar.gz

echo Descompactado
tar -xvf apache-tomcat-8.5.31.tar.gz


echo Removendo a antiga pasta da home
rm -rf ~/apache-tomcat-8.5.31

echo Criando pasta vazia na home
mkdir ~/apache-tomcat-8.5.31

echo Movendo conteudo da pasta descompactada para a pasta criada na home
mv ./apache-tomcat-8.5.31/* ~/apache-tomcat-8.5.31/

echo Apagando a pasta vazia 
rm -rf apache-tomcat-8.5.31/

echo Criando a pasta MyApp
mkdir ~/apache-tomcat-8.5.31/webapps/MyApp

echo Copiando o site para dentro do diretório MyApp
cp -r ./topcasafina/* ~/apache-tomcat-8.5.31/webapps/MyApp

echo Subindo aplicação
~/apache-tomcat-8.5.31/bin/startup.sh

echo Apagando o arquivo compactado
rm -r apache-tomcat-8.5.31.tar.gz

echo APP RODANDO NO IP:
hostname -I

echo PORTA:
echo :8080/MyApp
