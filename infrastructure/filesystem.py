from pathlib import Path


def get_two_latest_files(downloads_path: Path) -> list[Path]:
    """
    Return the two most recently modified files from a directory.

    :param downloads_path: Directory to search for files
    :return: List containing up to two Path objects
    """
    files = [file for file in downloads_path.iterdir() if file.is_file()]

    files_sorted = sorted(
        files,
        key=lambda file: file.stat().st_mtime,
        reverse=True,
    )

    return files_sorted[:2]


def rename_file(old_path: Path, new_path: Path) -> Path:
    """
    Rename (or move) a file to a new path.

    :param old_path: Original file path
    :param new_path: New file path
    :raises FileExistsError: If the destination file already exists
    :return: The new file path
    """
    if new_path.exists():
        raise FileExistsError(f"File already exists: {new_path}")

    old_path.rename(new_path)
    return new_path


def path_exists(path: Path) -> bool:
    """
    Check whether a path exists.

    :param path: Path to be checked
    :return: True if the path exists, False otherwise
    """
    return path.exists()


def list_directories(path: Path) -> list[Path]:
    """
    List all directories inside the given path.

    :param path: Base directory
    :return: List of directory paths
    """
    return [p for p in path.iterdir() if p.is_dir()]


def create_directory(path: Path) -> None:
    """
    Create a directory if it does not exist.

    :param path: Directory path to be created
    """
    path.mkdir(exist_ok=True)

