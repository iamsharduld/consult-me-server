import psycopg2

con = psycopg2.connect(
    host = 'ec2-3-215-83-17.compute-1.amazonaws.com',
    port = '5432',
    database = 'ddcf9ds377d9v3',
    user = 'ksuwummorvsqvg',
    password = '6a852012af5379f111a1fd444a61a497be1227dad940aeb28e47856c5b277bbd'
)

cur = con.cursor()


cur.execute("select first_name, last_name from users")
# cur.execute("CREATE TABLE users ( first_name VARCHAR(50), last_name VARCHAR(50));")
# cur.execute("\
#     INSERT INTO users VALUES \
#     ( 'Leo', 'Messi')\
#     ;"
#     )


rows = cur.fetchall()

for r in rows:
    print(r)

con.commit()

cur.close()

con.close()