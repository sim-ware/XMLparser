class XMLParser
    #TODO: want to pass in filepath, and have root/filename returned
    #have filepath as attribute
    def __init__(self,filepath):
        self.filepath=filepath

    def get_root(filepath):
        tree = ET.parse(filepath)
        return tree.getroot()
        # pass

    def find_filename(filepath):
        return filepath[-5:-1]

    def find_record_reference(root):
        return root[-1][0].text
        pass

    def find_sales_rights_type(root):
        return root[-1][-3][5][0].text
        pass

    def find_territory(root):
        return root[-1][-3][5][0][0].text.replace("\t", ', ').replace("\n", '')
        pass

    # def eval_countries_permitted(root):
    #     pass

end
