# Python3 script

# Replace the html code for the menu in every html file in the current folder recursively, except in menu.html, by the code in the aforementioned file
# Allows to quickly change a menu item without having to copy-paste it in every file by hand

import fileinput
import os
import codecs

# Get every html file (except menu.html) into a list
listfiles = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html") and not "menu.html" in file:
            listfiles.append(os.path.join(root,file))

# Read the content of menu.html into a list
def get_menu_content():
    menu = codecs.open('menu.html', encoding='utf-8')
    content = menu.readlines() 
    menu.close();
    return content

#print('[%s]' % ', '.join(map(str, listfiles)))
#print('[%s]' % ', '.join(map(str, content)))

# Return the index in the list containing the substring
def index_containing_substring(the_list, substring):
    for i, s in enumerate(the_list):
        if substring in s:
            return i
    return -1

# Return content but with the class for the current menu added based on the folder in which the file is
def content_for_current_menu(filepath, menucontent):
    # First Menu item
    if "commencer" in filepath:
	# Find the line corresponding to this item in content
        index = index_containing_substring(menucontent, 'Pour commencer</a>')
        # Add the class identifier at this index
        menucontent[index] = '			<li class="dropdown"><a class="current" href="#">Pour commencer</a>\n'
        return menucontent
    # Second Menu item
    elif "demarche" in filepath:
	# Find the line corresponding to this item in content
        index = index_containing_substring(menucontent, 'Les démarches</a>')
        # Add the class identifier at this index
        menucontent[index] = '			<li class="dropdown"><a class="current" href="#">Les démarches</a>\n'
        return menucontent
    # Third Menu item
    elif "S5" in filepath:
	# Find the line corresponding to this item in content
        index = index_containing_substring(menucontent, 'Partir au S5</a>')
        # Add the class identifier at this index
        menucontent[index] = '			<li class="dropdown"><a class="current" href="#">Partir au S5</a>\n'
        return menucontent
    # Fourth Menu item
    elif "S4" in filepath:
	# Find the line corresponding to this item in content
        index = index_containing_substring(menucontent, 'Partir au S4</a>')
        # Add the class identifier at this index
        menucontent[index] = '			<li class="dropdown"><a class="current" href="#">Partir au S4</a>\n'
        return menucontent
     # Home
    else:
        # Find the line corresponding to this item in content
        index = index_containing_substring(menucontent, 'Home</a></li>')
        # Add the class identifier at this index
        menucontent[index] = '			<li><a class="current" href="index">Home</a></li>\n'
        return menucontent

# Open a file, remove the content between the two markers, and replace it by the content of menu.html
def replace_in_file(filename, newcontent):
    writing = True
    for line in fileinput.input([filename], inplace=True):
        if writing:
            if '<!-- Menu begin -->' in line:
                writing = False
                print(line, end="")
                for lines in newcontent:
                    print(lines, end="")
            else: 
                print(line, end="")
        else:
            if '<!-- Menu end -->' in line: 
                writing = True
                print(line, end="")
    return 1
	   
	   
# Apply replace_in_file to the html files
for html in listfiles:
    oldcontent = get_menu_content()
    if replace_in_file(html, content_for_current_menu(html, oldcontent)) == 1:
        print('Fichier ' + html + ' modifié')