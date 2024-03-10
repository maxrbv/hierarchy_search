import requests


def make_req(elem_id: str):
    url = "http://localhost:8000/get_path"
    data = {
        "elem_id": elem_id
    }
    r = requests.post(url, json=data)
    print(r.text)


if __name__ == "__main__":
    elem_id = "zany-zircon-investigatess"
    make_req(elem_id)
