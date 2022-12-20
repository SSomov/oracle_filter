## install client Oracle in Ubuntu
`wget https://yum.oracle.com/repo/OracleLinux/OL7/oracle/instantclient/x86_64/getPackage/oracle-instantclient19.17-basic-19.17.0.0.0-1.x86_64.rpm`

`sudo apt install alien libaio1`

`sudo alien -i oracle-instantclient19.17-basic-19.17.0.0.0-1.x86_64.rpm`

default oracle instance

login `SYSTEM`

pass `oracle`

## file assignment

oracle_connect - init connect database

oracle_data_init - create fakedata

oracle_export_query - save csv query table