import xml.etree.ElementTree as ET


class XMLParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.root = ''

    def get_root(self):
        tree = ET.parse(self.filepath)
        self.root = tree.getroot()


    def find_filename(self):
        return self.filepath[-5:]


    def find_record_reference(self):
        return self.root[-1][0].text


    def find_sales_rights_type(self):
        ans = self.root[-1][-3][5][0].text
        if ans == None:
            ans = "INVALID SalesRightsType"
        return ans


    def find_territory(self):
        return self.root[-1][-3][5][-1][0].text.replace("\t", ', ').replace("\n", '')
