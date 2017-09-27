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
        
        # Read one character at a time, ignoring comments and empty lines
        self.inFile = self.__openFile(inFile)
        
        try:
            self.line = next(self.inFile)
        except:
            raise Exception('Empty input file')
        
        self.token = ''
        self.tType = ''
        self.i = 0
    
    def __openFile(self, file):
        incomment = False
        # Create a generator by opening the file
        with open(file) as jackFile:
            for line in jackFile:
                
                # Ignore Comments and empty lines
                # Check empty lines
                if not line:
                    continue
                
                # Check for Multi line comments
                elif line.startswith('/*') or incomment:
                    # Read next line till multi line comments ends
                    if '*/' not in line:
                        incomment = True
                        continue
                    else:
                        incomment = False
                        continue
                    
                # Check for end of line comments, which are on complete line
                elif line.startswith('//'):
                    continue
                
                for character in line:
                    yield character
    
    def hasMoreTokens(self):
        # True if there is more tokens to process
        while True:
            # Ignore Comments and empty lines
            if not self.line:
                pass
            elif self.line.startswith('//'):
                pass
            elif self.line.startswith('/*'):
                # Read next line till multi line comments ends
                while True:
                    try:
                        self.line = next(self.inFile)
                    except:
                        return False
                    
                    if '*/' in self.line:
                        break
            else:
                break
            
            # Read next line
            try:
                self.line = next(self.inFile)
                break
            except:
                return False
            
        return True
    
    def advance(self):
        ''' Get the next token from the input and
        make it the current token. Called when
        hasMoreTokens return True'''
        
        ''' Need to use the current character, self.c and 
        -if self.c is an Jack Identifier, int or string, create a complete token
        by iterating over more cahracters until a jack symbol defined in jack
        grammer is hit or space character.
        -If self.c is a jack Symbol, return it.
        -If self.c is a keyword build it and then return it.'''
        
        # If it's a comment
        if self.c == '/':
            self.token = self.c
            
            #!!! Handle EOF later
            #!!! and use try and except
            
            # Check the next character
            self.c = next(self.inFile)
            # If // type of comment
            if self.c =='/':
                while self.c != '\n':
                    self.c = next(self.inFile)
                
                self.advance()
            
            # If /* */ type of comment
            elif self.c == '*':
                
            
        # If the c value is in symbols
        elif self.c in JackTokenizer.symbols:
            self.token = self.c
            self.c = next(self.inFile)
        
        else:
            # Keep building the token until a separator(a symbol or space/s) is read
            while self.c != ' ' and self.c not in JackTokenizer.symbols:
                self.token += self.c
                self.c = next(self.inFile)
    
    def tokenType(self):
        ''' Return the current token type;
        KEYWORD | SYMBOL | IDENTIFIER | 
        INT_CONST | STRING_CONST'''
        
        # SYMBOL
        if self.token in JackTokenizer.symbols:
            self.tType = 'SYMBOL'
            return self.tType
        
        # KEYWORD
        elif self.token in JackTokenizer.keywords:
            self.tType = 'KEYWORD'
            return self.tType
            
        # STRING_CONST
        elif self.token[0] == "\"" and self.token[-1] == "\"":
            self.tType = 'STRING_CONST'
            return self.tType
        
        # INT_CONST
        elif self.token.isdigit():
            self.tType = 'INT_CONST'
            return self.tType
        
        # IDENTIFIER
        else:
            self.tType = 'IDENTIFIER'
            return self.tType
    
    def keyword(self):
        ''' Returns the current token if 
        tokenType is KEYWORD'''
        if self.tType != 'KEYWORD':
            raise ValueError('not a keyword')
        else:
            return self.token
    
    def symbol(self):
        # Returns the character which is the current token
        if self.tType != 'SYMBOL':
            raise ValueError('not a symbol')
        else:
            return self.token
    
    def identifier(self):
        # Returns the identifier which is the current token
        if self.tType != 'IDENTIFIER':
            raise ValueError('not a identifier')
        else:
            return self.token
    
    def intVal(self):
        # Returns the integer value of the current token
        if self.tType != 'INT_CONST':
            raise ValueError('not a int const')
        else:
            return self.token
    
    def stringVal(self):
        ''' Returns the String value of the current token
        without the double quotes'''
        if self.tType != 'STRING_CONST':
            raise ValueError('not a string const')
        else:
            return self.token[1:-1]
    