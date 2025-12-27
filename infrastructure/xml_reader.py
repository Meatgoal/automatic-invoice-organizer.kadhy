import xml.etree.ElementTree as ET
from pathlib import Path
from domain.naming import get_first_name


def extract_nf_data_from_xml(xml_path: Path) -> dict:
    """
    Extract relevant NF (invoice) data from an XML file.

    Extracted fields:
    - Invoice number
    - Service provider first name
    - Service taker first name

    :param xml_path: Path to the XML file
    :return: Dictionary containing extracted invoice data
    :raises FileNotFoundError: If the XML file does not exist
    """
    if not xml_path.exists():
        raise FileNotFoundError("XML file not found.")

    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Extract XML namespace dynamically
    namespace = {"ns": root.tag.split("}")[0].strip("{")}

    numero_tag = root.find(".//ns:Numero", namespace)
    prestador_tag = root.find(".//ns:Prestador/ns:RazaoSocial", namespace)
    tomador_tag = root.find(".//ns:Tomador/ns:RazaoSocial", namespace)

    return {
        "numero": numero_tag.text if numero_tag is not None else None,
        "prestador": get_first_name(prestador_tag.text if prestador_tag is not None else None),
        "tomador": get_first_name(tomador_tag.text if tomador_tag is not None else None),
    }
