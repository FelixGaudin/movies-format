import xml.etree.ElementTree as ET

def parse_nfo(file_path: str) -> dict:
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Récupérer le titre du film
    title = root.find(".//title").text

    # Récupérer les genres du film
    genres = [genre.text for genre in root.findall(".//genre")]

    # Récupérer l'année du film
    year = root.find(".//year").text

    # Récupérer l'URL de l'affiche du film
    poster = root.find(".//thumb").text

    return {
        "title" : title,
        "genres" : genres,
        "year" : year,
        "poster" : poster,
    }
