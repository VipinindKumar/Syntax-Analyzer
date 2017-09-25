import JackTokenizer
import sys

class JackAnalyzer:
    '''Main class to run the JackAnalyzer
    by using JackTokenizerand CompilationEngine'''
    
    if __name__ == '__main__':
        tokenizer = JackTokenizer.JackTokenizer(sys.argv[0])
        with open(sys.argv[0][0:-4] + 'xml', 'w') as outfile:
            outfile.write('<Token>\n')
            
            while tokenizer.hasMoreTokens():
                tokenizer.advance()
                
                ttype = tokenizer.tokenType()
                
                if ttype == 'KEYWORD':
                    outfile.write('    <keyword> ' + tokenizer.keyword() + ' <\keyword>\n')
                
                elif ttype == 'SYMBOL':
                    outfile.write('    <symbol> ' + tokenizer.symbol() + ' <\symbol>\n')
                
                elif ttype == 'IDENTIFIER':
                    outfile.write('    <identifier> ' + tokenizer.identifier() + ' <\identifier>\n')
                
                elif ttype == 'INT_CONST':
                    outfile.write('    <intConstant> ' + tokenizer.intVal() + ' <\intConstant>\n')
                
                elif ttype == 'STRING_CONST':
                    outfile.write('    <stringConstant> ' + tokenizer.stringVal() + ' <\stringConstant>\n')
                
            outfile.write('<\Token>')
        outfile.close()
        

#!!! Change <, >, &, " to their respective character reference - &lt;, &gt;, &amp;, &quot;
#!!! Handle comments in jack file