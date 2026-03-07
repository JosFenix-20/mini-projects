import sqlite3 as sql

DB_PATH = "C:\\Users\\FENIX\\Documents\\CODE_VISUAL\\PROYECTOS_PY\\inter\\Apy_rest\\database\\streamers.db"

def createDB():
    conect = sql.connect(DB_PATH)
    cursor = conect.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS streamers(
        name text,
        subs integer,
        followers integer   
    )""")
    conect.commit()
    conect.close()

def addValues():
    conect = sql.connect(DB_PATH)
    cursor = conect.cursor()
    data = [("alexelcapo",10000,800000),
            ("ibai",25000,7000000),
            ("elxokas",10000,1000000),
            ("auronplay",20000,8000000),
            ("cristini",5500,3000000)
        ]
    cursor.executemany("""INSERT OR IGNORE INTO streamers(name,subs,followers) VALUES (?,?,?)""",data)
    conect.commit()
    conect.close()

if __name__=="__main__":
    createDB()
    addValues()