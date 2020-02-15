import psycopg2

class PGconnect():
    def __init__(self, host, port, dbname, user, password):
        connectStr = "host={} port={} dbname={} user={} password={}".format(host, port, dbname, user, password)
        self.connection = psycopg2.connect(connectStr)

    def getData(self, sql):cursor()
        cur = self.connection.
        cur.execute(sql)

        return cur

