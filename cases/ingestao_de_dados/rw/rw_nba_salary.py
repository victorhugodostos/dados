from pyspark.sql import SparkSession
import logging
import sqlite3

# ingestão de dados fonte SQL, sendo a camada rw (bruta) de forma generica, podendo ser alterado os valores

def read_database(database, table):
    logging.info(f"Iniciando conexão no banco de dados {database}")
    conn = sqlite3.connect(database)
    logging.info(f"Conectado!")
    cursor = conn.cursor()
    logging.info(f"Obtendo dados do banco {database} e tabela {table}")
    return cursor.execute(f"SELECT * FROM {table}")


def save_dataframe(df, save_path):
    logging.info(f"Salvando dataframe mode overwrite, no path {save_path}")
    df.write.format("parquet").option("overwriteSchema", "true")\
        .mode("overwrite").save(save_path)
    logging.info(f"Salvo com sucesso!")


def main():
    logging.info("Iniciando sessão spark")
    spark = SparkSession.builder.appName("spark").getOrCreate()

    df = read_database("dados/database/nba_salary.sqlite", "NBA_season1718_salary")
    df = spark.createDataFrame(df)

    save_dataframe(df, "dados/datalake/")

    spark.stop()
    logging.info("Finalizando sessão spark")


if __name__ == "__main__":
    main()
