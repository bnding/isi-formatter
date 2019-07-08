import argparse

# parsing file into command line
parser = argparse.ArgumentParser()
parser.add_argument("isi")
args = parser.parse_args()


keywords = "important safety information, contraindications, warnings and precautions, drug interactions"


f = open(args.isi, "r")

# putting lines of isi in array
isiLines = [lines.replace('®', '<sup>®</sup>') for lines in f]

output = ""

# filtering out newline breaks w/ breaks from end of file
for x in isiLines:

    # TODO: Start working on ul/li interpretation
    if(x[0] == '•' or x[0] == '-' or x[0] == '*'):

        output += "<ul><li>"
        print("BULLET")


    if '\n' in x and len(x) > 1:
        x=x[:-1]
        output += ("<p>" + x + "</p>\n")
    elif '\n' in x and len(x) == 1:
        output += "<br>\n"
    else:
        output += "<p>" + x + "</p>"

    print(x)

# print(output)
