"""Problem 03: GET request for HTML content.

Task:
1. Send GET to https://example.com
2. Print:
   - status code
   - Content-Type header
   - HTML body (response.text)
3. Verify content type contains text/html
4. Add raise_for_status()
"""

import requests

URL = "https://example.com"


def main() -> None:
    # TODO: implement GET request and print HTML response
    pass
    response = requests.get(URL, verify=False)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
        return

    print("Status code:", response.status_code)
    print("Content-Type:", response.headers["Content-Type"])
    print("HTML body:", response.text)

    assert "text/html" in response.headers["Content-Type"]
    print("Confirmed: Content-Type contains text/html")



if __name__ == "__main__":
    main()
