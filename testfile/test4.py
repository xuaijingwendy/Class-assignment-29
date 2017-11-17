def functionName( level ):
    if level < 1:
        raise Exception("Invalid level!", level)
   
        print "OK"

try:
    functionName( 5 )            
except "Invalid level!":
    print "you....."
else:
    print "finally always run ..."
