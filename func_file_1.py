
# SYNTAX ANALYZER:-

i = 0
tokenList = []
error = 0
synError = ""


def syntaxAnalyzer(tokens):
    global i, tokenList, error, synError
    i = 0
    error = 0
    tokenList = tokens
    result = start()
    if (not result):
        synError += "\nTOKEN UNEXPECTED: \n\tLine number : " + str(tokenList[error].line) + "\n\tType : " + tokenList[error].type + \
             "\n\tValue :\t" + tokenList[error].value + "\n\tToken :\t" + str(error) + "\n\n\n"
    return synError, result


def syntaxError():
    global i, tokenList, error
    if (i > error):
        error = i
    return False

try: 
    def start():
        global i, tokenList
        if start_body():
            print("MMM")            
            if tokenList[i].type == "MAIN":
                
                i += 1  # Consume "main"
                if tokenList[i].type == "(":
                    i += 1  # Consume "("
                    if tokenList[i].type == ")":
                        i += 1  # Consume ")"
                        if tokenList[i].type == "{":
                            i += 1  # Consume "{"
                            if main_body():
                                if tokenList[i].type == "}":
                                    return True
        elif tokenList[i].type == "$":
            return True
        return syntaxError()
        
    
    def start_body():
        global i, tokenList
        if dec() or func_st() or struct_dec() or class_dec() or struct_obj() or obj_decl():
            return start_body()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return start_body()
        elif tokenList[i].type == "MAIN":
            return True 
        return syntaxError()  # Return True for epsilon    
        
    
    def main_body():
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_dec() or class_dec() or struct_obj() or obj_decl() or assign_st() or return_() or break_() or continue_():
            return main_body()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return main_body()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()  # Return True for epsilon 
        
