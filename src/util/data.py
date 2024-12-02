def read_file(filename='text.txt'):
    content = ""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File was not found"
    except Exception as e:
        return f"Something went wrong: {e}"