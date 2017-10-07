class SymbolTabel:
    """ Symbol Table is a class that stores an identifier 
        and all its properties like name, type, kind and runnign index
        in a python dictionary. For two scopes of Jack program
        one for class level and other for subroutine level.
        It also provides different methods to retrieve them """
    
    def __init__(self):
        """ Creates a new empty symbol table """
        
        
    
    def startSubroutine(self):
        """ Starts a new subroutine scope, ie.
            resets the subroutine's symbole table """
        
        
    
    def define(self, name, vartype, kind):
        """ Defines a new identifier of a given name, vartype and kind and
            assigns it a running index.
            STATIC and FIELD identifiers have a class scope, while 
            VAR and ARG identifiers have a subroutine scope """
        
        
    