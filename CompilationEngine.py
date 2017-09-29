class CompilationEngine:
    """ Gets its input from JackTokenizer and 
        emits it parsed structure in output stream/file"""
    
    def __init__(self, inFile, outFile):
        """ Creates a new CompilationEngine with given
            input and output. The next routine called must
            be compileClass()"""
        
        # Create an object of JackTokenizer with the input file
        self.tokenizer = JackTokenizer(inFile)
        
        # Open a output file to write to
        self.out = open(outFile, 'w')
        
        self.currentToken = ''
        self.currentTokenType = ''
        
    
    #Change <, >, &, " to their respective character reference - &lt;, &gt;, &amp;, &quot;
    def __charRef(sym):
        if sym == '<':
            return '&lt;'
        elif sym == '>':
            return '&gt;'
        elif sym == '&':
            return '&amp;'
        elif sym == '"':
            return '&quot;'
        else:
            return sym
    
    def __advance(self):
        """ """
        
        if not tokenizer.hasMoreTokens():
            # error
            
        else:
            tokenizer.advance()
            self.currentTokenType = tokenizer.tokenType()
            
            if self.currentTokenType == 'KEYWORD':
                self.currentToken = tokenizer.keyword()
            
            elif self.currentTokenType == 'SYMBOL':
                self.currentToken = self.__charRef(tokenizer.symbol())
            
            elif self.currentTokenType == 'IDENTIFIER':
                self.currentToken = tokenizer.identifier()
            
            elif self.currentTokenType == 'INT_CONST':
                self.currentToken = tokenizer.intVal()
            
            elif self.currentTokenType == 'STRING_CONST':
                self.currentToken = tokenizer.stringVal()
    
    def __eat(self, string):
        """ """
        
        if self.currentToken != string:
            raise Exception('Expected ' + string + 'but found ' + self.currentToken)
        else:
            # advance the tokenizer
            self.__advance()
    
    def compileClass(self):
        'Compiles a complete class'
        
        # Writes <class> in output
        # check that there is class keyword as next token and output the fact
    
    def compileClassVarDec(self):
        'Compiles a static or a field declaration'
        
    
    def compileSubroutine(self):
        'Compiles a complete method, function or constructor'
        
    
    def CompileParameterList(self):
        'Compiles a parameter list(possibly empty) not including the enclosing ()'
        
    
    def compileVarDec(self):
        'compiles a variable declaration'
        
    
    def compileStatements(self):
        'Compiles series of statements, without {}'
        
    
    def compileDo(self):
        'Compiles a do statement'
        
    
    def compileLet(self):
        'Compiles a Let statement'
        
    
    def compileWhile(self):
        'Compiles a while statement'
        
    
    def compileReturn(self):
        'Compiles a return statement'
        
    
    def compileIf(self):
        'Compiles an If statement, possibly with a trailing else clause'
        
    
    def compileExpression(self):
        'Compiles an expression'
        
    
    def compileTerm(self):
        'Compiles a Term'
        
    
    def compileExpressionList(self):
        'Compiles(possibly empty) comma separated list of expressions'
        
    