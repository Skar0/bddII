from xml.dom import minidom
doc = minidom.parse('1-3.xml')

def afficher_dico(racine, chaine) :
	nbr_fils = 0
	for noeud in racine.childNodes :
		if noeud.nodeType != 3 :
			if noeud.getElementsByTagName('mot') == [] :
				print chaine + noeud.attributes["att"].value
			else :
				afficher_dico(noeud, (chaine + noeud.attributes["att"].value + "-"))

afficher_dico(doc.firstChild, "")