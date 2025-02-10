from os import system 
from file.URLS import whatsapp,instagram,youtube 
from file.Hadings import Heading, Sub_head
from file.Writer import writer 

system("clear")
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


system('python file/insta_brut.py')
