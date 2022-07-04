# This program removes all moves from a pgn.
# First ask the name of the pgn to import


chesspgn= input("Which pgn you want to have without moves? ", )
#Now I open the file
cpgn= open(chesspgn, "r")

#Defining a function to readlines and append them in new pgn


def createnewpgn(pgnfile):
    newpgn=open("newpgnnomoves.pgn","w+")
    for line in pgnfile:

        if line[0]=="[":
            newpgn.writelines(line)
        elif line[0]=="1":
            newpgn.writelines("\n1.\t \n\n")
def main():
    createnewpgn(cpgn)
    cpgn.close()
if __name__ == '__main__':
    main()
