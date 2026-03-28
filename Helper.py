import json
from typing import List, Dict


def dump_json_to_file(data: List[Dict], filename: str) -> None:
    """
    Dumps a list of dictionaries into a JSON file.

    :param data: List of JSON dictionaries
    :param filename: File name without extension (or with .json)
    """

    # Ensure .json extension
    if not filename.endswith(".json"):
        filename = f"{filename}.json"

    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"✅ Data successfully written to {filename}")

    except Exception as e:
        print(f"❌ Error writing file: {e}")