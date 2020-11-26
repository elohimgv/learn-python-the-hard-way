from sys import argv

script, filename = argv

fileObject = open(filename)

print("THE CONTENT OF THE FILE IS:")
print("."*20)
print(fileObject.read())
print("."*20)
fileObject.close()