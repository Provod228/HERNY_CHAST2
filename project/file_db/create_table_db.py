import sqlite3


def create_user(cursor_db) -> None:
    cursor_db.execute('''
        CREATE TABLE IF NOT EXISTS User (
        id INTEGER PRIMARY KEY,
        username varchar (64) NOT NULL,
        login  varchar (32) not null unique,
        email varchar (254) not null unique,
        password VARCHAR (128) NOT NULL,
        role_id INTEGER,
        FOREIGN KEY (role_id) REFERENCES Role (id)
        )
    ''')


def create_role(cursor_db) -> None:
    cursor_db.execute('''
        CREATE TABLE IF NOT EXISTS Role (
        id INTEGER PRIMARY KEY,
        title varchar (64) NOT NULL unique
    )
    ''')


def create_educational_material(cursor_db) -> None:
    cursor_db.execute('''
        CREATE TABLE IF NOT EXISTS EducationalMaterial (
        id INTEGER PRIMARY KEY,
        title varchar (256) NOT NULL unique,
        summery TEXT not NULL,
        material_file BLOB not NULL,
        subject_id INTEGER,
        FOREIGN KEY (subject_id) REFERENCES Subject (id)
        )
    ''')


def create_subject(cursor_db) -> None:
    cursor_db.execute('''
        CREATE TABLE IF NOT EXISTS Subject (
        id integer primary key,
        title varchar (64) NOT NULL unique
        )
    ''')


if __name__ == "__main__":
    connection = sqlite3.connect('../school.db')

    cursor = connection.cursor()

    create_educational_material(cursor)
    create_role(cursor)
    create_user(cursor)
    create_subject(cursor)

    connection.commit()

    connection.close()
