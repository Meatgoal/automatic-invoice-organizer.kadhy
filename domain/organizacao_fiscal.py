from datetime import datetime


# Keywords used to identify NF (invoice) folders
NF_KEYWORDS = {"NF", "NOTA", "FISCAL", "FATURAMENTO"}


def current_year_folder_name() -> str:
    """
    Return the folder name for the current year.

    Example:
        "2025"
    """
    return str(datetime.now().year)


def current_month_folder_name() -> str:
    """
    Return the folder name for the current month and year.

    Format:
        MM-YYYY (e.g. "03-2025")
    """
    now = datetime.now()
    return f"{now.month:02d}-{now.year}"


def is_nf_folder(name: str) -> bool:
    """
    Check whether a folder name represents an NF (invoice) directory.

    The check is case-insensitive and based on predefined keywords.

    :param name: Folder name to be validated
    :return: True if it matches an NF folder, False otherwise
    """
    name = name.upper()
    return any(keyword in name for keyword in NF_KEYWORDS)

