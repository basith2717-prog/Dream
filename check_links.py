import re

html = open('worksruthi.html', encoding='utf-8').read()
links = re.findall(r'<link[^>]+>', html)
for l in links:
    print('LINK:', l)

scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
for s in scripts:
    print('SCRIPT:', s)
