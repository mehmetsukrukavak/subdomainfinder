import requests


def make_request(url):
    try:
      return requests.get(url)
    except:
        pass

target_input = "google.com" #input("Enter your target website: ")

with open("subdomainlist.txt", "r") as subdoman_list:
    for word in subdoman_list:
        word = word.strip()
        url = f"http://{word}.{target_input}"
        response = make_request(url)
        if response:
            print(f"Found -> {url}")