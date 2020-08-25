import os
from scriptcontext import sticky as st

if "count" not in st or Reset:
    st["count"] = 0
    
if Write:

    filePath = ghenv.LocalScope.ghdoc.Path
    fileName = ghenv.LocalScope.ghdoc.Name
    filePath = filePath.replace(".gh","*")
    filePath = filePath.replace(fileName,"")

    filePath = os.path.join(filePath,Name + "_" + str(st["count"]) + ".txt")
    
    fileWrite = open(filePath,"w")
    
    for line in Data:
        fileWrite.write(line + "\n")

    fileWrite.close()

    st["count"] += 1