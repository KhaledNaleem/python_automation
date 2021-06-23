import os
import PyPDF2

read_file = open('dictionary.txt')
file_content = read_file.read()

wordlist = file_content.split('\n')

pdfreader = PyPDF2.pdfFileReader(open('pdf_file', 'rb'))

try:
    if pdfreader.isENcrypted == True:
        for word in wordlist:
            pdfreader.decrypt(word)
            if (decrypt()): return 1
            elif not (decrypt()): return 0

    else:
        pdfreader.numPages