class SymbolTable:
    """ Symbol Table is a class that stores an identifier 
        and all its properties like name, type, kind and runnign index
        in a python dictionary. For two scopes of Jack program
        one for class level and other for subroutine level.
        It also provides different methods to retrieve them """
    
    def __init__(self):
        """ Creates a new empty symbol table """
        
        self.classDict = {}
        
        self.static = 0
        self.field = 0
    
    def startSubroutine(self):
        """ Starts a new subroutine scope, ie.
            resets the subroutine's symbole table """
        
        self.subDict = {}
        
        self.arg = 0
        self.var = 0
    
    def define(self, name, vartype, kind):
        """ Defines a new identifier of a given name, vartype and kind and
            assigns it a running index.
            STATIC and FIELD identifiers have a class scope, while 
            VAR and ARG identifiers have a subroutine scope """
        
        if kind == 'STATIC':
            self.classDict[name] = [vartype, kind, self.static]
            self.static += 1
        elif kind == 'FIELD':
            self.classDict[name] = [vartype, kind, self.field]
            self.field += 1
        elif kind == 'ARG':
            self.subDict[name] = [vartype, kind, self.arg]
            self.arg += 1
        elif kind == 'VAR':
            self.subDict[name] = [vartype, kind, self.var]
            self.var += 1
        else:
            raise ValueError('Not a valid kind of identifier')
    
    def varCount(self, kind):
        """ Returns the number of variables of the given kind already defined
            in the current scope """
        
        if kind == 'STATIC':
            return self.static
        elif kind == 'FIELD':
            return self.field
        elif kind == 'ARG':
            return self.arg
        elif kind == 'VAR':
            return self.var
        else:
            raise ValueError('Not a valid kind of identifier')
    
    def kindOf(self, name):
        """ Returns the kind(STATIC, FIELD, VAR, ARG, NONE) of the named identifier
            in the current scope. 
            If the identifier is unknown in the current scope return NONE """
        
        if name in self.subDict:
            return self.subDict[name][1]
        elif name in self.classDict:
            return self.classDict[name][1]
        else:
            return 'NONE'
    
    def typeOf(self, name):
        """ Returns the type of the named variable in the current scope """
        
        if name in self.subDict:
            return self.subDict[name][0]
        elif name in self.classDict:
            return self.classDict[name][0]
        else:
            return 'NONE'
    
    def indexOf(self, name):
        """ Returns the index assigned to the named variable """
        
        if name in self.subDict:
            return self.subDict[name][2]
        elif name in self.classDict:
            return self.classDict[name][2]
        else:
            return -1