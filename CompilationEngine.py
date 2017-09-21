class CompilationEngine:
    '''Gets its input from JackTokenizer and 
    emits it parsed structure in output stream/file'''
    
    def __init__(self, inFile, outFile):
        '''Creates a new CompilationEngine with given
        input and output. The next routine called must
        be compileClass()'''
        
    
    def compileClass(self):
        'Compiles a complete class'
        
    
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
        
    