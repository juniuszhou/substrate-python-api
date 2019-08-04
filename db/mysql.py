import pymysql

# 打开数据库连接
db = pymysql.connect(host='192.168.2.158', port=3306,
                     user='root', passwd='12345678', db='mysql', charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print('version is {}'.format(data))

# 关闭数据库连接
db.close()

