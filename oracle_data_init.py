import oracle_connect

init_data = [('AAA-BBB-CCC', 'text', 'text'),
             ('AAA-BBB-EEE', 'text', 'text'),
             ('AAA-BBB-DDD', 'text', 'text')]

init_data2 = [('AAABBBCCC', 'text', 'text', 'text'),
              ('AAABBBEEE', 'text', 'text', 'text'),
              ('AAABBBDDD', 'text', 'text', 'text')]

connection = oracle_connect.connection()
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
