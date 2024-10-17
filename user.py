data_dir = "/data"
save_extension = ".json"


def query_save_file(id: str):
    if not id:
        return None
    return f"{data_dir}/user/{id}{save_extension}"
