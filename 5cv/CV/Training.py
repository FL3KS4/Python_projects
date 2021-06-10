"""
Useful links:
https://naucse.python.cz/lessons/intro/testing/
https://refactoring.guru/design-patterns/observer/python/example
http://voho.eu/wiki/navrhovy-vzor/
https://docs.python.org/3/library/tkinter.html
https://docs.python.org/3/library/xml.etree.elementtree.html
"""


import xml.etree.ElementTree as ET

root = ET.parse("file.xml")

datums = root.findall('datum')

for datum in datums:
    print(datum)
    pass

for datum in datums:
    print(datum.attrib)
    pass

for datum in datums:
    print(datum.attrib['den'])
    pass

for datum in datums:
    print(datum.get("den"))
    pass

for datum in datums:
    jidla = datum.iter('jidlo')
    for jidlo in jidla:
        print(jidlo.attrib['nazev'])
        pass
        for ingredience in jidlo.iter('ingredience'):
            print(" ", ingredience.attrib['nazev'])
            pass


#Save to XML example
root = ET.Element("root")
doc = ET.SubElement(root, "doc")

ET.SubElement(doc, "field1", name="name1").text = "some value1"
ET.SubElement(doc, "field2", name="name2").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")
