import requests

def request_feed_content(url):
    try:
        full_response = requests.get(url, timeout=30)
        request_content = str(full_response.content)
        request_content = request_content.split('\\n')
        return request_content
    except:
        print(f"An error occured with {url}")