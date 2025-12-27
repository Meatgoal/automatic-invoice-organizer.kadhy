import re


def safe_value(value: str | None, fallback: str = "NO_NUMBER") -> str:
    """
    Return a stripped value if present, otherwise return a fallback.

    :param value: Input value (can be None)
    :param fallback: Value to be used when input is empty or None
    :return: Safe string value
    """
    return value.strip() if value else fallback


def safe_name(value: str | None, fallback: str = "UNKNOWN") -> str:
    """
    Normalize and sanitize a name for use in filenames.

    - Converts to uppercase
    - Replaces invalid filename characters with '-'

    :param value: Raw name value (can be None)
    :param fallback: Value to be used when name is empty or None
    :return: Sanitized name safe for filenames
    """
    if not value:
        return fallback

    value = value.strip().upper()

    # Replace characters that are invalid in filenames
    return re.sub(r'[\\/:*?"<>|]', "-", value)


def build_nf_filename(info: dict) -> str:
    """
    Build a standardized NF filename using invoice information.

    Expected keys in info:
    - 'numero'
    - 'prestador'
    - 'tomador'

    :param info: Dictionary containing invoice metadata
    :return: Base filename without extension
    """
    return (
        f"NF {safe_value(info.get('numero'))} "
        f"{safe_name(info.get('prestador'))} "
        f"{safe_name(info.get('tomador'))}"
    )


def get_first_name(value: str | None) -> str | None:
    """
    Extract and return the first name from a full name string.

    :param value: Full name (can be None)
    :return: First name or None if value is empty
    """
    if not value:
        return None

    return value.strip().split()[0]
