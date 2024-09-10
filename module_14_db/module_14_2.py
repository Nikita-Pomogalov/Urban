import sqlite3


con = sqlite3.connect('not_telegram.db')
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")
cur.execute(' CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
cur.execute(" DELETE FROM Users WHERE id = ?", (6,))

cur.execute(" SELECT COUNT(*) FROM Users")
total_users = cur.fetchone()[0]
cur.execute("SELECT SUM(balance) FROM Users")
all_balances = cur.fetchone()[0]
print(all_balances/total_users)

# users = cur.fetchall()
# for user in users:
#     print(f'Имя: {user[0]}|Почта: {user[1]}|Возраст: {user[2]}|Баланс: {user[3]}')

con.commit()
con.close()