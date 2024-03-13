
def get_extention(title: str) -> str:
    return title.split(".")[-1]

def is_movie(title: str) -> bool:
    expected_extentions = {
        "mkv",
        "mp4",
        "avi",
    }
    return get_extention(title) in expected_extentions

def is_nfo(title: str) -> bool:
    return get_extention(title) == "nfo"
