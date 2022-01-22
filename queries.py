import psycopg2

###SQL Q:
#query function
def sqlsearch(sqlqry):
    conn = psycopg2.connect("dbname=McKeown user=postgres password=admin")
    conn.autocommit=True
    cur = conn.cursor()

    test = cur.execute(sqlqry)


    sqllist = []

    for i in cur.fetchall():
        sqllist.append(i)
    return sqllist

##Death by Year
sqlbyyear = str("SELECT year, COUNT (name) FROM	McKeown GROUP BY year ORDER BY year;")
##Death by Gender
sqlbygender = str("SELECT sex,	COUNT (name)FROM McKeown GROUP BY sex;")
##Death by Agency:
sqlbyagency = str('SELECT agency, COUNT (name) FROM McKeown GROUP BY agency;')
##Death by Context:
sqlbycontext = str("SELECT context,	COUNT (name) FROM McKeown GROUP BY context;")
