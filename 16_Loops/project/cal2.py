h = []

while True:
    print('''
        #--------------------------- Welcome ---------------------------#
        Shortcuts:
            enter   : continue
            r       : restart
            q       : close,
            sh      : show history,
        
        Operators:
            +     : Addition
            -     : Subtraction
            *     : Multiplication
            **    : Exponent (raise to power)
            /     : Division
            //    : Floor Division
            %     : Remainder / Modulus
          ''')
    
    user = input('USE of Shortcuts: ')
    
    if "q" in user: break
    elif "r" in user: continue
    elif "sh" in user:
        print("\n#----------------- History ---------------#\n")
        # h = ['5   +   8    =     13',   '3   -   7    =     -4']
        for x in h:
            print("    " ,x)
        print("\n#--------------- End History -------------#\n")
        continue    
    
    a = int( input( "Enter value of A: " ) )  # 5
    o = input( "Select Operator: " )          # +
    b = int( input( "Enter value of B: " ) )  # 8

    if "+" in o:
        result = a + b # 5   +   8    =     13
        text_result =    a , o,  b , '=' , result 
        h.append( text_result )
        print( 'Result: ' , text_result )
    elif "-" in o:
        result = a - b 
        text_result =    a , o,  b , '=' , result 
        h.append( text_result )
        print( 'Result: ' , text_result )

   
    else:
        print("Invalid")