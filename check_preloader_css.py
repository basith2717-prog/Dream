import urllib.request, re

for u in ['/_next/static/immutable/chunks/0_vr5kr4-0c-u.css', '/_next/static/immutable/chunks/3y62y2uuds32t.css']:
    css = urllib.request.urlopen('https://www.worksruthi.com' + u).read().decode('utf-8')
    for m in re.finditer(r'([^{}]*preloader[^{}]*\{[^{}]*\})', css, re.IGNORECASE):
        print('PRELOADER CSS:', m.group(1))
    for m in re.finditer(r'([^{}]*\.pl-[^{}]*\{[^{}]*\})', css, re.IGNORECASE):
        print('PL CSS:', m.group(1))
