
from lexicalAnalyzer import generateOuput, classifyToken, breakWords
from func_file_1 import syntaxAnalyzer
from Semantic_Analyzer22 import semanticAnalyzer, report

with open("D:\\6th Semester\\Compiler Construction\\compiler\\source_file.txt", "r") as inputfile:
    input_text = inputfile.read()
    

# generatedTokens = breakWords(input_text)
# classifiedTokens = classifyToken(generatedTokens)
# output_text = generateOuput(classifiedTokens)

tokenList = classifyToken(breakWords(input_text))

'''
with open("output_tokens_file.txt", "w") as outputfile:
    outputfile.write(generateOuput(tokenList))
'''   

synError, check = syntaxAnalyzer(tokenList)
if (check):
    print("\nSyntax Result :")
    print("\t***  INPUT COMPLETELY PARSED WITH COMPLETE TREE  ***\n")
    x = semanticAnalyzer(tokenList)
    print("\nSemantic Result :")
    print("\t***  ", str(x).upper(), "  ***\n")

    with open("D:\\6th Semester\\Compiler Construction\\compiler\\output_tokens_file.txt", "w") as outputfile:
        outputfile.write(generateOuput(tokenList))
   
    with open("D:\\6th Semester\\Compiler Construction\\compiler\\output_semantic_file.txt", "w") as outputfile:
        outputfile.write(report())

else:
    print("\n\t***  SYNTAX ERROR  ***\n")
    print("ERROR:",synError)

    with open("D:\\6th Semester\\Compiler Construction\\compiler\\output_tokens_file.txt", "w") as outputfile:
        outputfile.write(synError)
        outputfile.write(generateOuput(tokenList))
