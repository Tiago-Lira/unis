# Ciclo 4: Calculo do IMC com banco de dados

Esta atividade depende da instalação do SQLAlchemy e foi testada com python 3.10.

### Instalação
É necessário criar um virtualenv para instalar as dependências.

```bash
(venv) ➜  ciclo4 git:(main) pip install -r requirements.txt
```

### Comandos
```bash
(venv) ➜  ciclo4 git:(main) python main.py
usage: main.py [-h] {calcular,listar_resultados} ...

positional arguments:
  {calcular,listar_resultados}

options:
  -h, --help            show this help message and exit
```
### Calculando o IMC

```bash
(venv) ➜  ciclo4 git:(main) python main.py calcular Tiago 171 80
Resultado:
-------------
Nome: Tiago
Altura: 1.71cm
Peso: 80kg
IMC: 27.36
```

### Listando resultados anteriores

```bash
(venv) ➜  ciclo4 git:(main) python main.py listar_resultados
Resultados:
-------------
Nome: Tiago
Altura: 1.71cm
Peso: 80.0kg
IMC: 27.36
-------------
```
