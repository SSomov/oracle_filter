import cx_Oracle
import csv

SELECT_SIZE = 5000
DELIMITER_CSV = ';'

CONNECT_QUERY = {'host': "localhost", 'port': 1521,
                 'sid': "orcl", 'user': "system", 'pwd': "oracle"}
CONNECT_OTHER = [
    {'host': "localhost", 'port': 1521, 'sid': "orcl",
        'user': "system", 'pwd': "oracle"},
    {'host': "localhost", 'port': 1521, 'sid': "orcl", 'user': "system", 'pwd': "oracle"}]


def connection(host: str, port: int, sid: str, user: str, pwd: str):
    """ connect database type - oracle

    Args:
        host (str): _description_
        port (int): _description_
        sid (str): _description_
        user (str): _description_
        pwd (str): _description_

    Returns:
        _type_: class connect oracle
    """
    dsn_tns = cx_Oracle.makedsn(host, port, service_name=sid)
    con = cx_Oracle.connect(user, pwd, dsn_tns, encoding="UTF-8")
    print(f"oracle database {str(con.version)}")
    return con


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
        writer = csv.writer(csvfile, delimiter=DELIMITER_CSV)
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


con_one = connection(**CONNECT_QUERY)
cursor = con_one.cursor()
# cursor.arraysize = SELECT_SIZE
query_filter_sql: str = "SELECT * FROM TEST ORDER BY ID"
query_filter = cursor.execute(query_filter_sql)
export_csv(query_filter, "raw_data.csv")
query_filter = cursor.execute(query_filter_sql)
list_cropped_id = processing(query_filter)
export_csv(list_cropped_id, "querytable.csv")

cursor.close()
con_one.close()

query_data = list_cropped_id

for con_other in CONNECT_OTHER:
    con_other = connection(**con_other)
    cursor = con_other.cursor()
    # # cursor.arraysize = SELECT_SIZE
    new_list_add_data = []
    if len(query_data) > 0:
        for row_list in query_data:
            query_sql = f"SELECT * FROM TEST2 WHERE ID2='{str(row_list[0])}'"
            print(query_sql)
            query = cursor.execute(query_sql)
            query_null = True
            for row in query:
                # row[1:] - remove first column ID in query
                if len(row) > 0:
                    query_null = False
                    new_list_add_data.append(row_list + list(row[1:]))
            if query_null:
                new_list_add_data.append(row_list)
        if len(new_list_add_data) > 0:
            query_data = new_list_add_data
        else:
            print("Неверный запрос или в бд нет данных")
    cursor.close()
    con_other.close()

export_csv(query_data, "result.csv")
