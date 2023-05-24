import ply.lex as lex
import ply.lex as lex
import ply.yacc as yacc
import sys
from ply.lex import TOKEN
 
class MyLexer():
 
 
  # Constructing the lexical analyser
  def __init__(self):
      print('Lexer constructor called.')
      self.lexer = lex.lex(module=self)
      self.lexer.begin('INITIAL')

  # Destroying the lexical analyser
  def __del__(self):
      print('Lexer destructor called.')


  # list of tokens 
  tokens = [
  'DOTSTRING',
  'HASHSTRING',
  'STRING',
  'COLON',
  'SEMICOLON',
  'OPENBRACKET',
  'CLOSEBRACKET',
  'IGNORE'
  ]

#All functions of the form "t_..." describe tokens used in the cfg

  # Token that defines a string that can start with a dot followed by one alphabet and any combination of alphanumeric characters
  # used for the class name
  def t_DOTSTRING(self,t):
    r'\.[A-Za-z][0-9A-Za-z]{0,}'
    print("DOTSTRING: ",t.value,sep=" ") 
    return t

  # Token that defines a string that can start with a hash followed by one alphabet and any combination of alphanumeric characters
  # used for the id name
  def t_HASHSTRING(self,t):
    r'\#[A-Za-z][0-9A-Za-z]{0,}'
    print("HASHSTRING: ",t.value,sep=" ")
    return t

  # Token that defines a string that contains any combination of 1 or more alphanumeric characters
  # used for property names and value names
  def t_STRING(self,t):
    r'[0-9A-Za-z\-]{1,}'
    print("STRING: ",t.value,sep=" ")
    return t

  # It represents the "." character
  def t_DOT(self,t):
    r'\.'
    print("DOT")
    return t

  # It represents the ":" character
  def t_COLON(self,t):
    r':'
    print("COLON")
    return t
  
  # It represents the ";" character
  def t_SEMICOLON(self,t):
    r';'
    print("SEMICOLON")
    return t
  
  # It represents the "{" character
  def t_OPENBRACKET(self,t):
    r'\{'
    print("OPENBRACKET")
    return t

  # It represents the "}" character
  def t_CLOSEBRACKET(self,t):
    r'\}'
    print("CLOSEBRACKET")
    return t

  # It contains all the characters that can be ignored while analysing the string
  def t_IGNORE(self, t):
    r'[ \t\n]'
    pass

  # every symbol that doesn't match with almost one of the previous tokens is considered an error
  def t_error(self,t):
      r'.'
      print("ERROR:", t.value)
      return t

