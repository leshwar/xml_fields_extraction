# Importing packages
import re, collections, glob, json, timeit
from lxml import etree
from lxml.etree import tostring
from collections import defaultdict

#--------------------------------- Global Variables ---------------------------------
#Need to remove this from data structure
FILE_MARKER = '<files>'

#Get list of files
files_list = [f for f in glob.glob("**/*.xml", recursive=True)]

#Get the total number of files
total_files = len(files_list)

#Variable to store XML paths and attributes
xml_structure = collections.OrderedDict()
main_dict = defaultdict(dict)

#--------------------------------- Global Functions ---------------------------------

#Building the Tree Structure
def attach(branch, trunk):
    parts = branch.split('/', 1)
    if len(parts) == 1:  # branch is a file
        if(parts[0]) not in trunk:
            trunk[parts[0]] = defaultdict(dict)
    else:
        node, others = parts
        if node not in trunk:
            trunk[node] = defaultdict(dict)
        attach(others, trunk[node])

#Printing the XML structure
def prettify(d, indent=0):
    for key, value in d.items():
        if key == FILE_MARKER:
            if value:
                print("{0} {1}: {2}".format('    ' * indent, indent, str(value)))
        else:
            print("{0} {1}: {2}".format('    ' * indent, indent, str(key)))
            if isinstance(value, dict):
                prettify(value, indent+1)
            else:
                print("{0} {1}: {2}".format('    ' * indent+1, indent+1, str(value)))

#Record the Start time
start = timeit.default_timer()

#Print processing start statistics
print("Total number of XML files found: {0} \n".format(total_files))
print(" Started processing files \n")

#Iterate though each file and process it.
for file_no, file_name in enumerate(files_list):
    
    # open file in ReadOnly mode
    with open(file_name, 'r') as file_to_read: 
        xml_string = file_to_read.read() #Fetch the XML file as a String
        file_to_read.close()
        xml_root = etree.fromstring(xml_string) #Fetch the root element of the XML
        raw_tree = etree.ElementTree(xml_root)
        
        for tag in xml_root.iter():
            path = re.sub('\[[0-9]+\]', '', raw_tree.getpath(tag))
            if path not in xml_structure:
                xml_structure[path] = []
            
            #Get the xml tag attributes and append them
            if len(tag.keys()) > 0:
                xml_structure[path].extend(attrib for attrib in tag.keys() if attrib not in xml_structure[path])            

    for line in xml_structure:
        attach(line, main_dict)
        
    #Print processing end statistics
    print("\n Processed file {0} of {1} \t Filename: {2} \n".format((file_no + 1), total_files, file_name))

#Record the End time
stop = timeit.default_timer()

print(xml_structure)

print("Completed parsing {0} files. \n".format(total_files))
print("--------------------------------- Parsing Statistics --------------------------------- \n")
print("Time taken to process: {0} Seconds \n".format(stop - start))
      
print("--------------------------------- Master XML Structure ---------------------------------\n")
prettify(main_dict)
    
#     #Print all the paths found - Reference Function
#     for path, attribs in xml_structure.items():
#         indent = int(path.count('/') - 1)
#         print('{0}{1}: {2} [{3}]'.format('    ' * indent, indent, path.split('/')[-1], ', '.join(attribs) if len(attribs) > 0 else '-'))
    