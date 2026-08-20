from psycopg2 import connect


def get_tasks():
    conn = connect(
        host="localhost",
        database="opspilot",
        user="postgres",
        password="blah123",
        port=5432,
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")

    rows = cursor.fetchall()

    print(rows)

    cursor.close()
    conn.close()
    return rows


def create_tasks_in_db(title: str, status: str = "pending"):
    conn = connect(
        host="localhost",
        database="opspilot",
        user="postgres",
        password="blah123",
        port=5432,
    )

    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO tasks(title,status)
    VALUES(%s,%s)
    RETURNING id,title,status
    """,
        (title, status),
    )

    task = cursor.fetchone()

    conn.commit()

    cursor.close()
    conn.close()
    return task
