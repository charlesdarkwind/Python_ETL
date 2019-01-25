from mod_createDBConnection import connect
from mod_data import get_csv, get_json, get_table, insert_data

# Create source and destination database connections
dest_conn = connect('jasminTP1', 'localhost', 'root', '')
src_conn = connect('etl_source', 'localhost', 'root', '')
dest_cursor = dest_conn.cursor()

# Create the destination table
dest_schema_sql = open('sql/dest_schema.sql')
dest_cursor.execute(dest_schema_sql.read())
dest_conn.commit()

# Get data
csv_data = get_csv('datasets/week_cust.csv')
json_data = get_json('datasets/cust_data.json')
table_data = get_table(src_conn, 'client_DATA')

# Insert data
insert_data(dest_conn, 'destination', csv_data+json_data+table_data)

dest_schema_sql.close()
dest_conn.close()
src_conn.close()