from urllib.request import Request, urlopen
from math import log
import json

random_elements = []
req = Request("https://drand.cloudflare.com/public/latest", headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0"})
data = urlopen(req).read()
rd = json.loads(data)
random_elements.append(rd["randomness"])
last_round = rd["round"]

for i in range(19):
    req = Request("https://drand.cloudflare.com/public/"+str(last_round-i-1), headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:31.0) Gecko/20130401 Firefox/31.0"})
    data = urlopen(req).read()
    rd = json.loads(data)
    random_elements.append(rd["randomness"])
text = "".join(random_elements)
text_len = len(text)
dict = {}

for char in text:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
for char in dict:
    prob = dict[char]/text_len #pithanotita
    dict[char] = prob*log(prob)
dict_values = dict.values()

entropy = sum(dict_values)*(-1)
print("Entropy:", entropy)
