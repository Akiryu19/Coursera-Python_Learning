import requests
import json
import requests_cache

requests_cache.configure()

parameters = {"term":"Ann arbor", "entity": "podcast"}
url = "https://itunes.apple.com/search"
iTunes_response = requests_with_caching.get(url,params = parameters, permanent_cache_file = "itunes_cache.txt")
py_data = json.loads(iTunes_response.)
