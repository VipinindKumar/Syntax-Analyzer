import CompilationEngine
import sys

"""Main file to run the JackAnalyzer
    by using JackTokenizer and CompilationEngine"""
    
if __name__ == '__main__':
    compiler = CompilationEngine.CompilationEngine(sys.argv[1], sys.argv[1][:-5] + 'Compiled.xml')
    compiler.compileClass()