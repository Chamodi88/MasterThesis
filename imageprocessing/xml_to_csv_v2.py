"""
Usage:
# Processing test data:
python xml_to_csv_v2.py "PATH_TO_XML_FOLDER" "PATH_TO_OUTPUT_FOLDER"

"""

import os
import sys
import glob
import numpy as np
import xml.etree.ElementTree as ET

path = sys.argv[1]
outputpath = sys.argv[2]

for xml_file in glob.glob(path + '/*.xml'):
    xml_list = []
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
        value = (int(member[4][1].text),
                int(member[4][0].text),
                int(member[4][3].text),
                int(member[4][2].text)
                )
        name = root.find('filename').text
        xml_list.append(value)
    np.savetxt(os.path.join(outputpath, name.split('.')[0] + ".csv"), xml_list, fmt='%i', delimiter=',')
    xml_list.clear()

print('Successfully converted xml to csv.')


