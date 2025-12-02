from flask import Flask
import requests

app = Flask(__name__)


def fetch_long_titles(min_length: int = 60):
    """Fetch posts and return a list of dicts for titles longer than min_length."""
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        res = requests.get(url, timeout=10)
    except requests.RequestException:
        return []

    if res.status_code != 200:
        return []

    posts = res.json()
    result = []
    for post in posts:
        title = post.get("title", "")
        if len(title) > min_length:
            spaces = title.count(" ")
            words = spaces + 1 if title else 0
            result.append(
                {
                    "title": title,
                    "spaces": spaces,
                    "words": words,
                }
            )
    return result


@app.route("/")
def index():
    long_titles = fetch_long_titles()
    html_items = "".join(
        f"<li><strong>{item['title']}</strong><br>"
        f"Spaces: {item['spaces']} | Words: {item['words']}</li>"
        for item in long_titles
    )

    return f"""
    <html>
    <head>
        <title>Posts titles longer than 60 chars</title>
    </head>
    <body>
        <h1>Posts titles longer than 60 chars</h1>
        <ul>
            {html_items}
        </ul>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
