# code

# Open the file with read only permit
f = open('file_00.txt')
# use readline() to read the first line
line = f.readline()
# use the read line to read further.
# If the file is not empty keep reading one line
# at a time, till the file is empty
fileNames=[]
while line:
    fileNames.append(line.rstrip())
    line = f.readline()
f.close()
fc = open("c_file_00.txt", "w")
fcpp = open("cpp_file_00.txt", "w")
fcs = open("cs_file_00.txt", "w")
for file in fileNames:
    index = file.find('.')
    extension=file[index+1:]
    if(extension=="c"):
        fc.write(file+"\n")
    if(extension=="cs"):
        fcs.write(file+"\n")
    if(extension=="cpp"):
        fcpp.write(file+"\n")
fc.close()
fcpp.close()
fcs.close()

# outputs

# cpp_file_00.txt


def process_source_files(baseFilename):
    c_output = open('c_' + baseFilename + '.txt', 'w')
    cpp_output = open('cpp_' + baseFilename + '.txt', 'w')
    cs_output = open('cs_' + baseFilename + '.txt', 'w')

    with open(baseFilename, 'r') as file:
        lines = file.readlines()
        for line in lines[2:]:  # Start from the 3rd line based on the sample input
            filename = line.strip()
            if filename.endswith('.c'):
                c_output.write(filename + '\n')
            elif filename.endswith('.cpp'):
                cpp_output.write(filename + '\n')
            elif filename.endswith('.cs'):
                cs_output.write(filename + '\n')

    c_output.close()
    cpp_output.close()
    cs_output.close()

# Example usage
input_filename = 'names_list_00.txt'
process_source_files(input_filename)

