import sqlite3
from infrastructure.config import businesses_txt_path


# Path to the text file containing the list of businesses
txt_path = businesses_txt_path()


def create_database(conn) -> None:
    """
    Create the database schema if it does not already exist.

    The 'files' table stores registered businesses and their active status.
    """
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            business_name TEXT UNIQUE NOT NULL,
            active INTEGER DEFAULT 1
        )
        """
    )
    conn.commit()


def connect_database(db_name: str = "business.db") -> sqlite3.Connection:
    """
    Create a connection to the SQLite database and ensure the schema exists.

    :param db_name: Database file name
    :return: SQLite connection instance
    """
    conn = sqlite3.connect(db_name)
    create_database(conn)
    return conn


def import_businesses_from_txt(conn) -> None:
    """
    Import business names from a text file into the database.

    Existing businesses are ignored to avoid duplicates.
    """
    cursor = conn.cursor()

    with txt_path.open("r", encoding="utf-8") as file:
        for line in file:
            business_name = line.strip()

            # Skip empty lines
            if not business_name:
                continue

            cursor.execute(
                "INSERT OR IGNORE INTO files (business_name) VALUES (?)",
                (business_name,),
            )

    conn.commit()
