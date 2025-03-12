import pymysql
from datetime import datetime


def sqlu(se, va):
    conn = pymysql.connect(host='localhost', user='root', password='xogus1125424a!', db='pos', port=3306, charset='utf8')
    with conn:
        with conn.cursor() as cur:
            cur.execute(se, va)
            conn.commit()


def sqls(se, va):
    conn = pymysql.connect(host='localhost', user='root', password='xogus1125424a!', db='pos', port=3306, charset='utf8')
    with conn:
        with conn.cursor() as cur:
            cur.execute(se, va)
            return cur.fetchall()


def sqlsa(se):
    conn = pymysql.connect(host='localhost', user='root', password='xogus1125424a!', db='pos', port=3306, charset='utf8')
    with conn:
        with conn.cursor() as cur:
            cur.execute(se)
            return cur.fetchall()


i = 1
if __name__ == '__main__':
    while (True):
        print('=== 빵집 재고관리 시스템 ===')
        menu = int(input('1> 제품등록\n2> 재고현황\n3> 판매\n4> 마감정산\n'))
        if (menu == 1):
            while (True):
                menu1 = int(input('지점을 선택해주세요(1.서울 2.인천 3.수원 4.용인 5.대구):'))
                print('추가할 빵')
                print('1> 단팥빵')
                print('2> 소보루빵')
                print('3> 크림빵')
                print('4> 피자빵')
                print('5> 식빵')
                print('6> 슈크림빵')
                print('7> 초코머핀')
                print('8> 바게트빵')
                print()
                p_id = int(input())
                if (p_id == 1):
                    b_id = '1001'
                elif (p_id == 2):
                    b_id = '1002'
                elif (p_id == 3):
                    b_id = '1003'
                elif (p_id == 4):
                    b_id = '1004'
                elif (p_id == 5):
                    b_id = '1005'
                elif (p_id == 6):
                    b_id = '1006'
                elif (p_id == 7):
                    b_id = '1007'
                elif (p_id == 8):
                    b_id = '1008'

                if (menu1 == 1):
                    p_id = '101'
                elif (menu1 == 2):
                    p_id = '102'
                elif (menu1 == 3):
                    p_id = '103'
                elif (menu1 == 4):
                    p_id = '104'
                elif (menu1 == 5):
                    p_id = '105'

                val1 = (p_id, b_id)

                sql = ("UPDATE iventory SET i_num=%s WHERE branch_b_id =%s AND breadd_p_id=%s")

                sql1 = ("SELECT i.i_num FROM iventory AS i WHERE i.branch_b_id =%s AND i.breadd_p_id=%s")

                d = sqls(sql1, val1)
                d = [list(d[x]) for x in range(len(d))]
                print("현재 개수:%d" % d[0][0])
                count = int(input('추가 개수:'))
                count = count + int(d[0][0])
                val = (str(count), p_id, b_id)  # 변수 처리
                sqlu(sql, val)
                break

        elif (menu == 2):
            while (True):
                menu2 = int(input('지점을 선택해주세요(1.서울 2.인천 3.수원 4.용인 5.대구 6.전체 7.뒤로가기):'))
                if (menu2 == 1):
                    print('날짜        지점    종류     가격  개수')
                    sql = "SELECT i.i_date,m.b_name,r.p_name,r.p_price,i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name=%s "
                    result = sqls(sql, ('서울'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')

                if (menu2 == 2):
                    print('날짜        지점    종류     가격  개수')
                    sql = "SELECT i.i_date,m.b_name,r.p_name,r.p_price,i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name=%s "
                    result = sqls(sql, ('인천'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                if (menu2 == 3):
                    print('날짜        지점    종류     가격  개수')
                    sql = "SELECT i.i_date,m.b_name,r.p_name,r.p_price,i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name=%s "
                    result = sqls(sql, ('수원'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                if (menu2 == 4):
                    print('날짜        지점    종류     가격  개수')
                    sql = "SELECT i.i_date,m.b_name,r.p_name,r.p_price,i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name=%s "
                    result = sqls(sql, ('용인'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                if (menu2 == 5):
                    print('날짜        지점    종류     가격  개수')
                    sql = "SELECT i.i_date,m.b_name,r.p_name,r.p_price,i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name=%s "
                    result = sqls(sql, ('대구'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')

                if (menu2 == 6):
                    print('날짜        지점    종류     가격  개수')
                    sql = "SELECT i.i_date,m.b_name,r.p_name,r.p_price,i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id "
                    result = sqlsa(sql)
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                if (menu2 == 7):
                    break
        elif (menu == 3):
            while (True):
                menu2 = int(input('지점을 선택해주세요(1.서울 2.인천 3.수원 4.용인 5.대구 6.뒤로가기):'))
                if (menu2 == 6):
                    break
                print('판매할 빵을 선택하세요.')
                print('1> 단팥빵')
                print('2> 소보루빵')
                print('3> 크림빵')
                print('4> 피자빵')
                print('5> 식빵')
                print('6> 슈크림빵')
                print('7> 초코머핀')
                print('8> 바게트빵')
                print()
                pp_id = int(input())
                if (pp_id == 1):
                    p_id = '1001'
                elif (pp_id == 2):
                    p_id = '1002'
                elif (pp_id == 3):
                    p_id = '1003'
                elif (pp_id == 4):
                    p_id = '1004'
                elif (pp_id == 5):
                    p_id = '1005'
                elif (pp_id == 6):
                    p_id = '1006'
                elif (pp_id == 7):
                    p_id = '1007'
                elif (pp_id == 8):
                    p_id = '1008'

                if (menu2 == 1):
                    b_id = '101'
                elif (menu2 == 2):
                    b_id = '102'
                elif (menu2 == 3):
                    b_id = '103'
                elif (menu2 == 4):
                    b_id = '104'
                elif (menu2 == 5):
                    b_id = '105'

                val1 = (b_id, p_id)

                sql = ("UPDATE iventory SET i_num=%s WHERE branch_b_id =%s AND breadd_p_id=%s")
                sql1 = ("SELECT i.i_num FROM iventory AS i WHERE i.branch_b_id =%s AND i.breadd_p_id=%s")
                sql2 = "INSERT INTO sorder (o_id,branch_b_id,breadd_p_id,p_num) VALUES (%s,%s,%s,%s)"
                sql3 = "INSERT INTO spayment (s_id,s_date,s_amount,order_o_id) VALUES (%s,%s,%s,%s) "
                sql4 = "select EXISTS (select * from sorder where o_id=1 limit 1) as isChk"
                sql6 = "SELECT b.p_price FROM breadd AS b WHERE b.p_id=%s"
                d = sqls(sql1, val1)
                find = sqlsa(sql4)
                if (int(find[0][0]) == 1):
                    sql5 = "SELECT MAX(o_id) FROM sorder"
                    finds = sqlsa(sql5)
                    i = int(finds[0][0]) + 1
                else:
                    i = 1
                d = [list(d[x]) for x in range(len(d))]
                dc = int(d[0][0])
                print("현재 개수:%d" % dc)
                count = int(input('판매할 개수:'))
                val2 = (str(i), b_id, p_id, str(count))

                if (count > dc):
                    print("재고가 %d개만 있습니다." % dc)
                    if (dc == 0):
                        print('재고가 %d개 판매불가 입니다.' % dc)
                        continue
                    s = input("%d개만 판매하시겠습니까?(y/n)" % dc)
                    if (s == 'y'):
                        count = dc
                    elif (s == 'n'):
                        continue
                p = sqls(sql6, str(p_id))
                print('총 가격:', int(p[0][0]) * count)
                now = datetime.now()
                val3 = (str(i), now.replace(microsecond=0), str(count), str(i))
                sqlu(sql2, val2)
                sqlu(sql3, val3)
                i += 1
                count = dc - count
                val = (str(count), b_id, p_id)
                sqlu(sql, val)

                d = sqls(sql1, val1)
                d = [list(d[x]) for x in range(len(d))]
                dc = int(d[0][0])
                print('남은재고:%d' % dc)
                ss = input("판매를 계속 하시겠습니까?(y/n)")
                if (ss == 'y'):
                    continue
                elif (ss == 'n'):
                    break
        elif (menu == 4):

            while (True):
                menu3 = int(input('지점을 선택해주세요(1.서울 2.인천 3.수원 4.용인 5.대구 6.당일 순이익 7.종료):'))
                if (menu3 == 1):
                    ds = []
                    print('당일 주문내역')
                    sql = (
                        "SELECT m.b_name,r.p_name,so.p_num FROM sorder AS so LEFT OUTER JOIN breadd AS r ON so.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON so.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql, ('서울'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('당일 판매내역')
                    sql1 = (
                        "SELECT m.b_name,r.p_name,so.s_amount,r.p_price*so.s_amount,so.s_date FROM spayment AS so LEFT OUTER JOIN sorder AS t ON so.order_o_id=t.o_id LEFT OUTER JOIN breadd AS r ON t.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON t.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql1, ('서울'))
                    d = [list(result[x]) for x in range(len(result))]
                    for i in range(len(result)):
                        ds.append(int(d[i][3]))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('서울지점 당일 매출:%d' % sum(ds))
                elif (menu3 == 2):
                    di = []
                    print('당일 주문내역')
                    sql = (
                        "SELECT m.b_name,r.p_name,so.p_num FROM sorder AS so LEFT OUTER JOIN breadd AS r ON so.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON so.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql, ('인천'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('당일 판매내역')
                    sql1 = (
                        "SELECT m.b_name,r.p_name,so.s_amount,r.p_price*so.s_amount,so.s_date FROM spayment AS so LEFT OUTER JOIN sorder AS t ON so.order_o_id=t.o_id LEFT OUTER JOIN breadd AS r ON t.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON t.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql1, ('인천'))
                    d = [list(result[x]) for x in range(len(result))]
                    for i in range(len(result)):
                        di.append(int(d[i][3]))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('인천지점 당일 매출:%d' % sum(di))
                elif (menu3 == 3):
                    dso = []
                    print('당일 주문내역')
                    sql = (
                        "SELECT m.b_name,r.p_name,so.p_num FROM sorder AS so LEFT OUTER JOIN breadd AS r ON so.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON so.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql, ('수원'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('당일 판매내역')
                    sql1 = (
                        "SELECT m.b_name,r.p_name,so.s_amount,r.p_price*so.s_amount,so.s_date FROM spayment AS so LEFT OUTER JOIN sorder AS t ON so.order_o_id=t.o_id LEFT OUTER JOIN breadd AS r ON t.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON t.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql1, ('수원'))
                    d = [list(result[x]) for x in range(len(result))]
                    for i in range(len(result)):
                        di.append(int(d[i][3]))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('수원지점 당일 매출:%d' % sum(di))
                elif (menu3 == 4):
                    dy = []
                    print('당일 주문내역')
                    sql = (
                        "SELECT m.b_name,r.p_name,so.p_num FROM sorder AS so LEFT OUTER JOIN breadd AS r ON so.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON so.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql, ('용인'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('당일 판매내역')
                    sql1 = (
                        "SELECT m.b_name,r.p_name,so.s_amount,r.p_price*so.s_amount,so.s_date FROM spayment AS so LEFT OUTER JOIN sorder AS t ON so.order_o_id=t.o_id LEFT OUTER JOIN breadd AS r ON t.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON t.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql1, ('용인'))
                    d = [list(result[x]) for x in range(len(result))]
                    for i in range(len(result)):
                        dy.append(int(d[i][3]))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('용인지점 당일 매출:%d' % sum(dy))
                elif (menu3 == 5):
                    dd = []
                    print('당일 주문내역')
                    sql = (
                        "SELECT m.b_name,r.p_name,so.p_num FROM sorder AS so LEFT OUTER JOIN breadd AS r ON so.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON so.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql, ('대구'))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('당일 판매내역')
                    sql1 = (
                        "SELECT m.b_name,r.p_name,so.s_amount,r.p_price*so.s_amount,so.s_date FROM spayment AS so LEFT OUTER JOIN sorder AS t ON so.order_o_id=t.o_id LEFT OUTER JOIN breadd AS r ON t.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON t.branch_b_id=m.b_id where b_name=%s")
                    result = sqls(sql1, ('대구'))
                    d = [list(result[x]) for x in range(len(result))]
                    for i in range(len(result)):
                        dd.append(int(d[i][3]))
                    for data in result:
                        print('--------------------------------------------------------')
                        print(data)
                        print('--------------------------------------------------------')
                    print('대구지점 당일 매출:%d' % sum(dd))
                elif (menu3 == 6):
                    print('당일 순이익')
                    sql = ("SELECT r.p_price*i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name='서울'")
                    sc = int(sqlsa(sql)[0][0])
                    print("서울 당일 순이익(판매금액-폐기된 빵):", sum(ds) - sc)
                    sql = "SELECT r.p_price*i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name='인천'"
                    sc = int(sqlsa(sql)[0][0])
                    print("인천 당일 순이익(판매금액-폐기된 빵):", sum(di) - sc)
                    sql = "SELECT r.p_price*i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name='수원'"
                    sc = int(sqlsa(sql)[0][0])
                    print("수원 당일 순이익(판매금액-폐기된 빵):", sum(dso) - sc)
                    sql = "SELECT r.p_price*i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name='용인'"
                    sc = int(sqlsa(sql)[0][0])
                    print("용인 당일 순이익(판매금액-폐기된 빵):", sum(dy) - sc)
                    sql = "SELECT r.p_price*i.i_num FROM iventory AS i LEFT OUTER JOIN breadd AS r ON i.breadd_p_id=r.p_id LEFT OUTER JOIN branch AS m ON i.branch_b_id=m.b_id where b_name='대구'"
                    sc = int(sqlsa(sql)[0][0])
                    print("대구 당일 순이익(판매금액-폐기된 빵):", sum(dd) - sc)
                elif (menu3 == 7):
                    exit()
