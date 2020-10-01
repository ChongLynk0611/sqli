from urllib.parse import urlparse

url="http://localhost/DVWA/vulnerabilities/brute/?username=admin&password=password&Login=Login#"
parsed = urlparse(url)
queries = urlparse(url).query.split("&")
print(len(queries))