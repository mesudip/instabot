host = "localhost"
port = 3306
uname = 'root'
passwd = ''
dbname = 'experiment'
table_name = 'python'
columns = {
    'uname': "username",
    'pwd': 'password'
}

lasterror = ''


def verify(name, pwd):
    global host, port, uname, passwd, dbname, table_name, columns, lasterror
    return True
    # try:
    #     connection = connector.connect(host=host, port=port, passwd=passwd, user=uname, db=dbname)
    #     cursor = connection.cursor()
    #     query = "SELECT username,password FROM `" + table_name + '`' + 'where ' + columns['uname'] + '=%s and ' + \
    #             columns['pwd'] + '=%s'
    #     print(query)
    #     cursor.execute(query, (name, pwd))
    #     name = ''
    #     password = ''
    #     for name, password in cursor:
    #         break;
    #     if name == '' or password == '':
    #         lasterror = ("Can't find registered user",)
    #     else:
    #         return True;
    # except Exception as e:
    #     lasterror = ("Exception ", *e.args)
    #     return False
