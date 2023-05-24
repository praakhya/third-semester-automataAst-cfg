import ply.lex as lex
import ply.yacc as yacc
import sys
 
from lexFile import *
from yaccFile import *
 
# create objects MY LEXER and MY PARSER
myLex = MyLexer() #imported from lexFile.py
myPars = MyParser(myLex) #imported from yaccFile.py
 
lex = myLex.lexer
parser = myPars.parser
 
# reading INPUT FILE
 
myFile = open("data.txt","r") #opening data.txt which contains the text (CSS) to be read and parsed
parser.parse(myFile.read()) #parsing the CSS text
