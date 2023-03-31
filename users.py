import sqlite3


# Fonction pour initialiser la base de données
def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            ip_address TEXT,
            cookie TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Fonction pour récupérer un utilisateur à partir de son nom d'utilisateur
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', [username])
    user = cursor.fetchone()
    conn.close()
    return user

def insert_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username=?', [username])
    row = cursor.fetchone()
    if row is not None:
        return "Le nom d'utilisateur existe déjà"
        # Le username est déjà présente, ne rien faire
        pass
    else:
        # Le username n'est pas présente, l'insérer dans la table
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', [username, password])
        conn.commit()
        return None
    conn.close()
