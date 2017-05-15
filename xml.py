import xml.etree.ElementTree as ET

tree = ET.parse('country.xml')
root = tree.getroot()

print(root.tag)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)
#end

print(root[0][1].text)

for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)
#end
