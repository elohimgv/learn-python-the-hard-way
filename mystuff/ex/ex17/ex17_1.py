from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(
    """
    Do you want to copy files from 
    %s to %s
    """ % (from_file, to_file))

in_file = open(from_file)

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_file.read())

print("Alright, all done.")

out_file.close()
in_file.close()