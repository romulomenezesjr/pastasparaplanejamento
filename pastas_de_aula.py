import os
import sys
from datetime import datetime
from datetime import timedelta

param = {"--ano":datetime.now().year,
        "--mes": datetime.now().month,
        "--dia": datetime.now().day,
        "--ch":20,
        "--aulas": "2" }
count = 0

for arg in sys.argv:
    if param.get(arg)!=None:
       param[arg] = int(sys.argv[count+1])
    count+=1

dt = datetime(param["--ano"], param["--mes"], param["--dia"])
for i in range(param["--ch"]):
    data_ = (dt + timedelta(days=i*7)).strftime("%Y-%m-%d")

    pasta = "{data} ({aulas}) #{num}".format(data=data_, aulas=param["--aulas"], num=i+1 )

    if (i+1) % 5 == 0:
        pasta += " PROVA"
        
    os.mkdir(pasta)
    
    
