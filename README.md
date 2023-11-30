
<p align="center">
<img>![HIVE DEV png (2)](https://github.com/LeoCorleone/tcc_senai/assets/99774912/36b88e29-ba1d-40ea-a3fc-9452dda55e0c)
</p>

<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# Índice 
* [Descrição do Projeto](#-Descrição-do-projeto)
* [Estrutura do Projeto](#Estrutura-do-projeto)
* [Desenvolvedores](#desenvolvedores-do-site)

<h1 align="center"> Hight Fashion </h1>

# Descrição do projeto
O projeto tem como objetivo desenvolver um site que funcionará como catálogo online de peças para a empresa Sãojoanense de vestuário High Fashion.O Catálogo contará com administradores para reposição, manutenção e moderação das imagens a serem armazenadas e atualizadas, assim como a moderação em cada comentário sobre as peças à disposição.


`Breve história da empresa:`A High Fashion Confecções Ltda, foi fundada em São João Nepomuceno, em 25 de fevereiro de 1972, pelos visionários Gianni Givenchy e Yves Dior. Desde o início, a empresa tem se dedicado à criação de moda adulta feminina, com um compromisso inabalável de combinar praticidade, conforto e beleza cotidiana em cada peça.

# Estrutura do projeto
Após baixar o sistema em sua máquina, execute:

1.1 Na pasta "catálogo" instale o Django

```python 
pip install django
```
1.2 Ainda na pasta "catálogo" instale o MYSQL

```python
pip install mysql-connector-python
```

```python
pip install mysqlclient
```
2. Após a execução dos comandos a cima, é hora de subir a estrutura para o Banco de Dados. Para isso execute:

```python
python manage.py makemigrations
```

3. Agora imposte os arquivos para o Banco de Dados:

```python
python manage.py loaddata roupas.json
```

4. Crie as tabelas a serem utilizadas através do comando:

```python
python manage.py migrate
```

Aproveite o Sistema!





 






