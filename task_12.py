from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint

def main_fun(url):                                                                  
        # print(url)
    url_api=requests.get(url)
    # print(url_api)
    html_content=url_api.content
    soup=BeautifulSoup(html_content,"html.parser")
    # print(soup)
    list=[]
    cast_div=soup.find('div',class_="castSection")
    # print(cast_div)
    recursive=cast_div.find_all("div",recursive=False)
    # print(recursive)
    j=0
    for i in recursive:
        if j==5:
            break
        all=i.find('div',class_="media-body")
        if all.a !=None:
            list.append(all.a.span.get_text().strip())
        j+=1
    print(list)
    with open("Task12.json","w") as f:

        json.dump(list,f,indent=4)
    return list
main_fun("https://www.rottentomatoes.com/m/black_panther_2018")


