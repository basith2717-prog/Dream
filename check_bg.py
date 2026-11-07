import urllib.request, re

for u in ['/_next/static/immutable/chunks/0_vr5kr4-0c-u.css', '/_next/static/immutable/chunks/3y62y2uuds32t.css']:
    css = urllib.request.urlopen('https://www.worksruthi.com' + u).read().decode('utf-8')
    for m in re.finditer(r'([^{}]*(?:body|html|\.hero|#hero)[^{}]*\{[^{}]*background[^{}]*\})', css, re.IGNORECASE):
        print('BG CSS:', m.group(1))
    for m in re.finditer(r'([^{}]*--spring[^{}]*)', css):
        print('SPRING VAR:', m.group(1)[:120])
