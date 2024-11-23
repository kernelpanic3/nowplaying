import json
import pprint
import sseclient

sn = "station:"+"test"
print(sn)
data = json.dumps({ "subs": { "station:azuracast_test": {} }})
print(data)

def with_urllib3(url, headers):
    """Get a streaming response for the given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False, headers=headers)

def with_requests(url, headers):
    """Get a streaming response for the given event feed using requests."""
    import requests
    return requests.get(url, stream=True, headers=headers)

url = f"http://127.0.0.1/api/live/nowplaying/sse?cf_connect={data}"
headers = {'Accept': 'text/event-stream'}
response = with_urllib3(url, headers)  # or with_requests(url, headers)
client = sseclient.SSEClient(response)
for event in client.events():
    pprint.pprint(json.loads(event.data))