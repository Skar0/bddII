from xml.dom import minidom
doc = minidom.parse('1-1.xml')
print doc.toxml()
       
print doc.firstChild.getAttribute('nom')       
print doc.firstChild.getAttribute('prenom')       
print doc.firstChild.getElementsByTagName('email')[0].firstChild.data
print doc.firstChild.getElementsByTagName('adresse')[0].firstChild.data 
print doc.firstChild.getElementsByTagName('adresse')[0].attributes['codePostal'].value
print doc.firstChild.getElementsByTagName('phone')[0].attributes['number'].value

# Index out of range
# print doc.firstChild.getElementsByTagName('age')[0].firstChild.data 

# Ca sort [], une liste vide
# print doc.firstChild.getElementsByTagName('age')

# 3 (text node)
# print doc.firstChild.getElementsByTagName('email')[0].firstChild.nodeType

# affiche la doc
# print help(doc.firstChild.getElementsByTagName('email')[0].firstChild)

# 1
# print len(doc.childNodes)

doc.firstChild.getElementsByTagName('email')[0].firstChild.replaceWholeText("email_bidon@hotmail.com")
print doc.firstChild.getElementsByTagName('email')[0].firstChild.data

doc.firstChild.getElementsByTagName('phone')[0].attributes['number'].value = "0483378209345775"
print doc.firstChild.getElementsByTagName('phone')[0].attributes['number'].value

print help(doc.firstChild.getElementsByTagName('email')[0])