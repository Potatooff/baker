

def load_file(text_path: str):
    """Loads a file from a given path and returns the text inside it."""

    text: str = ""
    try:
        with open(text_path, "r") as f:
            for line in f.readlines():
                text += line
            f.close()
        return text
    
    except:
        print("AN ERROR OCCURED IN load_save, loadsave.py load_file()")
        return None


def save_file(text_path: str, text: str): ... # TODO: Implement this function.