import psycopg2

conStr = "dbname='tensormsa' user='tfmsauser' host='localhost' password='1234'"
userId = "-1"

# Use Information
# from common.util import *
#
# println("S")
# println("Print Trace Information")
# println("Print1+Print2")
# println("E")
def println(printStr):
    conn = psycopg2.connect(conStr)
    cur = conn.cursor()

    if printStr == "S" or printStr == "s":
        sql = "delete from common_log_info where created_by = '"+userId+"'"
        cur.execute(sql)
        conn.commit()
    elif printStr == "E" or printStr == "e":
        sql = "select * from common_log_info where created_by = '"+userId+"' order by log_id"
        cur.execute(sql)
        rows = cur.fetchall()

        print("Trace.............................................................................")
        for i in range(0, len(rows)):
            for j in range(0, len(rows[i])):
                if rows[i][j] is not None and cur.description[j][0] not in (
                "id", "log_id", "creation_date", "last_update_date", "created_by", "last_updated_by"):
                    print(rows[i][j])
        print("..................................................................................")
    else:
        print(printStr)
        cur.execute("select COALESCE(max(log_id)::int,0)+10 seq from common_log_info where created_by = '"+userId+"'")
        rows = cur.fetchall()

        sql = "INSERT INTO common_log_info( "
        valueStr = ""

        valS = printStr.split("+")
        cnt = 1
        for i in valS:
            if cnt != 1 and cnt < 31:
                sql += ","
                valueStr += ","
            if cnt < 31:
                sql += str("attr") + str(cnt)
                valueStr += "'" + str(i) + "'"
            cnt += 1

        sql += ",creation_date,last_update_date, created_by, last_updated_by,log_id) "
        sql += "VALUES (" + valueStr + ",now(),now(),'"+userId+"','"+userId+"','" + str(rows[0][0]) + "')"

        cur.execute(sql)
        conn.commit()
    # 연결을 종료한다
    cur.close()
    conn.close()