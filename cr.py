import re, urllib.request

textfile = open('depth_1.txt','wt')

myurl = "https://wiprodigital.com/"
myurl = myurl.strip('\'"')

def findId(source):
    l = re.findall(r'"(http[s]*://wiprodigital.com\S+)"',source)
    return l

def get_source(url):
    url = myurl.strip('\'"')
    response = urllib.request.urlopen(url)
    page_source = response.read().decode('utf-8')
    return page_source

page_source = get_source(myurl)
links = set(findId(page_source))
for i in links:

    page_source = get_source(i)
    links = set(findId(page_source))
    print (i) 
    for ee in links:
        print ("    ",  ee)
        textfile.write(ee+'\n')

textfile.close()


