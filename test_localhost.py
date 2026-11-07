import urllib.request

html = urllib.request.urlopen('http://localhost:5173/').read().decode('utf-8')
print('HTML length:', len(html))
print('Has preloader:', 'id="preloader"' in html)
print('Has hero:', 'hero--sruthi' in html)
print('Has bq:', 'id="boss-quote"' in html)
