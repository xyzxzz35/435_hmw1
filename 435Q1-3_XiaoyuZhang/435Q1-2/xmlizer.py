import csv
import pandas as pd
from lxml import etree as et

#parser = etree.XMLParser(recover=True)
#root = etree.fromstring('FoodServiceData.xml', parser=parser)
#xmldata = open('root', 'w')

#csvdata = csv.reader(open('FoodServiceData.csv'))
#xmldata = open('FoodServiceData.xml', 'w')

csvfile = pd.read_csv("FoodServiceData.csv")
cols = list(csvfile.columns)
root = et.Element('foodservices')

with open("FoodServiceData.csv") as c:
    next(c)
    csvdata = csv.reader(c)
    for row in csvdata:
        sub = et.SubElement(root,'foodservice')
        for col in range(len(cols)):
            sub_sub = et.SubElement(sub,cols[col]).text = row[col]           
printoff = (et.tostring(root, pretty_print = True, encoding="UTF-8",xml_declaration = True))

xmldata = open('FoodServiceData.xml','wb')
xmldata.write(printoff)

