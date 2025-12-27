from infrastructure.db_repository import connect_database, import_businesses_from_txt
from presentation.app import App


def main() -> None:
    """
    Application entry point.

    - Connects to the database
    - Imports businesses from the reference text file
    - Starts the GUI application
    """
    conn = connect_database()
    import_businesses_from_txt(conn)

    app = App(conn)
    app.mainloop()


if __name__ == "__main__":
    main()
