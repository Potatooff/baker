def load_file(text_path: str) -> None:
    """Loads a file from a given path and returns the text inside it."""

    text: str = ""
    try:
        with open(text_path, "r") as f:
            for line in f.readlines():
                text += line
            f.close()
        return text
    
    except:
        print("AN ERROR OCCURED IN load_save, loadsave.py - load_file()")
        return None


def save_file(self, text_path: str, text: str) -> None:
        """Saves a file to a given path with the text inside it."""

        try:
            with open(text_path, "a") as f:
                text = text + "\n"
                f.write(text)
                f.close()
        
        except:
            print("AN ERROR OCCURED IN load_save, loadsave.py - save_file()")


def clean_file(self, text_path: str) -> None:
    """Clean a file to a given path."""

    try:
        with open(text_path, "w") as f:
            f.write("")
            f.close()
    
    except:
        print("AN ERROR OCCURED IN load_save, loadsave.py - clean_file()")