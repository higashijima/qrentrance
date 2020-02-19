import psycopg2

class PGconnect():
    def __init__(self, host, port, dbname, user, password):
        connectStr = "host={} port={} dbname={} user={} password={}".format(host, port, dbname, user, password)
        self.conn = psycopg2.connect(connectStr)

    def __del__(self):
        self.conn.close()
        print('connection terminated')

    def getData(self, sql, conditions):
        cur = self.conn.cursor()
        cur.execute(sql, conditions)

        return cur

    def getOneData(self, sql, conditions):

        return self.getData(sql, conditions).fetchone()
        

if __name__ == '__main__':
    db = PGconnect('192.168.11.9', 5432, 'qrentrance', 'postgres', '')

    records = db.getData('select id from qr_user where entry_hash=%s and entered_flg=%s', ('qrcode',False,))
    num = db.getOneData('select * from qr_user where entry_hash=%s and entered_flg=%s', ('qrcode',False,))
    empty = db.getData('select * from qr_user where 1=2', ())
    for record in records:
        print(record)
    print(num[0])
    print(num[1])
    print(num[2])
    print(len(empty.fetchmany()))
