from os import system 
from files.URLS import whatsapp,instagram,youtube 
from files.Hadings import Heading, Sub_head
from files.Writer import writer 


Heading()
print('\n'*2)
text = '''                This tool for crack any insta passwords. 
                This tool is very powerful. 
                this tool for only education purpose. 
                so please don'tuse for illegal work'''

writer(text)

youtube()
input('Tap Enter:  ')
instagram()
input('Tap Enter:  ')
whatsapp()

system('clear')
Sub_head()
print('\n'*2)


system('python files/insta_brut.py')