import cx_Oracle
import csv

SELECT_SIZE = 5000

IP: str = 'localhost'
PORT: int = 1521
SID: str = 'ORCL'
USER: str = 'system'
PWD: str = 'oracle'
    
def connection():
    dsn_tns = cx_Oracle.makedsn(IP, PORT, service_name=SID)
    connection = cx_Oracle.connect(USER, PWD, dsn_tns, encoding="UTF-8")
    print(f"oracle database {str(connection.version)}")
    return connection

def export_csv(data: list, filename: str) -> None:
    """ export list of lists to csv

    Args:
        data (list): list of lists
    """
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def processing(query: cx_Oracle.Cursor) -> list:
    """ remove '-' in ID

    Args:
        query (_type_): cursor data

    Returns:
        list: list of lists
    """
    query_cropped_id = []
    for row in query:
        row = list(row)
        row[0] = row[0].replace('-', '')
        query_cropped_id.append(row)
    return query_cropped_id


connection = connection()
cursor = connection.cursor()
# cursor.arraysize = SELECT_SIZE
query_filter_sql: str = 'SELECT * FROM TEST ORDER BY ID'
query_filter = cursor.execute(query_filter_sql)
export_csv(query_filter, 'raw_data.csv')
query_filter = cursor.execute(query_filter_sql)
list_cropped_id = processing(query_filter)
export_csv(list_cropped_id, 'querytable.csv')


cursor.close()
connection.close()
