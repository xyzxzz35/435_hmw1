#part 2(b)

import xml.etree.ElementTree as ET
tree = ET.parse('FoodServiceData.xml')
root = tree.getroot()

typeDescrip = []
for sub in root:
    for subElement in sub:
        if subElement.tag == "TypeDescription":
            typeDescrip.append(subElement.text)
num = {}
for types in typeDescrip:
    num[types] = num.get(types, 0) + 1
for i in num: 
    print(i," ",num[i])
    

    
#part 2(c)

type2 = []
for sub in root:
    for subelement in sub:
        if subelement.tag == "Grade":
            type2.append(subelement.text)
grades = {}
for grade in type2:
    grades[grade] = grades.get(grade, 0) + 1
for i in grades:
    print(i," ",grades[i])
