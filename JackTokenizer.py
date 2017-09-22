class JackTokenizer:
    ''' class used to tokenize the input
    file(s)? into a stream of tokens, ignoring
    whitespace, comments etc.'''
    
    def __init__(self, inFile):
        '''constructor for JackTokenizer open the
        inFile and get ready to tokenize it'''
        'Read one character at a time'
        self.__openFile(inFile)
    
    def __openFile(self, file):
        'Create a generator by opening the file'
        with open(file) as jackFile:
            for line in jackFile:
                for character in line:
                    yield character
    
    def hasMoreTokens(self):
        'True if there is more tokens to process'
        'Ignore white-space and if there is a charecter return True'
    
    def advance(self):
        '''Get the next token from the input and
        make it the current token. Called when
        hasMoreTokens return True'''
        
    
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
        
    