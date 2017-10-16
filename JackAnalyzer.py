import CompilationEngine
import sys
import os

"""Main file to run the JackAnalyzer
    by using JackTokenizer and CompilationEngine"""
    
if __name__ == '__main__':
    # if it's a file, then create the CompilationEngine object and compile the whole class
    if os.path.isfile(sys.argv[1]):
        compiler = CompilationEngine.CompilationEngine(sys.argv[1], sys.argv[1][:-4] + 'xml')
        compiler.compileClass()
    # else if it's a directory, then cycle through all the files ending in .jack to compile all classes
    else:
        for fol, subFol, files in os.walk(sys.argv[1]):
            for file in files:
                if file.endswith('.jack'):
                    compiler = CompilationEngine.CompilationEngine(os.path.join(fol, file), os.path.join(fol, file[:-4] + 'xml'))
                    compiler.compileClass()