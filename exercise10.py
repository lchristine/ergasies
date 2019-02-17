import re
import urllib.request

x = input('Give url: ')

if not x.startswith('http'):
    x = 'http://' + x
response = urllib.request.urlopen(x)
y = response.read().decode()

number_links = len(re.findall(r'<a .*?href=".*?".*?>.*?<\/a>', y))

number_lines = len(re.findall(r'<br .*?/?>', y))
number_lines += len(re.findall(r'<p .*?>.*?<\/p>', y))

print('There are %s links' % number_links)
print('There are %s newlines' % number_lines)