
import xml.dom.minidom


doc=xml.dom.minidom.Document()

lines=doc.createElement("lines")
lines.setAttribute("word",word)


word=doc.createElement("words")
text=doc .createTextNode("land")


word.appendChild(text)
words.appendChild(word)
doc.appendChild(words)


print(doc.toxml())
print()
print(doc.toprettyxml())
