import json


def load_config(file_path):
    """
    Load configuration from a JSON file.
    """
    with open(file_path, "r") as file:
        config = json.load(file)

    return config


if __name__ == "__main__":

    config = load_config("config/default.json")

    print(config)