

import json
# import pprint
def final(text):
    return " ".join(text.split())

def director_analyse():
    list=open("task5.json")
    l=json.load(list)
    # print(lang)
    list1=[]
    # dict={}
    for i in l:
        # g=i["Original Language:"]
        f=final(i["Genre:"])
        temp=f.split(",")
        # print(temp)
        for j in temp:
            if j not in list1:
                list1.append(j)
    # print(list1)            


        
    # if final(i["Genre:"]) not in list1:
        
        # #     # print(list1)
        # list1.append(final(i["Genre:"]))
    dict={}
    for j in list1:
        i=0
        count=0
        while i<len(l):
            if j in final(l[i]["Genre:"]).split(","):
                count+=1
            i+=1
        dict[j]=count
    # print(dict) 
    # pprint.pprint(dict)   


                                                          
    with open("task11.json","w") as f:
        json.dump(dict,f,indent=4)



    # print(list1)
director_analyse()









