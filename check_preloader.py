import urllib.request, re

req = urllib.request.Request('https://www.worksruthi.com/', headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    css_urls = re.findall(r'href=["\'](/_nuxt/[^"\']+\.css)["\']', html)
    print('CSS URLs:', css_urls)
    for u in css_urls:
        full_url = 'https://www.worksruthi.com' + u
        css_content = urllib.request.urlopen(urllib.request.Request(full_url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')
        for m in re.finditer(r'([^{}]*(?:preloader|\.pl-)[^{}]*\{[^{}]*\})', css_content, re.IGNORECASE):
            print('MATCH:', m.group(1)[:150])
except Exception as e:
    print('Error:', e)
