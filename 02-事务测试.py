import pymysql


def main():
    try:
        conn = pymysql.connect(host='localhost', user='root', password='ZHISHAO8@gezifu', port=3306, database='JingDong', charset='utf8')
        conn.begin()  # 开启事务
        cs1 = conn.cursor()
        # 执行事务， 原子性
        cs1.execute("update goods set price=price-1000 where id=44")

        cs1.execute("update goods set price=price-200 where id=40")

        conn.commit()  # 提交事务
    except Exception as e:
        print("出现异常", e)
        conn.rollback()  #回滚
    finally:
        cs1.close()
        conn.close()

    # conn.commit()


if __name__ == '__main__':
    main()