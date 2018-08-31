import xml.etree.ElementTree as ET


#
################################################################################
tree = ET.parse('./PerlegoXML/1.xml')
filename = '1.xml'
root = tree.getroot()
print("########################")
record_reference = root[-1][0].text
sales_rights = root[-1][-3][5]
territory = sales_rights[-1]
ans = {
  "fileName": filename,
  "recordReference": record_reference,
  "salesRightsType": sales_rights[0].text,
  "territory": territory[0].text
}
print(ans)

#
################################################################################
tree = ET.parse('./PerlegoXML/2.xml')
filename = '2.xml'
root = tree.getroot()
print("########################")
record_reference = root[-1][0].text
sales_rights = root[-1][-3][5]
territory = sales_rights[-1]
ans = {
  "fileName": filename,
  "recordReference": record_reference,
  "salesRightsType": sales_rights[0].text,
  "territory": territory[0].text
}
print(ans)

#
################################################################################
tree = ET.parse('./PerlegoXML/3.xml')
filename = '3.xml'
root = tree.getroot()
print("########################")
record_reference = root[-1][0].text
sales_rights = root[-1][-3][5]
territory = sales_rights[-1]
ans = {
  "fileName": filename,
  "recordReference": record_reference,
  "salesRightsType": sales_rights[0].text,
  "territory": territory[0].text
}
print(ans)

#
################################################################################
tree = ET.parse('./PerlegoXML/4.xml')
filename = '4.xml'
root = tree.getroot()
print("########################")
record_reference = root[-1][0].text
sales_rights = root[-1][-3][5]
territory = sales_rights[-1]
ans = {
  "fileName": filename,
  "recordReference": record_reference,
  "salesRightsType": sales_rights[0].text,
  "territory": territory[0].text.replace("\t", ', ').replace("\n", '')
}
print(ans)
