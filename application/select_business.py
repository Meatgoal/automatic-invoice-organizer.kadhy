def search_businesses(conn, term: str) -> list[str]:
    """
    Search for business names that start with the given term.

    The result is limited to 20 entries and ordered alphabetically.

    :param conn: Active database connection
    :param term: Search term used as the prefix for business names
    :return: List of matching business names
    """
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT business_name
        FROM files
        WHERE business_name LIKE ?
        ORDER BY business_name
        LIMIT 20
        """,
        (term + "%",),
    )

    # Extract only the business_name column from the result set
    return [row[0] for row in cursor.fetchall()]
