import JackTokenizer
import sys

class JackAnalyzer:
    '''Main class to run the JackAnalyzer
    by using JackTokenizerand CompilationEngine'''
    
    if __name__ == '__main__':
        tokenizer = JackTokenizer.JackTokenizer(sys.argv[0])
        with open(sys.argv[0][0:-4] + 'xml', 'w') as outfile:
            outfile.write('<Token>\n\n    ')
            
            while tokenizer.hasMoreTokens():
                tokenizer.advance()
                
                ttype = tokenizer.tokenType()
                
                if ttype == 'KEYWORD':
                    outfile.write('<keyword>' + tokenizer.keyword() + '<\keyword>\n    ')
                
                elif ttype == 'SYMBOL':
                    outfile.write('<symbol>' + tokenizer.symbol() + '<\symbol>\n    ')
                
                elif ttype == 'IDENTIFIER':
                    outfile.write('<identifier>' + tokenizer.identifier() + '<\identifier>\n    ')
                
                elif ttype == 'INT_CONST':
                    outfile.write('<intVal>' + tokenizer.intVal() + '<\intval>\n    ')
                
                elif ttype == 'STRING_CONST':
                    outfile.write('<stringVal>' + tokenizer.stringVal() + '<\stringVal>\n    ')
                
            outfile.write('\n<\Token>')
        outfile.close()
        
        
#!!! change tabs in the output file, so there is no need to add two \n
#!!! Change <, >, &, " to their respective character reference - &lt;, &gt;, &amp;, &quot;
#!!! Handle comments in jack file