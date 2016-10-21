import requests
request= requests.get("https://google.com")
print(request)
if request.status_code==200:
	print("loaded")
else:
	print("failed")