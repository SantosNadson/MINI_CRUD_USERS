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
    columns = [description[0] for description in cursor.description]
    result = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return result

def insert_data(name: str, age: int):
    query = f"""
    INSERT INTO users (nome,idade)
    values('{name}','{age}')
    """
    cursor.execute(query)
    cursor.commit()

def delete_data(id: int):
    query = f"""
    DELETE FROM users
    WHERE id = {id}
    """

    print(f"\n ETAPA INICIADA: DELETE, ID: {id}")
    cursor.execute(query)
    cursor.commit()
    print(f"\n ETAPA FINALIZADA: DELETE, ID: {id}")

def update_data(user_id: int, name: str, age: int):
    query = f"""
    UPDATE users
    SET nome = '{name}', idade = {age}
    WHERE id = {user_id}
    """

    print(f"\n ETAPA INICIADA: UPDATE, ID: {id}")
    cursor.execute(query)
    cursor.commit()
    print(f"\n ETAPA FINALIZADA: UPDATE, ID: {id}")
