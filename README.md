<div class="text-aling: center"> 
 
 <img src="https://github.com/LeoCorleone/tcc_senai/assets/99774912/750e0128-64f0-40c8-8085-ae8b7a135c8e " alt="![HIVE DEV png (2)]">
 
 </div>


<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/>
</p>

# Índice 
* [Descrição do Projeto](#-Descrição-do-projeto)
* [Estrutura do Projeto](#Estrutura-do-projeto)
* [Desenvolvedores do Projeto](#Desenvolvedores-do-projeto)
* [Licença](#licença)

# Descrição do projeto
O projeto tem como objetivo desenvolver um site que funcionará como catálogo online de peças para a empresa Sãojoanense de vestuário High Fashion.O Catálogo contará com administradores para reposição, manutenção e moderação das imagens a serem armazenadas e atualizadas, assim como a moderação em cada comentário sobre as peças à disposição.


`Hight Fashion:`A High Fashion Confecções Ltda, foi fundada em São João Nepomuceno, em 25 de fevereiro de 1972, pelos visionários Gianni Givenchy e Yves Dior. Desde o início, a empresa tem se dedicado à criação de moda adulta feminina, com um compromisso inabalável de combinar praticidade, conforto e beleza cotidiana em cada peça.

# Estrutura do projeto
Após baixar o sistema em sua máquina, execute:

1. Na pasta "catálogo" instale o MYSQL

```python
pip install mysqlclient
```

2. Após a execução dos comandos a cima, é hora de subir a estrutura para o Banco de Dados. Para isso execute:

```python
python manage.py makemigrations
```

3. Crie as tabelas a serem utilizadas através do comando:

```python
python manage.py migrate
```

4. Agora imposte os arquivos para o Banco de Dados:

```python
python manage.py loaddata roupas.json
```

5. Inicie o projeto:

```python
python manage.py runserver
```

Aproveite o Sistema!

# Desenvolvedores do projeto

Alice Fritz <br>
Daniel Magalhães <br>
Guilherme Assis <br>
Kauã Souza <br>
Leonardo Cunha <br>
Rebeca Velasco <br>

# Licença
[Educational Community v2.0 ECL-2.0]()

Copyright :copyright: 2023 





 






