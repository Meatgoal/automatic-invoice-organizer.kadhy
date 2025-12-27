from pathlib import Path
from infrastructure.filesystem import rename_file
from domain.naming import build_nf_filename


def process_business_files(
    files: list[Path],
    info: dict,
    destination_dir: Path
) -> list[Path]:
    """
    Rename and move invoice-related files (PDF and XML) to the destination folder
    using a standardized NF filename.

    :param files: List of file paths to be processed
    :param info: Dictionary containing invoice data used to build the filename
    :param destination_dir: Target directory where files will be moved
    :return: List of renamed file paths
    """
    renamed_files: list[Path] = []

    # Build the base filename once (without extension)
    base_name = build_nf_filename(info)

    for file in files:
        # Process only PDF and XML files
        if file.suffix.lower() not in {".pdf", ".xml"}:
            continue

        # Create the new full path with the same extension
        new_path = destination_dir / f"{base_name}{file.suffix}"

        # Rename (and move) the file to the destination directory
        rename_file(file, new_path)

        renamed_files.append(new_path)

    return renamed_files
