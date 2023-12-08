<p align="center">
  <img src="https://github.com/LeoCorleone/tcc_senai/assets/99774912/750e0128-64f0-40c8-8085-ae8b7a135c8e" alt="HIVE DEV png (2)">
</p>


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
# Versões dos programas utilizados no projeto

Django 4.2.3 <br>
mysqlclient 2.2.0 <br>
Python 3.11.6<br>

# Estrutura do projeto
Após baixar a pasta compactada em sua máquina ou após de copiar e executar "git clone (link do repositório) no terminal", execute:

1. No Terminal execute o comando a seguir:

```python
pip install -r requeriments.txt
```

2. Após a execução do comando acima, nos seu mysql crie um banco de dados chamado "catalago"

3. Após a criação do banco , execute em seu terminal o seguinte comando:

```python
python manage.py migrate
```
4. Após dar o comando migrate , execute:

```python
python manage.py createsuperuser
```

5. Agora imposte os arquivos para o Banco de Dados:

```python
python manage.py loaddata roupas.json
```

6. Inicie o projeto:

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





 






