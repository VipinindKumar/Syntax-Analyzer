class JackTokenizer:
    ''' class used to tokenize the input
    file(s)? into a stream of tokens, ignoring
    whitespace, comments etc.'''
    
    symbols = ['{', '}', '(', ')', '[', ']', '.',
    ',', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
    
    keywords = ['class', 'constructor', 'function', 'method', 'field', 
    'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 
    'null', 'this', 'let', 'do', 'while', 'if', 'else', 'return']
    
    
    def __init__(self, inFile):
        '''constructor for JackTokenizer open the
        inFile and get ready to tokenize it'''
        'Read one character at a time'
        self.c = ''
        self.inFile = self.__openFile(inFile)
    
    def __openFile(self, file):
        'Create a generator by opening the file'
        with open(file) as jackFile:
            for line in jackFile:
                for character in line:
                    yield character
    
    def hasMoreTokens(self):
        'True if there is more tokens to process'
        'Ignore white-space and if there is a charecter return True'
        while True:
            try:
                self.c = next(self.inFile)
            except:
                break
            
            'Ignore whitespace'
            if self.c.isspace():
                continue
            else:
                return True
        
        return False
    
    def advance(self):
        '''Get the next token from the input and
        make it the current token. Called when
        hasMoreTokens return True'''
        
        '''Need to use the current character, self.c and 
        -if self.c is an Jack Identifier, int or string, create a complete token
        by iterating over more cahracters until a jack symbol defined in jack
        grammer is hit or space character.
        -If self.c is a jack Symbol, return it.
        -If self.c is a keyword build it and then return it.'''
        
        
    
    def tokenType(self):
        '''Return the current token type;
        KEYWORD | SYMBOL | IDENTIFIER | 
        INT_CONST | STRING_CONST'''
        
    
    def Keyword(self):
        '''Returns the current token if 
        tokenType is KEYWORD'''
        
    
    def symbol(self):
        'Returns the character which is the current token'
        
    
    def identifier(self):
        'Returns the identifier which is the current token'
        
    
    def intVal(self):
        'Returns the integer value of the current token'
        
    
    def stringVal(self):
        '''Returns the String value of the current token
        without the double quotes'''
        
    