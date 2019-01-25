import csv
import json
from mod_helpers import normalize_gender


def insert_data(conn, table_name, data):
    """Insert structured data in table.

    :param conn: The database connection object
    :param table_name: The name of the destination table
    :type table_name: str
    :param data: A list of of lists containing the data
    :type data: list
    """
    cursor = conn.cursor()
    for line in data:
        insert_command = '''insert into {0} (source_id, source_name, first_name, last_name, email, gender, ville)
                values ({1}, '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')'''.format(table_name, *line)
        cursor.execute(insert_command)
    conn.commit()


def get_csv(csv_path):
    """Returns insertable data from extracted CSV data.

    :param csv_path: A CSV file path string
    :type csv_path: str
    :returns: A list of of lists containing the data
    """
    with open(csv_path) as f:
        data = list(csv.reader(f))[1:]
        src_name = csv_path.split('/')[-1]
    res = []
    for line in data:
        gender = normalize_gender(line[4])
        ville = 'unknown' if line[5] == '' else line[5]
        res.append([line[0], src_name, line[1], line[2], line[3], gender, ville])
    return res


def get_json(json_path):
    """Returns insertable data from extracted JSON data.

    :param json_path: A JSON file path string
    :type json_path: str
    :returns: A list of of lists containing the data
    """
    with open(json_path) as f:
        data = json.load(f)
        src_name = json_path.split('/')[-1]
    res = []
    for line in data:
        gender = 'unknown' if 'gender' not in line else normalize_gender(line['gender'])
        res.append([
            line['id'],
            src_name,
            line['first_name'],
            line['last_name'],
            line['email'],
            gender,
            line['ville']
        ])
    return res


def get_table(src_conn, src_table_name):
    """Returns insertable data from extracted MySQL table data.

    :param src_conn: A MySQL source database connection
    :param src_table_name: The source table name
    :type src_table_name: str
    :returns: A list of of lists containing the data
    """
    src_cursor = src_conn.cursor()
    src_cursor.execute('select * from {0}'.format(src_table_name))
    lines = src_cursor.fetchall()
    res = []
    for line in lines:
        res.append([
            line['id'],
            src_table_name,
            line['first_name'],
            line['last_name'],
            line['email'],
            line['gender'],
            line['ville']
        ])
    return res
