# ISI-Formatter &middot; ![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg) #
The ISI-Formatter is a small python project I did during my internship automates the tedious task of adding tags to the Instructional Safety Information for drugs being developed by pharmaceutical companies.

Automation includes...

* p tags
* ul/li tags (nested)
* superscript tags
* Section header detection

The formatter is designed to automatically update the file that needs the ISI and will only require CSS styling afterwards. This was not implemented as each company has different layouts and designs within the ISI.

## Installation ##

#### Python3 ####
Download [here](https://www.python.org/downloads/)

#### BeautifulSoup ####
`pip3 install beautifulsoup4`

If above does not work, go [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

## Inputs ##
#### ISI text file ####
The ISI must first be placed into a `.txt` file before it can be read with the formatter. There is a testcases folder that should have some txt files you can use as an example.

#### HTML file to write into ####
There needs to be an HTML file that the `formatter.py` can write the ISI into.

**IMPORTANT:** Make sure that the area you want the ISI to be in is an **empty** div element with class name `isi-area` in the html file before running.

## Running the Script ##

In the command line, run `python3` with `formatter.py`. The order of the two arguments will always be the **ISI** followed by the **HTML file** that you wish to put the formatted ISI into. 

For our example, `darzalex-isi-final.html` has an empty div with the class name `isi-area`. Any of the text files in the `testscases` folder should be able to be placed into the darzalex html file.

To format the ISI and write it into `darzalex-isi-final.html`, we can run...
`python3 formatter.py testcases/darzalex-isi.txt darzalex-isi-final.html`

This will result in the html file filled in with the formatted text file!