# f = open( '19_File_Handling/sumit.txt' )
# f = open('19_File_Handling/sumit.txt', 'r')

# print( f.read() )   # All file content read

# for x in f:
#     print(x)
    
# print( f.read(20) )   #  Read only 20 characters
# print( f.readline() )
# print( f.readline(5) ) # #  Read only 5 characters
# print( f.readline() )
# print( f.readline() )



# f = open('19_File_Handling/sumit.txt', 'w')
# f.write('Welcome')

# f = open('19_File_Handling/sumit.txt', 'a')
# f.write(' to this chapter.')
# f.write(' and this file is very nice')



f = open('19_File_Handling/sumit.txt', 'w')
f.write("Welcome \n\nDear, Student")
f.close()