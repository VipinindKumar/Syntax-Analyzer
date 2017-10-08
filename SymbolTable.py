class SymbolTabel:
    """ Symbol Table is a class that stores an identifier 
        and all its properties like name, type, kind and runnign index
        in a python dictionary. For two scopes of Jack program
        one for class level and other for subroutine level.
        It also provides different methods to retrieve them """
    
    def __init__(self):
        """ Creates a new empty symbol table """
        
        self.classDict = {}
    
    def startSubroutine(self):
        """ Starts a new subroutine scope, ie.
            resets the subroutine's symbole table """
        
        
    
    def define(self, name, vartype, kind):
        """ Defines a new identifier of a given name, vartype and kind and
            assigns it a running index.
            STATIC and FIELD identifiers have a class scope, while 
            VAR and ARG identifiers have a subroutine scope """
        
        
    
    def varCount(self, kind):
        """ Returns the number of variables of the given kind already defined
            in the current scope """
        
        
    
    def kindOf(self, name):
        """ Returns the kind(STATIC, FIELD, VAR, ARG, NONE) of the named identifier
            in the current scope. 
            If the identifier is unknown in the current scope return NONE """
        
        
    
    def typeOf(self, name):
        """ Returns the type of the named variable in the current scope """
        
        
    
    def indexOf(self, name):
        """ Returns the index assigned to the named variable """
        
        