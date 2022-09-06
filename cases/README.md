Olá pessoal, tudo bem?

Nessa pasta vai conter todos os meus cases de ingestão de dados, do básico ao avançado, do mais simplificado ao mais detalhado e cheio de operações.

# Guia
**Case 1 - NBA**

[RW NBA SALARY](https://github.com/victorhugodostos/dados/blob/main/cases/ingestao_de_dados/rw/rw_nba_salary.py)
- Nele consta informações desse dataset que usei como fonte do [kaggle](https://www.kaggle.com/datasets/rikdifos/nba-salary-and-statistics-201617).
- Foi desenvolvido de forma ELT (extração, salva, transformação), por ser uma ingestão rw, não contém transformações avançadas e nem tratamentos.
- Essa pipe é mais generica, sendo declarado o database e tabela desejada.
- Feito com fonte `SQL`, linguagem `python` e `pyspark`, salvo em formato `parquet`.
- Essa pipe é mais simples, sem conexões com schedule do `Airflow` e conexão com alguma `cloud`.
