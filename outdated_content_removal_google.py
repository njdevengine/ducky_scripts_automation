#save the html from google results pages into text.txt
with open('text.txt', 'r') as file:
    data = file.read().replace('\n', '')
    
links = []
for i in data.split(" "):
    if "http://thesite.org/" in i:
        links.append(i)
links2 = []
for i in links:
    for n in i.split('"'):
        if "http" in n:
            links2.append(n.replace("}",""))
links3 = []
for i in links2:
    if i[0] =="h":
        links3.append(i)
links4 = list(set(links3))
#check links
# for i in links4:
#     print(i)

p1 = """
DELAY 1000
GUI SPACE
STRING terminal
DELAY 500
ENTER
DELAY 4000
STRING open https://www.google.com/webmasters/tools/removals
ENTER
DELAY 5000
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
TAB
DELAY 500
STRING """
p2 = """
ENTER
DELAY 6000
TAB
DELAY 500
TAB
DELAY 500
ENTER
DELAY 1000
GUI SHIFT w
"""
# for i in links4:
#     print(p1+i+p2)
