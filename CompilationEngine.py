import JackTokenizer

class CompilationEngine:
    """ Gets its input from JackTokenizer and 
        emits it parsed structure in output stream/file """
    
    def __init__(self, inFile, outFile):
        """ Creates a new CompilationEngine with given
            input and output. The next routine called must
            be compileClass() """
        
        # Create an object of JackTokenizer with the input file
        self.tokenizer = JackTokenizer.JackTokenizer(inFile)
        
        # Open a output file to write to
        self.out = open(outFile, 'w')
        
        self.currentToken = ''
        self.currentTokenType = ''
        self.tabs = 0
        
    
    def __charRef(self, sym):
        """ Change <, >, &, " to their respective
            character reference - &lt;, &gt;, &amp;, &quot; """
        
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
        """ Advance the tokenizer and store the 
            token and it's respective type """
        
        if not self.tokenizer.hasMoreTokens():
            # error
            raise Exception('Unexpected end of file')
        else:
            self.tokenizer.advance()
            self.currentTokenType = self.tokenizer.tokenType()
            
            if self.currentTokenType == 'KEYWORD':
                self.currentToken = self.tokenizer.keyword()
            
            elif self.currentTokenType == 'SYMBOL':
                self.currentToken = self.tokenizer.symbol()
            
            elif self.currentTokenType == 'IDENTIFIER':
                self.currentToken = self.tokenizer.identifier()
            
            elif self.currentTokenType == 'INT_CONST':
                self.currentToken = self.tokenizer.intVal()
            
            elif self.currentTokenType == 'STRING_CONST':
                self.currentToken = self.tokenizer.stringVal()
    
    def __printTabs(self):
        """ Print the appropriate numbers of tabs, before the tag """
        for i in range(self.tabs):
            self.out.write('\t')
    
    def __printTag(self):
        """ Print the currentToken as an appropriate tag in xml file
            using currentToken and currentTokenType """
        
        self.__printTabs()
        
        # Print the tag and its value in the xml file
        self.out.write('<' + self.currentTokenType + '> ' + self.currentToken + ' <' + self.currentTokenType + '>\n')
        
        self.__advance() # advance the tokenizer
    
    def __eat(self, stringList):
        """ Make sure the string equals the currentToken value
            and if it does it advances the tokenizer
            else an exception is thrown"""
        
        if self.currentToken in stringList:
            raise Exception('Expected ' + self.currentToken + 'but found ' + self.currentToken)
        else:
            self.__printTag()
    
    def __varDec(self):
        """ Compilea part of class variable declaration and 
            variable declaration 
            : type varName (',' varName)* ';' """
        
        # type: int | char | boolean | className
        # can just use self.__printTag()
        try:
            self.__eat(['int', 'char', 'boolean'])
        except:
            self.__printTag()
        
        self.__printTag() # varName identifier
        
        # (',' varName)*
        while self.currentToken != ';':
            self.__eat(',')
            self.__printTag() # varName identifier
        
        self.__eat(';') # ';'
    
    
    
    def compileClass(self):
        """ Compiles a complete class 
            Class: 'class' className '{' classVarDec* subroutineDec* '}' """
        
        self.__printTabs()
        self.out.write('<class>\n') # Start <class> tag in output
        self.tabs += 1 # Add single Indentation to xml file tags from here
        
        self.__eat(['class']) # check that there is class keyword as next token and output the fact
        self.__printTag() # Handles className identifier
        self.__eat(['{']) # '{'
        
        # 0 or more class variable declarations
        while self.currentToken not in ['constructor', 'method', 'function']:
            self.compileClassVarDec()
        
        # 0 or more subroutines
        while self.currentToken != '}':
            self.compileSubroutine()
        
        self.__eat(['}']) # '}'
        
        self.tabs -= 1 # Remove single indentation from the tags
        self.__printTabs()
        self.out.write('</class>')
    
    def compileClassVarDec(self):
        """ Compiles a static or a field declaration 
            ClassVarDec: ('static' | 'field') type varName (',' varName)* ';' """
        
        self.__printTabs()
        self.out.write('<ClassVarDec>\n')
        
        self.tabs += 1 # increase indentation
        
        self.__eat(['static', 'field']) # (static | field)
        
        self.__varDec() # type varName (',' varName)* ';'
        
        # Remove single indentation from the tags
        self.tabs -= 1
        
        self.__printTabs()
        self.out.write('</ClassVarDec>\n')
    
    def compileSubroutine(self):
        """ Compiles a complete method, function or constructor 
            Subroutine: ('constructor' | 'method' | 'function')
                        ('void' | type) subroutineName '(' parameterList ')'
                        subroutineBody """
        
        self.__printTabs()
        self.out.write('<SubroutineDec>\n')
        self.tabs += 1 # increase indentation
        
        self.__eat(['constructor', 'function', 'method']) # constructor | function | method
        
        # void | type: int | char | boolean | className
        # can just use self.__printTag()
        try:
            self.__eat(['void', 'int', 'char', 'boolean'])
        except:
            self.__printTag()
        
        self.__printTag() # subroutineName identifier
        
        self.__eat('(') # '('
        
        self.compileParameterList()
        
        self.__eat(')') # ')'
        
        # subroutineBody
        self.__eat('{')
        
        # (varDec)*
        while self.currentToken not in ['let', 'if', 'do', 'while', 'return']:
            self.compileVarDec()
        
        # statements
        self.compileStatements()
        
        self.__eat('}')
        
        # Remove single indentation from the tags
        self.tabs -= 1
        self.__printTabs()
        self.out.write('</SubroutineDec>\n')
    
    def compileParameterList(self):
        """ Compiles a parameter list(possibly empty) not including the enclosing ()
            ParameterList: ((type varName) (',' type varName)*)? """
        
        self.__printTabs()
        self.out.write('<ParameterList>\n')
        self.tabs += 1 # add indentation
        
        if self.currentToken != ')':
            # type: int | char | boolean | className
            try:
                self.__eat(['int', 'char', 'boolean'])
            except:
                self.__printTag()
            
            self.__printTag() # varName identifier
            
            while self.currentToken != ')':
                self.__eat(',')
                # type: int | char | boolean | className
                try:
                    self.__eat(['int', 'char', 'boolean'])
                except:
                    self.__printTag()
                
                self.__printTag() # varName identifier
        
        self.tabs -= 1 # remove indentation
        self.__printTabs()
        self.out.write('</ParameterList>\n')
    
    def compileVarDec(self):
        """ compiles a variable declaration 
            varDec: var type varName (',' varName)* ';' """
        
        self.__printTabs()
        self.out.write('<VarDec>\n')
        self.tabs += 1 # increase indentation
        
        self.__eat(['var']) # var
        
        self.__varDec() # type varName (',' varName)* ';'
        
        # Remove single indentation from the tags
        self.tabs -= 1
        self.__printTabs()
        self.out.write('</VarDec>\n')
    
    def compileStatements(self):
        """ Compiles series of statements, without {} 
            statements: statement* 
            statement: letStatement | doStatement | ifStatement | 
                       whileStatement | returnStatement """
        
        self.out.write('<Statements>\n')
        self.tabs += 1
        
        while True:
            if self.currentToken == 'do':
                self.compileDo()
            elif self.currentToken == 'let':
                self.compileLet()
            elif self.currentToken == 'while':
                self.compileWhile()
            elif self.currentToken == 'return':
                self.compileReturn()
            elif self.currentToken == 'if':
                self.compileIf()
            else:
                break
        
        self.tabs -= 1
        self.out.write('</Statements>\n')
    
    def __subroutineCall(self):
        """ Compiles the subroutine call part of the program
            SubroutineCall: subroutineName '(' expressionList ')' | (className | varName) '.' 
                            subroutineName '(' expressionList ')' """
        
        self.__printTag() # subroutineName | (className | varName)
        
        if self.currentToken == '.':
            self.__printTag() # subroutineName
        
        self.__eat('(') # '('
        self.compileExpressionList()
        self.__eat(')') # ')'
    
    def compileDo(self):
        """ Compiles a do statement 
            doStatment: 'do' subroutineCall ';' """
        
        self.out.write('<DoStatement>\n')
        self.tabs += 1
        
        self.__eat('do')
        
        # subrutineCall
        self.__subroutineCall()
        
        self.__eat(';') # ';'
        
        self.tabs -= 1
        self.out.write('</DoStatement>\n')
    
    def compileLet(self):
        """ Compiles a Let statement 
        LetStatement: 'let' varName ('[' expression ']')? '=' expression ';' """
        
        self.out.write('<LetStatement>\n')
        self.tabs += 1
        
        self.__eat('let')
        self.__printTag()
        
        if self.currentToken == '[':
            self.__eat('[')
            self.compileExpression()
            self.__eat(']')
        
        self.__eat('=')
        
        self.compileExpression()
        
        self.__eat(';')
        
        self.tabs -= 1
        self.out.write('</LetStatement>\n')
    
    def compileWhile(self):
        """ Compiles a while statement 
            whileStatement: 'while' '(' expression ')' '{' statements '}' """
        
        self.out.write('<WhileStatement>\n')
        self.tabs += 1
        
        self.__eat('while')
        self.__eat('(')
        
        self.compileExpression()
        
        self.__eat(')')
        self.__eat('{')
        
        self.compileStatements()
        
        self.__eat('}')
        
        self.tabs -= 1
        self.out.write('</WhileStatement>\n')
    
    def compileReturn(self):
        """ Compiles a return statement
            ReturnStatement: 'return' (expression)? ';' """
        
        self.out.write('<ReturnStatement>\n')
        self.tabs += 1
        
        self.__eat('return')
        
        if self.currentToken != ';':
            self.compileExpression()
        
        self.__eat(';')
        
        self.tabs -= 1
        self.out.write('</ReturnStatement>\n')
    
    def compileIf(self):
        """ Compiles an If statement, possibly with a trailing else clause
            IfStatements: 'if' '(' expression ')' '{' statements '}'
                          ('else' '{' statements '}')? """
        
        self.out.write('<IfStatment>\n')
        self.tabs += 1
        
        self.__eat('if')
        self.__eat('(')
        
        self.compileExpression()
        
        self.__eat(')')
        self.__eat('{')
        
        self.compileStatements()
        
        self.__eat('}')
        
        if self.currentToken == 'else':
            self.__eat('else')
            self.__eat('{')
            
            self.compileStatements()
            
            self.__eat('}')
        
        self.tabs -= 1
        self.out.write('</IfStatement>\n')
    
    # There could be a problem with no tabs in self.out.write commands
    
    def compileExpression(self):
        """ Compiles an expression """
        
    
    def compileTerm(self):
        """ Compiles a Term """
        
    
    def compileExpressionList(self):
        """ Compiles(possibly empty) comma separated list of expressions """
        
    