from task_2 import*
years=group_by_year(list)
import json
#task 2 pr paramitar chal raha hai.
def group_by_decade(movies):
    m_dic={}
    list1=[]
    for i in movies:# movies task2 ka salution hai usipr task chala rahe hai.
        m=i%10 # ye task 2 pr chal raha hai ,to yiski ek ek key ayengi.
               # jaise,  1973 key ko 10 se (%) krenge to remaider 3 aayega,
        decade=i-m
        if decade not in list1:
            list1.append(decade)
    # print(list1)
    list1.sort()
#     # print(list1)
    for i in list1:
        m_dic[i]=[]# khali key ki value khali list
    for i in m_dic:
        dec=i+9
        for j in movies:
            if j<=dec and j>=i:
                for k in movies[j]:
                    m_dic[i].append(k)
    with open("task3.json","w")as file:
        json.dump(m_dic,file,indent=2)
    return(scrape_top_list)
    # return (m_dic)
# print(group_by_decade(year))
group_by_decade(years)




