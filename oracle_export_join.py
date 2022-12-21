import cx_Oracle
import csv

SELECT_SIZE = 5000
DELIMITER_CSV = ';'

IP: str = "localhost"
PORT: int = 1521
SID: str = "ORCL"
USER: str = "system"
PWD: str = "oracle"


def connection():
    dsn_tns = cx_Oracle.makedsn(IP, PORT, service_name=SID)
    connection = cx_Oracle.connect(USER, PWD, dsn_tns, encoding="UTF-8")
    print(f"oracle database {str(connection.version)}")
    return connection


def import_csv(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as read_obj:
        csv_reader = csv.reader(read_obj)
        list_of_csv = list(csv_reader)
    return list_of_csv


def export_csv(data: list, filename: str) -> None:
    """export list of lists to csv

    Args:
        data (list): list of lists
        filename (str): name file export
    """
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter = DELIMITER_CSV)
        writer.writerows(data)


def processing(query: cx_Oracle.Cursor) -> list:
    """remove '-' in ID

    Args:
        query (_type_): cursor data

    Returns:
        list: list of lists
    """
    query_cropped_id = []
    for row in query:
        row = list(row)
        row[0] = row[0].replace("-", "")
        query_cropped_id.append(row)
    return query_cropped_id


query_data = import_csv("querytable.csv")
connection = connection()
cursor = connection.cursor()
# # cursor.arraysize = SELECT_SIZE

new_list_add_data = []
if len(query_data) > 0:
    for row_list in query_data:
        query = cursor.execute(f"SELECT * FROM TEST2 WHERE ID2='{str(row_list[0])}'")
        for row in query:
            # row[1:] - remove first column ID in query 
            new_list_add_data.append(row_list + list(row[1:]))

export_csv(new_list_add_data, "result.csv")

cursor.close()
connection.close()
