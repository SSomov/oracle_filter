import cx_Oracle
    
def connection():
    ip: str = 'localhost'
    port: int = 1521
    SID: str = 'ORCL'
    usr: str = 'system'
    pwd: str = 'oracle'

    dsn_tns = cx_Oracle.makedsn(ip, port, service_name=SID)
    connection = cx_Oracle.connect(usr, pwd, dsn_tns, encoding="UTF-8")
    print(f"oracle database {str(connection.version)}")
    return connection
