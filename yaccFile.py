from lexFile import *
import ply.yacc as yacc
from grammarError import *
class MyParser:
 
  # Constructing the parser
    def __init__(self,lexer):
        print("Parser constructor called")
        precedence = (('DOTSTRING'),('HASHSTRING'),('STRING'))

        self.parser = yacc.yacc(module=self, debug=True,  start="start", write_tables=True)
        self.lexer = lexer
 
  # Destroying the parser
    def __del__(self):
        print('Parser destructor called.')
 
    #getting the list of tokens defined in the lexer
    tokens = MyLexer.tokens
 
#CFG being implemented:-
#(All words in caps are tokens (as defined in lexer))
#    start -> selectorlist styles
#    styles -> OPENBRACKET pairs CLOSEBRACKET
#    pairs -> STRING COLON STRING SEMICOLON | STRING COLON STRING SEMICOLON pairs 
#    classselector -> DOTSTRING
#    idselector -> HASHSTRING
#    selector -> classselector | idselector
#    selectorlist : selector | selectorlist selector

# all function of the form "p_..." describe productions of the cfg

    # GRAMMAR START

    def p_start(self,p):
        '''
        start : cssblocks
        '''
    def p_cssblocks(self,p):
        '''
        cssblocks : cssblock 
               | cssblocks cssblock  
        '''
    def p_cssblock(self,p):
        '''
        cssblock : selectorlist styles
        '''
    def p_styles(self,p):
        '''
        styles : OPENBRACKET cssprops CLOSEBRACKET
        '''
    def p_cssprops(self,p):
        '''
        cssprops : cssprop 
               | cssprops cssprop  
        '''
    def p_cssprop(self, p) :
        '''
        cssprop : STRING COLON values SEMICOLON 
        '''
    def p_values(self, p):
        '''
        values : STRING 
               | values STRING  
        '''

    def p_classselector(self,p):
        '''
        classselector : DOTSTRING
        ''' 
    def p_idselector(self,p):
        '''
        idselector : HASHSTRING
        '''
    def p_selector(self,p):
        '''
        selector : classselector 
                   | idselector
        '''
    def p_selectorlist(self,p):
        '''
        selectorlist : selectorlist selector
                       | selector  
        '''
    def p_error(self,p):
        if p:
            print("Syntax error at '%s'" % p.value)
            raise GrammarError("Parsing error at '%s'" % p.value, p.value)
        else:
            print("Syntax error at EOI")
            raise GrammarError("Parsing error at EOI", "@NA")
