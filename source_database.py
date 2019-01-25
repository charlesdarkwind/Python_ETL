# ! USED TO FEED THE 'SOURCE' DB !
from mod_createDBConnection import connect


def create_table():
    # Create connection
    conn = connect('ETL_source', 'localhost', 'root', '')
    cursor = conn.cursor()

    # Create table structure
    src_schema_sql = open('sql/src_schema.sql')
    cursor.execute(src_schema_sql.read())
    conn.commit()

    # Open exercice sql file and grab all the 'insert into' lines
    with open('datasets/client_DATA.sql') as f:
        insert_commands = f.read().splitlines()[8:]

    # Exec inserts
    for line in insert_commands:
        cursor.execute(line)

    conn.commit()
    src_schema_sql.close()
    conn.close()