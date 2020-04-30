import urllib.request, urllib.error, urllib.parse
import re
import html2text
open('output.txt', 'w').close()
filepath = 'links.txt'
with open(filepath) as fp:
   for cnt, url in enumerate(fp):
       print("Link {}: {}".format(cnt, url))
       response = urllib.request.urlopen(url)
       webContent = response.read().decode('utf-8')
       rendered_content = html2text.html2text(webContent)
       matches = re.findall(r"([A-Fa-f0-9]{64})", rendered_content)
       print("Found " + str(len(matches)) + " Hashes")
       with open("output.txt", "a") as myfile:
           for i in matches:
               myfile.write(i + '\n')
       count = 0
       with open("output.txt", 'r') as f:
           for line in f:
               count += 1

print("Total number of hashes is:", count)
