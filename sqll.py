import mysql.connector
db=mysql.connector.connect(host="localhost",user ="root",password="4801")
cur=db.cursor()
cur.execute("use mns")
cur.execute("insert into Agents(agent,amount)values('divya',60000)")
cur.execute("select * from Agents")
for x in cur:
    print(x)
db.commit()
