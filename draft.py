import sys

import requests


def make_req(elem_id: str):
    url = "http://localhost:8000/get_path"
    data = {
        "elem_id": elem_id
    }
    r = requests.post(url, json=data)
    print(r.text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python draft.py elem_id")
        sys.exit(1)

    elem_id = str(sys.argv[1])
    make_req(elem_id)
