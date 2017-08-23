import urllib.request

# response = urllib.request.urlopen("http://www.taobao.com")
# print(response.read())


def download(url, num_retries):
    print('downloading:', url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                return download(url, num_retries-1)
    return html

f = download('http://www.qq.com', -1)
print(f)
