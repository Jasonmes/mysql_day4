"""
******************************
对商品类型表管理
1. 所有类型
2. 查询类型
3. 新增类型
4. 删除类型
5. 更新类型
0. 退出选择
******************************
"""
import pymysql


class JD(object):
    def __init__(self):
        # 创建连接
        self.conn = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', port=3306, database='JingDong', charset='utf8')
        # 获取游标
        self.cs1 = self.conn.cursor()

    def __del__(self):

        # 释放资源
        self.cs1.close()
        self.conn.close()

    def show_cates(self):
        """查询所有类别"""

        # 执行sql
        sql = "select * from goods_cates"
        self.cs1.execute(sql)

        # 处理结果
        for item in self.cs1.fetchall():
            print(item)

    def query_cates(self):
        """查询指定类别"""

        cate_key = input("请输入要查询的类别名: ")
        # 执行sql
        sql = "select * from goods_cates WHERE name rlike %s"
        self.cs1.execute(sql, [cate_key])

        # 处理结果
        for item in self.cs1.fetchall():
            print(item)

    def add_cates(self):
        """新增类别"""

        cate_name = input("请输入要添加的类别名: ")
        # 执行sql
        sql = "insert into goods_cates(name) values(%s)"
        affect_rows = self.cs1.execute(sql, [cate_name])
        print(affect_rows)

        self.conn.commit()  # 增删改时，记得提交数据，持久化数据

        # 处理结果
        if self.cs1.rowcount == 1:
            print("添加成功")
        else:
            print("添加失败")

    def del_cates(self):
        """删除指定类别"""

        cate_id = input("请输入要删除的类别id: ")
        # 执行sql
        sql = "delete from goods_cates WHERE id=%s"
        affect_rows = self.cs1.execute(sql, [cate_id])
        print(affect_rows)

        self.conn.commit()  # 增删改时，记得提交数据，持久化数据

        # 处理结果
        if self.cs1.rowcount == 1:
            print("删除成功")
        else:
            print("删除失败")

    def update_cates(self):
        """更新类别"""

        cate_id = input("请输入要更新的类别id: ")
        cate_name = input("请输入要新的类别名称: ")
        # 执行sql
        sql = "update  goods_cates set name=%s WHERE id=%s"
        affect_rows = self.cs1.execute(sql, [cate_name, cate_id])
        print(affect_rows)

        self.conn.commit()  # 增删改时，记得提交数据，持久化数据

        # 处理结果
        if self.cs1.rowcount == 1:
            print("更新成功")
        else:
            print("更新失败")

    def startup(self):
        # 1. 显示菜单功能界面
        while True:
            opt = JD.show_menu()

            # 3. 依据用户选择，做相应的业务处理
            if opt == "1":  # 查询所有类别
                self.show_cates()
            elif opt == "2":  # 查询指定类别
                self.query_cates()
            elif opt == "3":  # 新增类别
                self.add_cates()
            elif opt == "4":  # 删除类别
                self.del_cates()
            elif opt == "5":  # 更新类别
                self.update_cates()
            elif opt == "0":  # 退出
                break
            else:
                print("选择有误，请重新输入")

    # 方法抽取： ctrl+alt+m
    @staticmethod  # 静态方法
    def show_menu():
        """显示功能菜单"""
        print("*" * 30)
        print("1. 所有类型")
        print("2. 查询类型")
        print("3. 新增类型")
        print("4. 删除类型")
        print("5. 更新类型")
        print("0. 退出选择")
        print("*" * 30)
        # 2. 获取用户的功能选择
        opt = input("请输入您的选择:")
        return opt


if __name__ == '__main__':
    # 由类创建对象
    jd = JD()
    jd.startup()
