import pyodbc

conn_str = (
        r'DRIVER={ODBC Driver 17 for SQL Server};'
        r'SERVER=localhost\SQLEXPRESS01;'
        r'DATABASE=NSS_ERP;'
        r'Trusted_Connection=yes;'
    )
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def get_data():
    query = """
    SELECT
    *
    FROM users
    ORDER BY id
    """

    cursor.execute(query)
    colunas = [description[0] for description in cursor.description]
    resultado = [dict(zip(colunas, row)) for row in cursor.fetchall()]
    return resultado

def insert_data(nome: str,idade: int):
    query = f"""
    INSERT INTO users (nome,idade)
    values('{nome}','{idade}')
    """
    cursor.execute(query)
    cursor.commit()

def delete_data(id: int):
    query = f"""
    DELETE FROM users
    WHERE 1=1
        AND id = {id}
    """

    print(f"\n ETAPA INICIADA: DELETE, ID: {id}")
    cursor.execute(query)
    cursor.commit()
    print(f"\n ETAPA FINALIZADA: DELETE, ID: {id}")

def update_data(user_id: int, nome: str, idade: int):
    query = f"""
    UPDATE users
    SET nome = '{nome}', idade = {idade}
    WHERE 1=1
        AND id = {user_id}
    """

    print(f"\n ETAPA INICIADA: UPDATE, ID: {id}")
    print('\n DEBUG', query)
    cursor.execute(query)
    cursor.commit()
    print(f"\n ETAPA FINALIZADA: UPDATE, ID: {id}")
    



