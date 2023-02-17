import psycopg2


conn = psycopg2.connect(database="", user="", password="" , host="")
cur = conn.cursor()
print("Database opened successfully")


class BD1:
	def ss():
		cur.execute("""SELECT * FROM users""")
		query_results = list(cur.fetchall())
		text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
		return str(text)


	def counter():
		cur.execute("""SELECT * FROM users""")
		query_results = list(cur.fetchall())
		#text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
		return query_results


	def mailing():
		cur.execute("""SELECT * FROM users""")
		query_results = list(cur.fetchall())
		#text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
		return query_results

	def add(user):
		cur.execute(f"""INSERT INTO users(tg_id) VALUES ({user})""")