def main():
    encrytion= {"A" : "%", "a" : "9", "B" : "@", "b" : "#", "C" : "!", "c" : "1" , "D" : "$", "d" : "2", "E" : "^", "e" : "3",
            "F" : "&", "f" : "4", "G" : "5", "g" : "*", "H" : "6", "h" : "(", "I" : "7", "i" : ")", "J" : "8", "j" : "-",
            "K" : "0", "k" : "_", "L" : "=", "l" : "+", "M" : "`", "m" : "~", "N" : "[", "n" : "{", "O" : "]", "o" : "}",
            "P" : "|", "p" : ";", "Q" : "(-:]", "q" : "'", "R" : '"', "r" : ",", "S" : "<", "s" : ">", "T" : "(-.]", "t" : "/",
            "U" : "?", "u" : "(:-)", "V" : "(;-)", "v" : "(;-(", "W" : "(:-(", "w" : "(:-/", "X" : "(:-?", "x" : "[:-)",
            "Y" : "[:-(", "y" : "[:-/", "Z" : "[;-)", "z" : "[;-(", " " : " ", "." : ".", ":" : ":"}
    encrypting_security_info(encrytion)

def encrypting_security_info(codes):
    infile = open('info_security.txt' , 'r')
    file_contents = infile.read()
    outfile = open('encrypted_info_security.txt' , 'w')

    for x in file_contents:
        encrypt = codes[x]
        outfile.write(encrypt)

    infile.close()
    outfile.close()

main()