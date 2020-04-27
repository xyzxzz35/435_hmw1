import pandas as pd
import numpy as np
import lxml.etree as ET
from lxml import html,etree
import re
import requests


def read_html(path,num):
    htmlFile = open(path, 'r', encoding='utf-8')
    hr = htmlFile.read() 
    start = hr.find("\"works\": [")
    end = hr[start:].find("</script>") + start
    hr_1 = hr[start:end]
    title_start = [i.start() for i in re.finditer("title",hr_1)]
    title_start.append(len(hr_1)-1)
    
    title = []
    price = []
    formatt = []
    condition = []
    author = []

    for i in range(len(title_start)-1):
        space = hr_1[title_start[i]:title_start[i+1]]
        
        title_find = [i.start() for i in re.finditer("\"",space)]
        title_space = space[(title_find[1]-1):title_find[2]]
        title.append(title_space)

        price_find = space.find("lowPrice")
        price_space = space[price_find:]
        price_2 = [price_space.find(" "),price_space.find(",")]
        price_s = price_space[(price_2[0]+1):price_2[1]]
        price.append(price_s)
 
        format_find = space.find("media")
        format_space = space[format_find:]
        format_2 = [i.start() for i in re.finditer("\"",format_space)]
        format_s = format_space[(format_2[1]+1):format_2[2]]
        formatt.append(format_s)
        
        condition_find = space.find("qualityDescription")
        condition_space = space[condition_find:]
        if "null" not in condition_space[:30]:
            condition_2 = [i.start() for i in re.finditer("\"",condition_space)]
            condition_s = condition_space[(condition_2[1]+1):condition_2[2]]
            condition.append(condition_s)
        else:
            condition.append("null")

        author_find = space.find("authorName")
        author_space = space[author_find:]
        if author_find != -1:
            author_2 = [i.start() for i in re.finditer("\"",author_space)]
            author_s = author_space[(author_2[1]+1):author_2[2]]
            author.append(author_s)
        else:
            author.append("null")
    
    root = ET.Element('books')
    subroot = ET.SubElement(root,"book")
    for col in range(len(title)):
        sub_1 = ET.SubElement(subroot,"title").text = title[i]
        sub_2 = ET.SubElement(subroot,"price").text = price[i]
        sub_3 = ET.SubElement(subroot,"format").text = formatt[i]
        sub_4 = ET.SubElement(subroot,"condition").text = condition[i]
        sub_5 = ET.SubElement(subroot,"authors").text = author[i]

    printoff = (ET.tostring(root, pretty_print = True, encoding="UTF-8", xml_declaration = True))
    filename = "book" + str(num) + ".xml"
    f = open(filename,'wb')
    f.write(printoff)
        
read_html("././././././Browse | New & Used Books from ThriftBooks1.html",1)
read_html("././././././Browse | New & Used Books from ThriftBooks2.html",2)
read_html("././././././Browse | New & Used Books from ThriftBooks3.html",3)
read_html("././././././Browse | New & Used Books from ThriftBooks4.html",4)
read_html("././././././Browse | New & Used Books from ThriftBooks5.html",5)
read_html("././././././Browse | New & Used Books from ThriftBooks7.html",7)
read_html("././././././Browse | New & Used Books from ThriftBooks8.html",8)
read_html("././././././Browse | New & Used Books from ThriftBooks9.html",9)