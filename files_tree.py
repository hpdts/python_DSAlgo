
"""
we are tasked with building a File Tree UI given a list of File objects,
consisting of a path and the contents of the file.
Your solution must:
display files in a nested structure,
with entries for each folder and file be able to handle arbitrarily-deep file 
structures sort folders are shown before files
all items are sorted alphabetically (case-insensitive)
given a list of File objects
Input:
path: Input
/input/folder1/folder/folder2/img21.jpg 
/input/folder1/folder/folder2/img22.jpg 
/input/folder1/folder/img1.jpg
output:
-input
    folder1
        folder
            folder2
                img21
                img22
            img1.jpg
            img2.jpg

    img11.jpg

"""
def get_tree(inputs):
    output={} 
    for input in inputs:
        #print(input)
        folders = input.split('/')
        #print(f"folders: {folders}")
        curr_node = output
        for folder in folders:
            if '.' in folder:
                curr_node[folder] = None
            else:
                if not folder in curr_node: 
                    curr_node[folder] = {}
                curr_node = curr_node[folder]
    return output

input = ["/input/folder1/folder/folder2/img21.jpg",
         "/input/folder1/folder/folder2/img22.jpg",
         "/input/folder1/folder/img1.jpg"]
"""
#print(get_tree(input))

#Print the tree now sortingh folders
def print_tree(node, indent=0):
    # Folders first, then files, both sorted alphabetically (case-insensitive)
    for key in sorted(node.keys(), key=lambda x: ('.' in x, x.lower())):
        print('    ' * indent + key)
        if isinstance(node[key], dict):
            print_tree(node[key], indent + 1)
"""

def print_tree(node, indent=0):
    for k in sorted(node.keys()):
        print(' ' * indent + k)
        if isinstance(node[k], dict):
            print_tree(node[k], indent + 1)
        


tree = get_tree(input)
print_tree(tree)



