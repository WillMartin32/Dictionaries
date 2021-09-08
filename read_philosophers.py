def main():

    infile = open('philosophers.txt' , 'r')

    file_contents = infile.read()

    line1 = infile.readline().rstrip('\n')
    line2 = infile.readline()
    line3 = infile.readline()

    print(line1)
    print(line2.rstrip('\n'))
    print(line3)
    