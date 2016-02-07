from xml.dom import minidom
from os import listdir
from os.path import isdir, isfile
doc = minidom.Document()

def createArbo(path, node) :
	for elem in listdir(path) :
		if isfile(path+"/"+elem) :
			temp = doc.createElement("elem")
			temp.setAttribute("type"  , "file")
			temp.setAttribute("name"  , elem)
			node.appendChild(temp)
		else :
			temp = doc.createElement("elem")
			temp.setAttribute("type"  , "folder")
			temp.setAttribute("name"  , elem)
			node.appendChild(temp)
			createArbo(path+"/"+elem, temp)

def createDoc() :
	doc.appendChild(doc.createElement("arbo"))

	path = str(raw_input('Enter a path:\n'))
	createArbo(path, doc.firstChild)

	file_handle = open("2-5.xml","wb")
	doc.firstChild.writexml(file_handle)
	file_handle.close()

createDoc()