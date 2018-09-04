import sys

sys.path.append('./lib')

from xmlparser import *
from dbhandler import *


import os
rootdir = './PerlegoXML'

files_list = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filepath = os.path.join(subdir, file)
        if ".xml" in filepath:
            files_list.append(filepath)


dbhandler = DBHandler('perlego.db')
dbhandler.create_table()


for file in files_list:
    xmlparser = XMLParser(file)
    xmlparser.get_root()
    filename = xmlparser.find_filename()
    record_reference = xmlparser.find_record_reference()
    sales_rights_type = xmlparser.find_sales_rights_type()
    print(sales_rights_type)
    territory = xmlparser.find_territory()

    dbhandler.create_row(filename, int(record_reference), sales_rights_type, territory)

dbhandler.commit_changes()
dbhandler.close_connection()
