import platform

# x = platform.machine()
# x = platform.node() 
# x = platform.processor() 
# x = platform.system()
x = platform.win32_edition()
# x = platform.platform(aliased=False, terse=False) 

print(x)

