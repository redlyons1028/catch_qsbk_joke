# -*- coding: utf-8 -*-

import sys
import cymysql
import pyodbc


class mysqlDB:
    '''操作MySQL的类'''

    def __init__(self, host, user, password, db, port, charset='utf8'):
        '''
        功能：初始化配置信息
        host：      数据服务器
        db：        数据库
        port：      数据库连接端口
        user：      登录名
        password：  登录密码
        charset:    字符编码
        '''
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.port = port
        self.chartset = charset

    def _getConnect(self):
        '''
        功能: 利用配置信息连接MySQL
        '''
        try:
            self.conn = cymysql.connect(host=self.host,
                                        user=self.user,
                                        passwd=self.password,
                                        db=self.db,
                                        port=self.port,
                                        charset=self.chartset)
            cur = self.conn.cursor()
        except Exception, ex:
            print 'MySQL connecting error,reason is:' + str(ex[1])
            sys.exit()
        return cur

    def ExecQuery(self, sql):
        '''
        功能：执行查询语句，返回结果集
        sql：要执行的SQL语句
        '''
        cur = self._getConnect()
        try:
            cur.execute(sql)
            rows = cur.fetchall()
        except pyodbc.Error, ex:
            print 'MySQL.Error :%s \ns' % (str(ex[0]), str(ex[1]))
            sys.exit()
        cur.close()
        self.conn.close()
        return rows

    def ExecNoQuery(self, sql):
        '''
        功能：执行查询语句，如Create,Insert,Delete,update,drop等。
        sql：要执行的SQL语句
        '''
        cur = self._getConnect()
        try:
            cur.execute(sql)
            self.conn.commit()
        except pyodbc.Error, ex:
            print 'MySQL.Error :%s %s' % (str(ex[0]), str(ex[1]))
            sys.exit()
        cur.close()
        self.conn.close()


def testMysql():
    '''
    功能：Mysql测试函数
    '''
    mysql = mysqlDB('127.0.0.1', 'root', 'xxx722123', 'test', 3306)
    sql = r'select * from newcq limit 0,10;'
    rows = mysql.ExecQuery(sql)
    for row in rows:
        print row[0], row[1], row[2], row[3]
    # InsertSQL = u'''insert into city
    #               values(2, '10002','tiananmen','10001'),
    #               (3, '40001','changsha','40000');'''
    #
    # mysql.ExecNoQuery(InsertSQL)
