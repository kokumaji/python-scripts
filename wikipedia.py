import prompts
import requests
import json
import sys
import webbrowser

URL = "https://en.wikipedia.org/w/api.php"

def random_article():
    PARAMS = {
        "action": "query",
        "format": "json",
        "generator": "random",
        "grnnamespace": "0",
        "prop": "revisions",
        "rvprop": "content",
        "grnlimit": "1" 
    }

    query = requests.get(url=URL, params=PARAMS)
    json_response = json.loads(query.text)
    first_element = list(json_response['query']['pages'].items())[0][1]

    title = first_element['title']
    print(f"Found Article '{title}'.")
    answer = prompts.yesno("Would you like to open this article?")
    if(answer == 1):
        title = title.replace(" ", "_")
        webbrowser.open(f"https://en.wikipedia.org/wiki/{title}")

def main():
    arg = sys.argv[1]
    if(arg == "-random"):
        random_article()

if __name__ == "__main__":
    main()
