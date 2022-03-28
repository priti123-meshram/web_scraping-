import json

with open("task5.json","r") as f:
    data1=json.load(f)

def language_and_directores(movies_list):
    Directoreslist=[]

    for movies in movies_list:
        # print(movies)
        if movies["Director:"] not in Directoreslist:
            Directoreslist.append(movies["Director:"])
            # print(Directoreslist)
    f={}        
    for i in Directoreslist:
        print(i) 
        count={}
        lan=[]
        for director in movies_list:
            if i==director["Director:"]:
                if director["Original Language:"] not in lan:
                   count[director["Original Language:"]]=1
                   lan.append(director["Original Language:"])
                    # print(a)
                    # print(lan)                     
                else:
                    count[director["Original Language:"] ]+=1              
        f[i]=count
        # print(f) 
                        
    with open("task10.json","w") as file:
        json.dump(f,file,indent=4)
    return f

language_and_directores(data1)