
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
