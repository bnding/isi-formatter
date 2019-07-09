import argparse

keywords = ["important safety information", "contraindications",
            "warnings and precautions", "drug interactions"]


def getFile():

    # parsing file into command line
    parser = argparse.ArgumentParser()
    parser.add_argument("isi")
    args = parser.parse_args()
    return args.isi


def fileToList(fileName):

    f = open(fileName, "r")
    isiLines = [lines.replace('®', '<sup>®</sup>') for lines in f]
    f.close()
    return isiLines


def toHtml(isiLines):
    output = ""
    stack = []

    listState = False
    for x in isiLines:
        isList = x[0] == '•' or x[0] == '-' or x[0] == '*'

        # Checks if the current line is a list
        if(isList == True):
            # Checks if a <ul> needs to be added
            if listState == False:
                listState = True
                x = x[1:].strip()
                output += "<ul><li>" + x + "</li>\n"
                # stack is implemented to make sure </ul> is written if a list is that last element of list
                stack.append("<ul>")
                continue

            elif listState == True:
                # Middle lists
                x = x[1:].strip()
                output += "<li>" + x + "</li>\n"
                continue

        # Non lists
        if(isList == False):
            # Checks for line breaks only or breaks with content
            if '\n' in x and len(x) > 1:
                # Check to see if closing ul tag is needed after last li tag
                if(listState == True):
                    listState = False
                    output += "</ul>\n"
                    stack.pop()

                # \n exists as last character in non-break only lines. Need to remove
                x = x[:-1]
                output += ("<p>" + x + "</p>\n")
            elif '\n' in x and len(x) == 1:
                output += "<br>\n"
            else:
                output += "<p>" + x + "</p>\n"

    # Check for any trailing ul tags
    while(stack):
        if(stack[len(stack)-1] == "<ul>"):
            output += "</ul>"
        stack.pop()

    return output


def main():
    fileName = getFile()
    isiLines = fileToList(fileName)
    htmlIsi = toHtml(isiLines)

    f = open(fileName.replace(".txt", ".html"), "w+")
    f.write(htmlIsi)
    f.close()


if __name__ == "__main__":
    main()
