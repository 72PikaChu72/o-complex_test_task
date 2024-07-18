import sqlite3

class Database:
    def startDatabase():
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                request TEXT,
                success BOOLEAN
                )""")
        
    def addRequest(text, success):
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO requests VALUES (NULL, ?, ?)", (text, success))
    
    def getRequests():
        with sqlite3.connect("database.db") as db:
            cursor = db.cursor()
            cursor.execute("""SELECT request, COUNT(CASE WHEN success = 1 THEN 1 END) AS successes, COUNT(CASE WHEN success = 0 THEN 1 END) AS errors
                            FROM requests
                            GROUP BY request""")
            rows = cursor.fetchall()
            k = cursor.description
            return [dict(zip([col[0] for col in k], row)) for row in rows]

Database.startDatabase()