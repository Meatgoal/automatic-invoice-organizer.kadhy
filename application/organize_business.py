from domain.organizacao_fiscal import (
    is_nf_folder,
    current_year_folder_name,
    current_month_folder_name
)
from infrastructure.filesystem import list_directories, create_directory


def get_nf_folder(business_dir):
    """
    Find and return the NF (invoice) folder inside a business directory.

    :param business_dir: Path to the business root directory
    :return: Path to the NF folder
    :raises FileNotFoundError: If no NF folder is found
    """
    for folder in list_directories(business_dir):
        if is_nf_folder(folder.name):
            return folder

    raise FileNotFoundError("NF folder not found")


def get_year_folder(nf_dir):
    """
    Get the folder for the current year inside the NF directory.
    If it does not exist, it will be created.

    :param nf_dir: Path to the NF directory
    :return: Path to the year folder
    """
    year_name = current_year_folder_name()

    for folder in list_directories(nf_dir):
        if folder.name == year_name:
            return folder

    # Create year folder if it does not exist
    new_folder = nf_dir / year_name
    create_directory(new_folder)
    return new_folder


def get_month_folder(year_dir):
    """
    Get the folder for the current month inside the year directory.
    If it does not exist, it will be created.

    :param year_dir: Path to the year directory
    :return: Path to the month folder
    """
    month_name = current_month_folder_name()

    for folder in list_directories(year_dir):
        if folder.name == month_name:
            return folder

    # Create month folder if it does not exist
    new_folder = year_dir / month_name
    create_directory(new_folder)
    return new_folder
