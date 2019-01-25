import pymysql


def connect(db_name, host, user, password):
    if any(type(t) is not str for t in [db_name, host, user, password]):
        raise ValueError('Please provide valid string values for db_name, host, user and password.')

    return pymysql.connect(host=host,
                           user=user,
                           password=password,
                           db=db_name,
                           cursorclass=pymysql.cursors.DictCursor)
