#!/usr/bin/env python

"""
CONVERTER
----------------------------------------------------------
This program requires an xml file named export.xml to run.
----------------------------------------------------------
Follow these steps
1. Open SecureCRT
2. Click "Tools"
3. Click "Export Settings..."
4. Verify that ONLY "Sessions" is checkmarked. If not,
   Make it so.
5. Export the file to the same directory as this script
6. Run script
"""

__author__ = "Ryan Murray"
__version__ = "1.0"
__maintainer__ = "Ryan Murray"
__email__ = "ryan.murray.570@gmail.com"
__status__ = "Prototype"

import xml.etree.ElementTree as ET

tree = ET.parse('.\export.xml')
root = tree.getroot()

print('---')
print('all:')
print('  children:')

check = []
for child in root:
    for root_name in child:
        if root_name.tag == 'key':
            print("    " + str(root_name.attrib['name']) + ":") # Done BRAIDWOOD:
        for child1 in root_name:
            for child2 in child1:
                if child2.attrib == {'name': 'Hostname'} and str(child1.attrib['name']) not in check:
                    print("      hosts:")
                    for child1_host in root_name:
                        for child2_host in child1_host:
                            if child2_host.attrib == {'name': 'Hostname'}:
                                print("        " + str(child1_host.attrib['name']) + ":")
                                print("          ansible_host: " + str(child2_host.text))
                                check.append(str(child1_host.attrib['name']))
                else:
                    for child3 in child2:
                        if child3.attrib == {'name': 'Hostname'} and str(child2.attrib['name']) not in check:
                            print("      children:")
                            for child1_host in root_name:
                                if child1_host.tag == 'key':
                                    print("        " + str(child1_host.attrib['name']) + ":")
                                    print("          hosts:")
                                for child2_host in child1_host:
                                    for child3_host in child2_host:
                                        if child3_host.attrib == {'name': 'Hostname'}:
                                            print("            " + str(child2_host.attrib['name']) + ":")
                                            print("              ansible_host: " + str(child3_host.text))
                                            check.append(str(child2_host.attrib['name']))
                        else:
                            for child4 in child3:
                                if child4.attrib == {'name': 'Hostname'} and str(child3.attrib['name']) not in check:
                                    print("        " + str(child1_host.attrib['name']) + ":")
                                    print("          children:")
                                    for child1_host in root_name:
                                        for child2_host in child1_host:
                                            if child2_host.tag == 'key':
                                                print("          " + str(child2_host.attrib['name']) + ":")
                                                print("            hosts:")
                                            for child3_host in child2_host:
                                                for child4_host in child3_host:
                                                    if child4_host.attrib == {'name': 'Hostname'}:
                                                        print("              " + str(child3_host.attrib['name']) + ":")
                                                        print("                ansible_host: " + str(child4_host.text))
                                                        check.append(str(child3_host.attrib['name']))
        check = []
