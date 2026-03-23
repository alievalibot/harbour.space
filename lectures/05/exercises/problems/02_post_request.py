"""Problem 02: POST request to JSONPlaceholder.

Task:
1. Send POST to https://jsonplaceholder.typicode.com/posts
2. Send JSON payload with fields: title, body, userId
3. Print:
   - status code
   - raw body
   - parsed JSON
4. Confirm response includes your data + id

Note: JSONPlaceholder simulates writes; data is not truly persisted.
"""

import requests

URL = "https://jsonplaceholder.typicode.com/posts"


def main() -> None:
    # TODO: create payload dict
    # TODO: send POST request with json=payload
    # TODO: print response details
    pass
    payload = {
        "title": "Hello World",
        "body": "This is my first post",
        "userId": 1,
    }

    response = requests.post(URL, json=payload)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
        return

    print("Status code:", response.status_code)
    print("Raw body:", response.text)

    data = response.json()
    print("Parsed JSON:", data)

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data
    print("Confirmed: response includes our data + id:", data["id"])

if __name__ == "__main__":
    main()
