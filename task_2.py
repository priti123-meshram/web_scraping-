from task_1 import  scrape_top_list
import json
list=scrape_top_list()
def group_by_year(movies):
    years=[]
    for i in movies:
        year=i["Year"] #years ki value hamne year nam ke vaiabe me store kr liya hai
        if year not in years:# only unic years 
            years.append(year)
        # print(years)
        # yaha pe ham ek  movie ki dict banayenge,
        # hamara i jo hai vo ek year hai,  aur vo dict ki keys hai.aur value khali list hogi.

    movie_dict= {i:[]for i in years}
    for i in movies:
        # name=i
        year=i["Year"] #year ki vaule
        for x in movie_dict:
            if str(x)== str(year):
                movie_dict[x].append(i)
    with open("task2.json","w")as file:
        json.dump(movie_dict,file,indent=2)
    return movie_dict
    # print(movie_dict)
group_by_year(list)



