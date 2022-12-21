import cx_Oracle

init_data = [('AAA-BBB-CCC', 'text', 'text'),
             ('AAA-BBB-EEE', 'text', 'text'),
             ('AAA-BBB-DDD', 'text', 'text')]

init_data2 = [('AAABBBCCC', 'text', 'text', 'text'),
              ('AAABBBDDD', 'text', 'text', 'text')]

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

connection = connection()
cursor = connection.cursor()
# create table
cursor.execute("DROP TABLE TEST")
cursor.execute("DROP TABLE TEST2")
connection.commit()
cursor.execute(
    "CREATE TABLE TEST ( ID VARCHAR2(15) NOT NULL, PARAMETR_1 VARCHAR2(100) NOT NULL, PARAMETR_2 VARCHAR2(100) NOT NULL )")
cursor.executemany("INSERT INTO TEST values (:1, :2, :3)", init_data)
cursor.execute(
    "CREATE TABLE TEST2 ( ID2 VARCHAR2(15) NOT NULL, PARAMETR_1 VARCHAR2(100) NOT NULL, PARAMETR_2 VARCHAR2(100) NOT NULL, PARAMETR_3 VARCHAR2(100) NOT NULL )")
cursor.executemany("INSERT INTO TEST2 values (:1, :2, :3, :4)", init_data2)
connection.commit()
# print(cursor.execute("SELECT * FROM ALL_TABLES"))
cursor.close()
connection.close()
