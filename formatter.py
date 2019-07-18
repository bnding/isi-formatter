import argparse

sections = ["important safety information", "contraindications",
            "warnings & precautions", "drug interactions", "adverse reactions", "use in specific populations"]


# TODO: Merging Injector.py with formatter.py... getFiles now returns the args object. Need to call args.isi, args.html
def getFiles():
    # parsing file into command line
    parser = argparse.ArgumentParser()
    parser.add_argument("isi")
    parser.add_argument("html")
    args = parser.parse_args()
    return args


def fileToList(fileName):
    f = open(fileName, "r")
    isiLines = [lines.replace('®', '<sup>®</sup>') for lines in f]
    f.close()
    return isiLines


def toHtml(isiLines):
    output = ""
    stack = []
    bulletState = {}
    bulletStack = []
    prevBullet = ""
    previous = ""
    previousSect = False
    for x in isiLines:
        # strips leading whitespace if it exists
        if(x[0] == ' ' or x[0] == '\t'):
            x = x.strip()
        isList = x[0] == '•' or x[0] == '-' or x[0] == '◦' or x[0] == '▲'
        if(isList == True):
            if(prevBullet == x[0]):
                bullet = x[0]
                x = x[1:].strip()
                if(previousSect):
                    output += "<ul><li>" + x + "</li>\n"
                    stack.append("<ul>")
                    bulletStack.append(bullet)
                    bulletState[bulletStack[len(bulletStack)-1]] = True
                    previous = "li"
                else:
                    # need an if statement here...
                    if ((bullet in bulletStack) and len(bulletStack) > 1):
                        while(bulletStack[len(bulletStack)-1] != bullet and len(bulletStack) > 1):
                            if(bulletStack[len(bulletStack)-1] == bullet):
                                break
                            bulletStack.pop()

                            output += "</ul>"
                            if(len(stack) >= 1):
                                stack.pop()
                    if(len(bulletStack) == 1):
                        if(previous == "p"):
                            output += "<ul><li>" + x + "</li>"
                            previous = "li"
                            stack.append("<ul>")
                        else:
                            output += "<li>" + x + "</li>"
                            previous = "li"
                    else:
                        output += "<ul><ul><li>" + x + "</li>\n"
                        stack.append("<ul>")
                        stack.append("<ul>")
                        previous = "li"

                previousSect = False
                bulletState[bulletStack[len(bulletStack)-1]] = True
                if(len(bulletStack) > 1):
                    prevBullet = bulletStack[len(bulletStack)-2]
                else:
                    prevBullet = ""
                    previous = "li"
                continue

            if(len(bulletStack) == 0):
                bulletStack.append(x[0])
            elif(bulletStack[len(bulletStack)-1] != x[0]):
                prevBullet = bulletStack[len(bulletStack)-1]
                bulletStack.append(x[0])
                x = x[1:].strip()
                bulletState[bulletStack[len(bulletStack)-1]] = True
                output += "<ul>\n<li>" + x + "</li>\n"
                stack.append("<ul>")
                previousSect = False
                previous = "li"
                continue

            if bulletStack[len(bulletStack)-1] not in bulletState:
                bulletState[bulletStack[len(bulletStack)-1]] = False

            # Checks if a <ul> needs to be added
            if bulletState[bulletStack[len(bulletStack)-1]] == False:
                bulletState[bulletStack[len(bulletStack)-1]] = True
                x = x[1:].strip()
                output += "<ul><li>" + x + "</li>\n"
                previousSect = False
                # stack is implemented to make sure </ul> is written if a list is that last element of list
                stack.append("<ul>")
                previous = "li"
            elif bulletState[bulletStack[len(bulletStack)-1]] == True:
                # Middle lists
                x = x[1:].strip()
                output += "<li>" + x + "</li>\n"
                previous = "li"
                previousSect = False

        # Non lists
        if(isList == False):
            # Checks for line breaks only or breaks with content
            if '\n' in x and len(x) > 1:
                # Check to see if closing ul tag is needed after last li tag
                if(bulletState):
                    if(bulletState[bulletStack[len(bulletStack)-1]] == True):
                        bulletState[bulletStack[len(bulletStack)-1]] = False
                        output += "</ul>\n"
                        if(len(stack) >= 1):
                            stack.pop()

                # \n exists as last character in non-break only lines. Need to remove
                if str(x.strip().lower()) in sections:
                    while(len(stack) != 0):
                        if(stack[len(stack)-1] == "<ul>"):
                            for bullets in bulletStack:
                                bulletState[bullets] = False
                            output += "</ul>\n"
                            stack.pop()
                    previousSect = True
                    x = x[:-1].strip()
                    output += "<h3 class='section'>" + x + "</h3>"
                    previous = "p"
                    continue
                x = x[:-1].strip()
                output += ("<p>" + x + "</p>\n")
                previous = "p"
                continue
            elif '\n' in x and len(x) == 1:
                output += "<br>\n"
                previousSect = False
            else:
                output += "<p>" + x + "</p>\n"
                previous = "p"
                previousSect = False

    # Check for any trailing ul tags
    while(stack):
        if(stack[len(stack)-1] == "<ul>"):
            output += "</ul>"
            stack.pop()

    return output



def main():
    fileName = getFiles().isi
    isiLines = fileToList(fileName)
    htmlIsi = toHtml(isiLines)

    f = open(fileName.replace(".txt", ".html"), "w+")
    f.write(htmlIsi)
    f.close()

    print(getFiles().html)


if __name__ == "__main__":
    main()
