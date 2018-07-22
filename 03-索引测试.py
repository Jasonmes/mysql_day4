# import pymysql
#
#
# def main():
#     try:
#         conn = pymysql.connect(host='localhost',
#                                user='root',
#                                password='ZHISHAO8@gezifu',
#                                port=3306,
#                                database='JingDong',
#                                charset='utf8')
#         # 开启事务
#         print('--------')
#         conn.begin()
#         cs1 = conn.cursor()
#         # 执行事务， 原子性
#         for i in range(1000):
#             sql = "insert into t_index values('he-%d')" % i;
#             cs1.execute(sql)
#         # 提交事务
#         conn.commit()
#     except Exception as e:
#         print("出现异常", e)
#         # 回滚
#         conn.rollback()
#     finally:
#         cs1.close()
#         conn.close()
#
#
# if __name__ == '__main__':
#     main()

# 第一遍
# import pymysql
#
#
# def Index():
#     try:
#         connected = pymysql.connect(database='JingDong', host='localhost', port=3306, password='ZHISHAO8@gezifu',
#                                     user='root', charset='utf8')
#
#         # 开启事务
#         connected.begin()
#         cur = connected.cursor()
#         # 执行事务，原子性
#         for i in range(1000):
#             cur.execute("insert into t_index values('haaa-%d')" % i);
#         connected.commit()
#     except Exception as e:
#         print('失败', e)
#         connected.rollback()
#     finally:
#         cur.close()
#         connected.close()
#
#
# if __name__ == "__main__":
#     Index()

# 第二遍
# import pymysql
#
#
# def Index():
#     try:
#         conect = pymysql.connect(database='JingDong', user='root', password='ZHISHAOgezifu', port=3306,
#                                  charset='utf8')
#         conect.begin()
#
#         cur = conect.cursor()
#         for i in range(100):
#             cur.execute("insert into t_index value('hhhhhaaaa--%d')" % i)
#         conect.commit()
#     except Exception as e:
#         print('失败', e)
#         conect.rollback()
#     finally:
#         cur.close()
#         conect.close()
#
#
# Index()