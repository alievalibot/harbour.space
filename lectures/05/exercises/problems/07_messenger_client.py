"""Problem 07 (part B): messenger sender client.

Task:
1. Split into pairs
2. Write an infinite loop reading message text from terminal
3. Send each message to partner API endpoint /messages
4. Show send status in terminal


Partner setup:
- Partner gives you ngrok public URL
- You set TARGET_BASE_URL to that URL
"""

import requests

TARGET_BASE_URL = "https://replace-with-partner-ngrok-url"
SENDER_NAME = "replace-with-your-name"


def main() -> None:
    # TODO: implement input loop and POST sending
    pass
    print(f"Sending messages as '{SENDER_NAME}'. Type 'quit' to exit.")
    while True:
        text = input("Message: ")
        if text.strip().lower() == "quit":
            break
        try:
            response = requests.post(
                f"{TARGET_BASE_URL}/messages",
                json={"sender": SENDER_NAME, "text": text},
            )
            response.raise_for_status()
            print("Status:", response.json()["status"])
        except requests.exceptions.HTTPError as e:
            print("HTTP error:", e)
        except requests.exceptions.ConnectionError:
            print("Connection error: could not reach partner server")



if __name__ == "__main__":
    main()
