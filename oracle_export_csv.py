import oracle_connect
from cx_Oracle import Cursor
import csv

SELECT_SIZE = 5000
FILE_NAME_QUERY_TABLE = 'querytable.csv'

def export_csv(data: list) -> None:
    """ export list of lists to csv

    Args:
        data (list): list of lists
    """
    with open(FILE_NAME_QUERY_TABLE, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def processing(query: Cursor) -> list:
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


connection = oracle_connect.connection()
cursor = connection.cursor()
cursor.arraysize = SELECT_SIZE
query = cursor.execute('SELECT * FROM TEST ORDER BY ID')

list_cropped_id = processing(query)
new_list_add_data = []
if len(list_cropped_id) > 0:
    for row_list in list_cropped_id:
        print(row_list)
        query = cursor.execute(f"SELECT * FROM TEST2 WHERE ID2='{str(row_list[0])}'")
        for row in query:
            print(row[1:])
            new_list_add_data.append(row_list+list(row[1:]))

export_csv(new_list_add_data)

cursor.close()
connection.close()
