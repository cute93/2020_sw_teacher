import requests
from xml.etree import ElementTree

xmlurl = 'https://api.manana.kr/exchange/rate/KRW/KRW,USD,JPY.xml'
xmlresp = requests.get(xmlurl)
if xmlresp.ok :
    print(xmlresp.text)
root = ElementTree.fromstring(xmlresp.content)
print(dir(root))
items = root.findall('item')
print(type(root))

''''
print(len(items))
for e in items.pop().getchildren():
    print(f'{e.tag} : {e.text}')
    '''