from pathlib import Path


def businesses_base_dir() -> Path:
    """
    Return the base directory where all business folders are stored.

    This path is currently hardcoded for the local development environment.
    """
    return Path("/home/gabriel/Downloads/Meu_projeto/data/Empresas/")


def downloads_dir() -> Path:
    """
    Return the system Downloads directory used as input/output workspace.
    """
    return Path("/home/gabriel/Downloads/")


def businesses_txt_path() -> Path:
    """
    Return the path to the text file containing the list of businesses.

    This file is used as a reference source for business names.
    """
    return Path("/home/gabriel/Downloads/Meu_projeto/Automatic_move_files.kadhy/empresas_Y.txt")
