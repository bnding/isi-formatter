from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("html")
args = parser.parse_args()



f = open(args.html, "r")
htmlText = f.read()
f.close()
# print(htmlText)

soup = BeautifulSoup(htmlText, 'html.parser')
soup.find(class_="isi-area").insert(1,BeautifulSoup("<p>Inserted!</p>", "html.parser"))

print(str(soup))


f=open("darzalex-isi-final.html", "w")
f.write(str(soup))
f.close()