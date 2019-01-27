import pymysql


def connect(db_name, host, user, password):
    """Connect to a MySQL database.

    :param db_name: The database connection object
    :type db_name: str
    :param host: The name of the destination table
    :type host: str
    :param user: A list of lists containing the data
    :type user: str
    :param password: A list of lists containing the data
    :type password: str
    :return: Connection object
    """
    if any(type(t) is not str for t in [db_name, host, user, password]):
        raise ValueError('Please provide valid string values for db_name, host, user and password.')

    return pymysql.connect(host=host,
                           user=user,
                           password=password,
                           db=db_name,
                           cursorclass=pymysql.cursors.DictCursor)
