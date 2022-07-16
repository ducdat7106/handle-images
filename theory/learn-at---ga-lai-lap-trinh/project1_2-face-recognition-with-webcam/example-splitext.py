import os
path = 'home/User/Desktop/file.txt'

root_path = os.path.splitext(path)

print(path)

print(root_path)
print(root_path[0])
print(root_path[1])



print("root path of '%s':" % path, root_path)