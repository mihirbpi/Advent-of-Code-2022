from aocd import get_data
data = get_data(year=2022, day=7).split("\n")

class directory_node:

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.dir = True

    def add_child(self, new_child):
        self.children.append(new_child)
    
    def get_size(self):
        return sum([x.get_size() for x in self.children])

    def get_children(self):
        return self.children
    
    def get_parent(self):
        return self.parent
    
    def get_name(self):
        return self.name

    def is_dir(self):
        return self.dir

class file_node:

    def __init__(self, name, size, parent):
        self.parent = parent
        self.name = name
        self.size = size
        self.dir = False

    def get_size(self):
        return self.size
    
    def get_parent(self):
        return self.parent
    
    def get_name(self):
        return self.name
    
    def is_dir(self):
        return self.dir

root = directory_node("/", None)
curr_dir = root

for command in data[2:]:
    command_split = command.split(" ")

    if(command_split[0] == "dir"):
        curr_dir.add_child(directory_node(command_split[1], curr_dir))

    elif(command_split[1] == "cd"):

        if(command_split[2] == ".."):
            curr_dir = curr_dir.get_parent()

        elif(command_split[2] == "/"):
            curr_dir = root

        else:

            for child in curr_dir.get_children():

                if(child.get_name() == command_split[2]):
                    curr_dir = child
                    break

    elif(command_split[1] != "ls"):
        curr_dir.add_child(file_node(command_split[1], int(command_split[0]), curr_dir))

directory_sizes = []

def add_directory_sizes(dir):
    directory_sizes.append(dir.get_size())

    for child in dir.get_children():

        if(child.is_dir()):
            add_directory_sizes(child)

add_directory_sizes(root)
unused_space = 70000000 - directory_sizes[0]
min_size = 1e99

for size in directory_sizes:

    if(size + unused_space >= 30000000):
        min_size = min(size, min_size)
        
print(min_size)
