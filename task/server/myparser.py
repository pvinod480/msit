import xml.sax
class Handler(xml.sax.ContentHandler):
    def startElement(self,element,attr):
        pass
    def endElement(self,element):
        if element == "line":
                print(self.text)
                
    def chars(self,text):
        self.text=text