# Declaration and Initialization:

    def dec():
        global i, tokenList
        print("RRRRRRRRRRRRRR")
        if DT1():
            if (tokenList[i].type == "ID"):
                print("aaaaaaaaaaaaa")
                i += 1
                if init():
                    print("a[2]")
                    if (tokenList[i].type == ";"):
                        print(";")
                        i+=1
                        print("::::::::::::::::::::::::::")
                        return True
                    # print("yyy")
                    # else:
                    #     return syntaxError()
        #print("ghghguhu")
        return syntaxError()
    
    def DT1():
        global i, tokenList
        if (tokenList[i].type == "CONSTANT"):
            i += 1
            if DT():
                return True
        elif (DT()):
            return True
    
        return syntaxError()
    
    def dec11():
        global i, tokenList
        if (DT1()):
            print("hello")
            if tokenList[i].type == "ID":
                print("ghgh")
                i += 1
                return init22()
        return syntaxError()
    
    def init22():
        global i, tokenList
        if tokenList[i].type == "AO":
            i += 1
            return OE()
        elif tokenList[i].type == "[":
            i += 1
            return init33()
        elif tokenList[i].type == "," or tokenList[i].type == ")":
            print("hjkhjk")
            return True
        return syntaxError()
    
    def init33():
        global i, tokenList
        if OE():
            if tokenList[i].type == "]":
                i += 1
                return Arr()
        elif tokenList[i].type == "]":
            i += 1
            return Arr()
        return syntaxError()    
    
    def DT():
        global i, tokenList
        #if (tokenList[i].type == "int" or tokenList[i].type == "float" or tokenList[i].type == "char" or tokenList[i].type == "string" or tokenList[i].type == "bool"):
        if (tokenList[i].type == "DT"):
            print("int")
            i += 1
            return True
        return syntaxError()
    
    def const():
        global i, tokenList
        if (tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR"):
            i += 1
            return True
        return syntaxError()  
    
    def SA():
        global i, tokenList
        if (tokenList[i].type == "AO"):
            i += 1
            return True
        return syntaxError()
    
    def or_():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            return True
        return syntaxError()
    
    def init():
        global i, tokenList
        if (tokenList[i].type == "AO"):
            print("AOinit")
            i += 1
            if (init5()):
                print("init5")
                return True
        elif (tokenList[i].type == "["):
            i += 1
            print("[")
            return init1()
        elif (tokenList[i].type == ","):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                print("IIIIIIIIII")
                return init()
        elif (tokenList[i].type == ";"):
            print("QQQQQQQQQQ")
            return True
        return syntaxError()
    
    def init6():
        global i, tokenList
        if (tokenList[i].type == "AO"):
            print("=")
            i += 1
            if (init7()):
                return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def init5():
        global i, tokenList
        if (OE()):
            print(init5())
            return True
        elif(take()):
            return True
        return syntaxError()
    
    def init7():
        global i, tokenList
        if (tokenList[i].type == "{"):
            print("{")
            i += 1
            if (init2()):
                if (tokenList[i].type == "}"):
                    i += 1
                    #if (init2()):
                    return True
        return syntaxError()
    
    def init2():
        global i, tokenList
        if (tokenList[i].type == ","):
            print("{2,")
            i += 1
            if (init8()):
                print("{")
                return True
        elif (OE() and init2()):
            return True
        elif (tokenList[i].type == "{"):
            print("{")
            i += 1
            if (OE() and init2()):
                print("A")
                if (tokenList[i].type == "}"):
                    i += 1
                    if (init2()):
                        return True
        elif (tokenList[i].type == "}"):
            i += 1
            #return True
            return init2()
        elif (tokenList[i].type == "}" or tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def init8():
        global i, tokenList
        if (OE() and init2()):
            return True
        elif (tokenList[i].type == "{"):
            i += 1
            if (OE() and init2()):
                if (tokenList[i].type == "}"):
                    return True
        return syntaxError()
    
    def init1():
        global i, tokenList
        if (OE()):
            print("2")
            if (tokenList[i].type == "]"):
                print("]")
                i += 1
                if (Arr() and init6()):
                    print("Arr and init6")
                    return True
        elif (tokenList[i].type == "]"):
            print("Init1-follow")
            i += 1
            if (Arr() and init16()):
                return True
        return syntaxError()
  

    def init16():
        global i, tokenList
        if SA():
            return init7()
        return syntaxError()
    

    def struct_obj11():
        global i, tokenList
        if tokenList[i].type == "ST":
            i += 1
            if tokenList[i].type == "ID":
                i += 1
                if tokenList[i].type == "ID":
                    i += 1
                    return listA11()
        return syntaxError()
    
    def listA11():
        global i, tokenList
        if tokenList[i].type == "[":
            i += 1
            if OE():
                if tokenList[i].type == ']':
                    i += 1
                    return Arr()
        elif (tokenList[i].type == "," or tokenList[i].type == ")"):
            return True
        return syntaxError()
    

    def param():
        global i, tokenList
        if dec11():
            print("look")
            return param1()
        elif struct_obj11():
            return param1()
        elif obj_decl():
            return param1()
        elif tokenList[i].type == ")":
            return True
        return syntaxError()
    
    
    def param2():
        global i, tokenList
        if (dec11()):
            print("pppp")
            return True
        elif struct_obj11():
            return True
        elif obj_decl():
            return True
        return syntaxError()
    



# assign_st  
    
    def assign_st():                     
        global i, tokenList
        if (tokenList[i].type=="ASSIGN"):
            i+=1
            if(D2() and X2() and list_()):
                if(tokenList[i].type==";"):
                    print(";assign")
                    i+=1
                    return True
        return syntaxError()     

    def D2():
        global i, tokenList
        if(tokenList[i].type=="Inc_Dec"):
            i+=1
            if(inc_dec_op()):
                return p()
        elif(tokenList[i].type=="THIS"):
            i += 1
            return True
        elif (tokenList[i].type=="ID" or tokenList[i].type=="("):
            print("NULL(D2)")
            return True
        return syntaxError()

    def X2():
        global i, tokenList
        if(tokenList[i].type=="ID"):
            print("a")
            i+=1
            return dot22() 
        elif(tokenList[i].type=="("):
            i+=1
            if(tokenList[i].type=="ID"):
                i+=1
                if(dot22()):
                    if(tokenList[i].type==")"):
                        i+=1
                        return True
        elif tokenList[i].type == "AO":
            return True
        return syntaxError()
   
    def dot22():
        global i, tokenList
        if tokenList[i].type == ".":
            i += 1
            if tokenList[i].type == "ID":
                i += 1
                return dot22()
        elif tokenList[i].type == "(":
            i += 1
            if para():
                if tokenList[i].type == ")":
                    i += 1
                    if tokenList[i].type == ".":
                        i += 1
                        if tokenList[i].type == "ID":
                            i += 1
                            return dot22()
        elif tokenList[i].type == "[":
            if OE():
                if tokenList[i].type == "]":
                    i += 1
                    return dot22()
        elif tokenList[i].type == ")" or tokenList[i].type == "AO":
            return True
        return syntaxError()                    
            
    
    def list_():
        global i, tokenList
        if (tokenList[i].type == "AO"):    # AO or AO_D(+=,-=,...)
            print("=")
            i += 1
            if(SSA()):
                #print("5")
                return True
        elif tokenList[i].type == ";":
            return True
        return syntaxError()
    
    def p1():
        global i, tokenList
        if (tokenList[i].type == "THIS"):
            i += 1
            if (tokenList[i].type == "."):
                return True
        return syntaxError()
    
    def take():
        global i, tokenList
        if(tokenList[i].type=="TAKE"):
            return IndexA
        return syntaxError() 
    
    def SSA():              # issue 
        global i, tokenList
        if(OE()):
            #print("8")
            return True
        elif(tokenList[i].type=="TAKE"):
            return take()
        return syntaxError()
    
    def IndexA():
        global i, tokenList
        if(tokenList[i].type=="(" and const()):
            if (tokenList[i].type==")"):
                i+=1
                if(tokenList[i].type==";"):
                    i+=1
                    return True
        return syntaxError()
    
    
    
  
    

    
# Inc_Dec_obj_call:

    def Inc_Dec_obj_call():
        global i, tokenList
        if (tokenList[i].type == "Inc_Dec"):
            print("I/C")
            i += 1
            if (B1()):
                print("B1")
                return True
        
        return syntaxError()
    
    def B1():
        global i, tokenList
        if (tokenList[i].type == "ID"):
            print("i")
            i += 1
            if (dot() and inc_dec_op()):
                print("Inc_Dec i++")
                return True
        elif (tokenList[i].type == "Inc/Dec"):
            print("VVV")
            i += 1
            return X11()
        elif(tokenList[i].type == "(" or tokenList[i].type == "THIS"):
            i += 1
            if (B2() and inc_dec_op()):
                return True
        return syntaxError()
        
    
    def B2():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                if (dot()):
                    if (tokenList[i].type == ")"):
                        return True
        elif (tokenList[i].type == "THIS"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return dot()
        return syntaxError()
    
    def X11():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                if (dot()):
                    if (tokenList[i].type == ")"):
                        return True
        elif (tokenList[i].type == "ID"):
                i += 1
                print("HAM")
                return dot()
        return syntaxError()
    
    def para():
        global i, tokenList
        #if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (OE() and para1()):
            return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()
    
    def para1():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            if (OE() and para1()):
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()
    

    def dot():                                        
        global i, tokenList
        if (tokenList[i].type == "."):
            print(".")
            i += 1
            if (tokenList[i].type == "ID"):
                print("fn")
                i += 1
                return dot()
        elif (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return dot()
        elif (tokenList[i].type == "("):
            print("(")
            i += 1
            if (para()):
                if (tokenList[i].type == ")"):
                    print(")")
                    i += 1
                    return dot()       
        elif (tokenList[i].type == ")"  or tokenList[i].type == "Inc/Dec" or tokenList[i].type == ";" or tokenList[i].type == "]" or tokenList[i].type == "{"  or tokenList[i].type == "}" or  tokenList[i].type == "," or tokenList[i].type == "AND" or tokenList[i].type == "OR" or tokenList[i].type == "PM" or tokenList[i].type == "MDM" or tokenList[i].type == "R_OP"):
            print("NULL(dot)")
            return True
        return syntaxError()
 
   
  
# object_call:        
    
    def obj_call():
        global i, tokenList
        #if (tokenList[i].type == "ID" or tokenList[i].type == "(" or tokenList[i].type == "this"):
        if B_():
            print("B_")
            return True
        return syntaxError()
    
    def B_():
        global i, tokenList
        if (tokenList[i].type == "ID"):
            print("i")
            i += 1
            return dot()
        elif (tokenList[i].type == "THIS"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return dot()
        return syntaxError()
    
# struct_obj:

    def struct_obj():
        global i, tokenList
        if (tokenList[i].type == "ST"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                if (tokenList[i].type == "ID"):
                    i += 1
                    if (list_A() and initA()):
                        if (tokenList[i].type == ";"):
                            return True
                    
        return syntaxError()
            
    def list_A():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return list_A
        elif (tokenList[i].type == "["):
            i += 1
            if (OE()):
                if (tokenList[i].type == "]"):
                    i += 1
                    return list_A
        elif (tokenList[i].type == "AO" or tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def initA():
        global i, tokenList
        if (tokenList[i].type == "="):
            i += 1
            if (tokenList[i].type == "{"):
                i += 1
                if (OE() and list_B()):
                    if (tokenList[i].type == "}"):
                        return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()
    
    def list_B():
        global i, tokenList
        if (tokenList[i].type == ","):
            i += 1
            if (OE() and list_B()):
                return True
        elif (tokenList[i].type == "}"):
            return True
        return syntaxError()
 
 
    
# if-else: 
    
    def if_else():
        global i, tokenList
        if tokenList[i].type == "IF":
            i += 1
            if if2():
                return True
        return syntaxError()

    def if2():
        global i, tokenList
        if tokenList[i].type == "(":
            i += 1
            if cond():
                print("cond")
                if tokenList[i].type == ")":
                    i += 1
                    if (if_body() and elif_()):
                        return True
        return syntaxError()

    def elif_():
        global i, tokenList
        if tokenList[i].type == "ELIF":
            i += 1
            if if2():
                return True
        elif tokenList[i].type == "ELSE":
            i += 1
            if tokenList[i].type == ":":
                i += 1
                if if_body():
                    return True
        elif tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CONST" or tokenList[i].type == "STR" or tokenList[i].type == "BOOL" or tokenList[i].type == "CHAR" or tokenList[i].type == "DEF" or tokenList[i].type == "VIRTUAL" or tokenList[i].type == "THROW" or tokenList[i].type == "ACCESS MODIFIER" or tokenList[i].type == "IF" or tokenList[i].type == "BREAK" or tokenList[i].type == "CONTINUE" or tokenList[i].type == "THIS" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "DT" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "ID" or tokenList[i].type == "RETURN" or tokenList[i].type == "CHECK" or tokenList[i].type == "FOR" or tokenList[i].type == "PRINT" or tokenList[i].type == "ST" or tokenList[i].type == "OBJ" or tokenList[i].type == "ASSIGN" or tokenList[i].type == "STRUCT" or tokenList[i].type == "CLASS" or tokenList[i].type == "}" or tokenList[i].type == "MAIN" or tokenList[i].type == "~" or tokenList[i].type == "ELIF" or tokenList[i].type == "ELSE" or tokenList[i].type == "CONSTRUCT":
            return True
        return syntaxError()

    def cond():
        global i, tokenList
        if OE():
            print("OE-")
            return True
        return syntaxError()

    def if_body():
        global i, tokenList
        if tokenList[i].type == "{":
            i += 1
            if if_SST():
               if tokenList[i].type == "}":
                   i += 1 
                   return True
        elif tokenList[i].type == ";":
            i += 1
            return True
        return syntaxError()
    
    def if_SST():
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or OE() or return_() or break_() or continue_() or throw():
            return if_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return if_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()  # Return True for epsilon
    
# struct_dec:

    def struct_dec():
        global i, tokenList
        if (tokenList[i].type == "STRUCT"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return struct_body()
        return syntaxError()
    
    def struct_body():
        global i, tokenList
        if (tokenList[i].type == "{"):
            i += 1
            if (struct_sst()):
                if (tokenList[i].type == "}"):
                    i += 1
                    return True
        elif (tokenList[i].type == ";"):
            i += 1
            return True
        return syntaxError()
    
    def struct_sst():
    # Check if there are any statements in the struct_SST
        if (dec() or assign_st() or struct_obj() or obj_decl() or func_st() or print_()):   # direct function given without non-terminal first-set
        # After processing a statement, continue with struct_SST
            return struct_sst()
        elif (tokenList[i].type == "}"):
            return True
        # If no statements match, it's an epsilon (empty) production
        return syntaxError()
    
# break

    def break_():
        global i, tokenList
        if (tokenList[i].type == "BREAK"):
            i += 1  
            if (tokenList[i].type == ";"):
                i += 1 
                return True
        return syntaxError()
    
# continue

    def continue_():
        global i, tokenList
        if (tokenList[i].type == "CONTINUE"):
            i += 1  
            if (tokenList[i].type == ";"):
                i += 1  
                return True
        return syntaxError()
    
# return
 
    def return_():
        global i, tokenList
        if (tokenList[i].type == "RETURN"):
            i += 1  
            if (index1()): 
                if (tokenList[i].type == ";"):
                    i += 1  
                    return True  
        return syntaxError()
        
    def index1():
        global i, tokenList
        if (OE()):
            return True
        elif (tokenList[i].type == ";"):
            return True  
        return syntaxError()

# throw

    def throw():
        global i, tokenList
        if (tokenList[i].type == "THROW"):
            i += 1 
            if index():
                return True
        return syntaxError()
    
# print_

    def print_():
        global i, tokenList
        if (tokenList[i].type == "PRINT"):
            i += 1  
            if index():
                if (tokenList[i].type == ";"):
                    i += 1  
                    return True
        return syntaxError()

    def index():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1 
            if (OE()):
                if (tokenList[i].type == ")"):
                    i += 1 
                    return True  
        return syntaxError()
    
# inc_dec

    def inc_dec_op():
        global i, tokenList
        if tokenList[i].type == "Inc/Dec":
            i += 1  # Consume the "++" or "--"
            return True
        return syntaxError()

    def Arr():
        global i, tokenList
        if tokenList[i].type == "[":
            i += 1  # Consume the opening square bracket "["
            print("ARR1")
            if OE():
                if tokenList[i].type == "]":
                    i += 1  # Consume the closing square bracket "]"
                    return Arr()  # Recursively check for more arrays
        elif tokenList[i].type == "AO" or tokenList[i].type == ";" or tokenList[i].type == "Inc/Dec" or tokenList[i].type == "," or tokenList[i].type == ")":
            print("ARR")
            return True 
        return syntaxError()  # Return True for epsilon

    def IDC():
        global i, tokenList
        if p():
            if tokenList[i].type == "ID":
                i += 1  # Consume the identifier (ID)
                if Arr():
                    if inc_dec_op():
                        return True
        elif inc_dec_op():
            if tokenList[i].type == "ID":
                i += 1  # Consume the identifier (ID)
                if Arr():
                    return True
        return syntaxError()

# p()
    
    def p():
        global i, tokenList
        if(tokenList[i]=="THIS"):
            return True
        elif(tokenList[i].type=="ID" or tokenList[i].type=="("):
            return True
        return syntaxError()
    
# obj_declare:

    def parameter1():
        global i, tokenList
        if tokenList[i].type == ",":
            i += 1  # Consume the comma ","
            if OE() and parameter1():
                return True
        elif (tokenList[i].type == ")"):
            return True
        return syntaxError()  # Return True for epsilon

    def parameter():
        global i, tokenList
        #if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if OE() and parameter1():
            return True
        return syntaxError()

    def N5():
        global i, tokenList
        if (tokenList[i].type == "="):
            i += 1
            return OE()
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def N4():
        global i, tokenList
        if tokenList[i].type == ",":
            i += 1  
            if OE() and N4():
                return True
        elif tokenList[i].type == "{":
            i += 1  # Consume "{"
            if OE() and N4():
                if tokenList[i].type == "}":
                    i += 1  # Consume "}"
                    return N4()  # Recursively check for more occurrences
        elif (tokenList[i].type == "}" or tokenList[i].type == ";"):
            return True        
        return syntaxError()  # Return True for epsilon

    def N3():
        global i, tokenList
        if (tokenList[i].type == "{"):
            i += 1
            if OE() and N4():
                if (tokenList[i].type == "}"):
                    i += 1
                    return N4()
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def N2():
        global i, tokenList
        if (tokenList[i].type == "="):
            i += 1
            return N3()
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def N1():
        global i, tokenList
        if tokenList[i].type == "[":
            i += 1  # Consume "["
            if OE():
                if (tokenList[i].type == "]"):
                    i += 1 
                    return Arr() and N2()
        elif tokenList[i].type == "(":
            i += 1  # Consume "("    
            if parameter():
                if tokenList[i].type == ")":
                    i += 1  # Consume ")"
                    return N5()  # Check for SA and OE
        elif tokenList[i].type == "=": 
            i += 1
            if OE():
                return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()  # Return True for epsilon

    def obj_decl():
        global i, tokenList
        if tokenList[i].type == "OBJ":
            i += 1  # Consume "obj"
            if tokenList[i].type == "ID":
                i += 1  # Consume the first ID
                if tokenList[i].type == "ID":
                    i += 1  # Consume the second ID
                    if N1():
                        if tokenList[i].type == ";":
                            i += 1  # Consume the semicolon
                            return True
        return syntaxError()

# destructor

    def destructor():
        global i, tokenList
        if (tokenList[i].type == "~"):
            i += 1
            if (tokenList[i].type == "ID"):
                i += 1
                return indexD()
        return syntaxError()

    
    def indexD():
        global i, tokenList
        if (tokenList[i].type == "("):
            i += 1
            if (tokenList[i].type == ")"):
                i += 1
                if (tokenList[i].type == "{"):
                    i += 1
                    if (tokenList[i].type == "}"):
                        i += 1
                        return True
        return syntaxError()
        
    def destructor_SST():    
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_dec() or struct_obj() or obj_decl() or assign_st() or OE() or class_dec():
            return constructor_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return constructor_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()    
        
# class_dec

    def sealed():
        global i, tokenList, typeMod
        if (tokenList[i].type == "SEALED"):
            typeMod=tokenList[i].value
           
            i+=1
            return typeMod
        elif(tokenList[i].type=="CLASS"):
            typeMod="-"
            print("elif", typeMod)
            return typeMod
        return syntaxError()

    def class_dec():
        global i, tokenList
        if sealed():
            if (tokenList[i].type=="CLASS"):
                i+=1
                if(tokenList[i].type=="ID"):
                    print("HM")
                    i+=1
                    if(Class_dec1()):
                        print("JJ")
                        i+=1
                        if(tokenList[i].type==";"):
                            print("class;")
                            i+=1
                            return True
        return syntaxError()

    def Class_dec1():
        global i, tokenList
        #if (tokenList[i].type == ":"):
        if(Inherit() and class_body()):
            print("II")
            return True
        #elif (tokenList[i].type == ";"):
         #   return True
        return syntaxError()
   
    def Inherit():
        global i, tokenList
        if(tokenList[i].type==":"):
            i+=1
            if(access_mod()):
                if(tokenList[i].type=="ID"):
                    i+=1
                    #return multiple_inherit()
                    if (multiple_inherit()):
                        print("SS")
                        return True
        elif(tokenList[i].type=="{" or tokenList[i].type==";"):
            print("PP")
            return True
        return syntaxError()
    
    def multiple_inherit():
        global i, tokenList
        if(tokenList[i].type ==","):
            i+=1
            if(access_mod()):
                if(tokenList[i].type=="ID"):
                    i+=1
                    return multiple_inherit()
        elif(tokenList[i].type=="{" or tokenList[i].type==";"):
            return True
        return syntaxError()

    def class_body():
        global i, tokenList
        if(tokenList[i].type=="{"):
            print("BBB")
            i+=1
            if(class_SST()):
                print("AZZZ")
                if(tokenList[i].type =="}"):
                    print("}")
                    #i+=1
                    return True
        elif(tokenList[i].type==";"):
            return True
        return syntaxError()
    
    def access_mod():
        global i, tokenList
        if(tokenList[i].type=="ACCESS MODIFIER"):
            i+=1
            return True
        #elif(tokenList[i].type=="ACCESS MODIFIER"):
        #    i+=1
        #    return True
        #elif(tokenList[i].type=="ACCESS MODIFIER"):
        #    i+=1
        #    return True
        elif(tokenList[i]=="ID"):
            return True        
        return syntaxError()
    
    def class_SST():
        global i, tokenList
        print("123")
        if access_mod():
            print("A")
            if (tokenList[i].type == ":"):
                i+=1
                return class_SST()
        elif dec():
            return class_SST()
            print("B")
        elif func_st() and class_SST():
            print("C")
            return True
        elif constructor() and class_SST():
            print("D")
            return True
        elif destructor() and class_SST():
            print("E")
            return True
        elif if_else() and class_SST():
            print("F")
            return True
        elif try_catch() and class_SST():
            print("G")
            return True
        elif for_st() and class_SST():
            print("H")
            return True
        elif print_() and class_SST():
            print("I")
            return True
        elif class_dec() and class_SST():
            print("J")
            return True
        elif struct_dec() and class_SST():
            print("K")
            return True
        elif OE():
            print("L")
            if (tokenList[i].type == ";"):
                i += 1
                return class_SST()
        elif struct_obj() and class_SST():
            print("M")
            return True
        elif obj_decl() and class_SST():
            print("N")
            return True
        elif assign_st() and class_SST():
            print("O")
            return True
        elif tokenList[i].type == "}":
            print("P")
            return True
        
        return syntaxError()

# constructor



    

    def constructor_Body():
        global i, tokenList
        if tokenList[i].type == "{":
            i += 1  # Consume "{"
            if constructor_SST():
                if tokenList[i].type == "}":
                    i += 1  # Consume "}"
                return True
        elif (tokenList[i].type == ";"):
            return True
        return syntaxError()

    def constructor_SST():
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_dec() or class_dec() or struct_obj() or obj_decl() or assign_st() or OE():
            return constructor_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
                return constructor_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()

    def indexC():
        global i, tokenList
        if tokenList[i].type == "(":
            i += 1  # Consume "("
            if param():
                if tokenList[i].type == ")":
                    i += 1  # Consume ")"
                    return constructor_Body()            
        return syntaxError()

    def constructor():
        global i, tokenList
        if tokenList[i].type == "CONSTRUCT":
            i += 1  # Consume "construct"
            if tokenList[i].type == "ID":
                i += 1  # Consume "ID"
                if indexC():
                    if (tokenList[i].type == ";"):
                        i += 1
                        return True
        return syntaxError()
    
    
# function_st
 
    def func_st():                # def int A(){}
        global i, tokenList
        if(key()):
            if(tokenList[i].type =="DEF"):
                i+=1
                if(DT2() and tokenList[i].type=="ID"):
                    i+=1
                    if(func_I()):
                        return True
        return syntaxError()

    def func_I():
        global i, tokenList
        if tokenList[i].type == "(":
            i += 1
            if param() and tokenList[i].type == ")":
                i += 1
                print("dddddddddddddddddddddddd")
                if override():
                    print("xxxxxxxxxxxxxxxxxxxxxx")
                    if funct_body():
                        print("000000000000000000")
                        return True
        return syntaxError()

    def override():
        global i, tokenList
        print("uuuuuuuuuuuuuuuuuuuuuuuuuuu")
        if (tokenList[i].type == "OVERRIDE"):
            print("iiiiiiiiiiiiiiiiiiiiiiiii")
            i+=1
            return True
        elif funct_body():
            print("hhhhhhhhhhhhhhhhhhhhhhhh")
            return True      
        print("jjjjjjjjjjjjjjjjjjjjjjjj")
        return syntaxError()

    def param1():
        global i, tokenList
        if tokenList[i].type == ",":
            print("dfdfd")
            i += 1
            if param2() and param1():
                return True
        elif(tokenList[i].type ==")"):
            return True
        return syntaxError()
     
                   

    
    def key():
        global i, tokenList
        if tokenList[i].type == "VIRTUAL":
            i += 1
            return True
        elif tokenList[i].type == "DEF":
            return True
        return syntaxError()
    
    def funct_body():
        global i, tokenList
        if tokenList[i].type == "{":
            print("oooooooooooooooooooooooooo")
            i += 1
            if funct_SST() and tokenList[i].type == "}":
                print("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
                i += 1
                return True
        elif tokenList[i].type == ";":
            i += 1
            return True
        return syntaxError()


    def funct_SST():
        global i, tokenList
        if dec() or func_st() or if_else() or try_catch() or for_st() or print_() or struct_dec() or class_dec() or struct_obj() or obj_decl() or assign_st() or break_() or continue_() or OE() or return_():
            return funct_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return funct_SST()
        elif tokenList[i].type == "}":
            return True 
        return syntaxError()  # Return True for epsilon

    def DT2():
        global i, tokenList
        #if tokenList[i].type == "void" or tokenList[i].type == "int" or tokenList[i].type == "float" or tokenList[i].type == "char" or tokenList[i].type == "string" or tokenList[i].type == "bool":
        if tokenList[i].type == "DT":
            i += 1
            return True
        return syntaxError()
    
# try_catch

    def try_catch():
        global i, tokenList
        if tokenList[i].type == "CHECK":
            i += 1
            if tokenList[i].type == "{":
                i += 1
                if try_SST():
                    if tokenList[i].type == "}":
                        i += 1
                        if catch():
                            return catch1() 
        return syntaxError()

    def catch1():
        global i, tokenList
        if catch() and catch1():
            return True
        elif tokenList[i].type == "DT" or tokenList[i].type == "DEF" or tokenList[i].type == "VIRTUAL" or tokenList[i].type == "THROW" or tokenList[i].type == "ACCESS MODIFIER" or tokenList[i].type == "IF" or tokenList[i].type == "BREAK" or tokenList[i].type == "CONTINUE" or tokenList[i].type == "CONST" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "THIS" or tokenList[i].type == "(" or tokenList[i].type == "ID" or tokenList[i].type == "NOT" or tokenList[i].type == "RETURN" or tokenList[i].type == "CHECK" or tokenList[i].type == "FOR" or tokenList[i].type == "PRINT" or tokenList[i].type == "ST" or tokenList[i].type == "OBJ" or tokenList[i].type == "ASSIGN" or tokenList[i].type == "STRUCT" or tokenList[i].type == "CLASS" or tokenList[i].type == "}" or tokenList[i].type == "CONSTRUCT" or tokenList[i].type == "~" or tokenList[i].type == "MAIN" or tokenList[i].type == "ELIF" or tokenList[i].type == "ELSE":
            return True
   
    def try_SST():
        global i, tokenList
        if dec() or if_else() or try_catch() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or throw() or OE() or return_():
            return try_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return try_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()  # Return True for epsilon

    def catch():
        global i, tokenList
        if tokenList[i].type == "CATCH":
            i += 1
            if tokenList[i].type == "(":
                i += 1
                if catch_para():
                    if tokenList[i].type == ")":
                        i += 1
                    if tokenList[i].type == "{":
                        i += 1
                        if catch_SST():
                            if tokenList[i].type == "}":
                                i += 1
                                return True
        return syntaxError()

    def catch_para():
        global i, tokenList
        if obj_decl():
            return True
        elif tokenList[i].type == "...":
            i += 1
            return True
        return syntaxError()

    def catch_SST():
        global i, tokenList
        if dec() or if_else() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or throw() or OE() or return_():
            return catch_SST()
        elif OE():
            if tokenList[i].type == ";":
                i += 1  # Consume ";"
            return catch_SST()
        elif tokenList[i].type == "}":
            return True 
        return syntaxError()  # Return True for epsilon

# for-st
    def for_st():
        global i, tokenList
        if(tokenList[i].type=="FOR"):
            i+=1
            if(tokenList[i].type=="("):
                i+=1
                if(init11()):
                    print("1st cond")
                    #if(tokenList[i].type==";"):
                    print(";for")
                    # i+=1
                    if(cond11()):         # issue (for-loop)
                        print("2nd cond")
                        if(tokenList[i].type==";"):
                            i+=1
                            if(inc_dec11()):
                                print("Inc_Dec i++")
                                if(tokenList[i].type==")"):
                                    i+=1
                                    return for_body()
            return syntaxError()
    
    def init11():
        global i, tokenList
        if dec():
            return True
        elif(assign_st()):
            return True
        elif(tokenList[i].type == ";"): 
            return True
        return syntaxError()
    
    def cond11():
        global i, tokenList
        if OE():
            print("for-OE")
            return True
        elif(tokenList[i].type ==";"):
            print("for-;")
            return True
        return syntaxError() 
 
    def inc_dec11():
        global i, tokenList
        if Inc_Dec_obj_call():
            print("I?C")
            return True
        elif(tokenList[i].type==")"):
            #print("??")
            return True
        return syntaxError() 
        
    def for_body():
        global i, tokenList
        if tokenList[i].type == "{":
            i += 1
            if funct_SST() and tokenList[i].type == "}":
                i += 1
                return True
        elif tokenList[i].type == ";":
            i += 1
            return True
        return syntaxError()

    def for_SST():
        global i, tokenList
        if dec() or func_st() or if_else() or try_catch() or for_st() or print_() or struct_obj() or obj_decl() or assign_st() or break_() or continue_() or return_() or OE():
            return for_SST()
        elif OE():
         if tokenList[i].type == ";":
                i += 1  
                return for_SST()
        elif tokenList[i].type == "}":
            return True
        return syntaxError()

    
# OE:
    def OE():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (AE() and OE_()):
            print("OE")
            return True 
        return syntaxError()
    
    def OE_():
        global i, tokenList
        if (tokenList[i].type == "OR"):
            i += 1
            if (AE() and AE_()):
                print("OE_")
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type ==";" or tokenList[i].type =="{" or tokenList[i].type =="}" or tokenList[i].type =="," or tokenList[i].type =="]"):
            print(",OE_")
            return True
        return syntaxError()
    
    def AE():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (RE() and AE_()):
            print("AE")
            return True
        return syntaxError()
    
    def AE_():
        global i, tokenList
        if (tokenList[i].type == "AND"):
            i += 1
            if (RE() and AE_()):
                print("AE_")
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "OR" or tokenList[i].type == "AND" or tokenList[i].type =="{" or tokenList[i].type =="}" or tokenList[i].type =="]" or tokenList[i].type ==";" or tokenList[i].type ==","):
            print(",AE_")
            return True
        return syntaxError()
    
    def RE():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (E() and RE_()):
            print(",RE")
            return True
        return syntaxError()
    
    def RE_():
        global i, tokenList
        if (tokenList[i].type == "R_OP"):
            #print("i >")
            i += 1
            if (E() and RE_()):
                print("RE_")
                return True
        elif (tokenList[i].type == ")" or tokenList[i].type == "OR" or tokenList[i].type == "AND" or tokenList[i].type =="{" or tokenList[i].type =="}" or tokenList[i].type =="]" or tokenList[i].type ==";" or tokenList[i].type ==","):
            print(",")
            return True
        return syntaxError()
    
    def E():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (T() and E_()):
            print("E()")
            return True
        return syntaxError()
    
    def E_():
        global i, tokenList
        if (tokenList[i].type == "PM"):
            i += 1
            if (T() and E_()):            # possible issue
                print("E_")
                return True
        elif (tokenList[i].type == "R_OP") or (tokenList[i].type == "AND") or (tokenList[i].type == "OR") or (tokenList[i].type == ")") or (tokenList[i].type == "{" or (tokenList[i].type == "}") or (tokenList[i].type == "]") or (tokenList[i].type == ";")or (tokenList[i].type == ",")    ) :
            print(",E_")
            return True 
        return syntaxError()
    
    def T():
        global i, tokenList
        #if (tokenList[i].type == "THIS" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "NOT" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (F() and T_()):
            print("T()")
            return True
        return syntaxError()
    
    def T_():
        global i, tokenList
        if (tokenList[i].type == "MDM"):
            i += 1
            if (F() and T_()):
                print("T_")
                return True
        elif (tokenList[i].type == "PM") or (tokenList[i].type == "R_OP") or (tokenList[i].type == "AND") or (tokenList[i].type == "OR") or (tokenList[i].type == ")") or (tokenList[i].type == "{" or (tokenList[i].type == "}") or (tokenList[i].type == "]") or (tokenList[i].type == ";")or (tokenList[i].type == ",")    ) :
            print(",T_")
            return True
        return syntaxError()
    
    def F():
        global i, tokenList
        #if (tokenList[i].type == "this" or tokenList[i].type == "INT" or tokenList[i].type == "FLT" or tokenList[i].type == "CHAR" or tokenList[i].type == "STR" or tokenList[i].type == "(" or tokenList[i].type == "!" or tokenList[i].type == "Inc_Dec" or tokenList[i].type == "ID"):
        if (const()):
            print("342")
            return True
        elif (Inc_Dec_obj_call()):
            print("Inc_Dec_obj_call1")
            return True
        elif (tokenList[i].type == "("):
            #print("(")
            i += 1
            if (OE()):
                if (tokenList[i].type == ")"):
                    #i += 1
                    #print("Inside OE")
                    return True
        elif (tokenList[i].type == "NOT"):
            i += 1
            if (F()):
                #print("Inside F")
                return True
        elif (obj_call()):
            print("i")
            return True
        return syntaxError()
    
    
except LookupError:
    print_("Tree Incomplete... Source File (Input) Completely Parsed")




        
        
       
        
