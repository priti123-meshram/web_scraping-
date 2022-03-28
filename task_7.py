import json
def analyse_movies_directors():
    directors=open("task5.json")
    list=json.load(directors)
    # print(list)
    list1=[]
    dic={}
    for i in list:
        if(i["Director:"]) not in list1:
            list1.append(i["Director:"])
            # print(list1)
            dic={}
            list2=[]
            for j in list1:
                i=0
                c=0
                while i <len(list):
                    if j==list[i]["Director:"]:
                        c=c+1
                    i=i+1
                dic.update({j:c})
            list2.append(dic)
    with open("task7.json","w")as f:
        json.dump(list2,f,indent=2)
analyse_movies_directors()










