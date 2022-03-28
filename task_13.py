# from task_12 import*
# # import json
# from bs4 import BeautifulSoup
# cast=main_fun(url_api)
# print(cast)



# def scrape_movie_details(Movie_url):
#     moviedetails={}
#     page=requests.get(Movie_url)
#     # print(page)
#     soup=BeautifulSoup(page.text,"html.parser")
#     # print(soup)
#     # title_div=soup.find(div,class_="scoreboard_title").h1.get.text()
#     # print(title_div)
#     moviedetails["name"]=soup.find("h1").text
#     # print(moviedetails)
#     main=soup.find("ul",class_="content-meta info")
#     # print(main)
#     all=main.find_all("li",class_="meta-row clearfix")
#     # print(all)
#     for i in all:
#         # print(i)
#         # moviedetails[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value")).text).split())
#         moviedetails[" ".join((i.find("div",class_="meta-label subtle").text).split())]=" ".join((i.find("div",class_="meta-value").text).split())
#         print(moviedetails)
# scrape_movie_details("https://www.rottentomatoes.com/m/black_panther_2018")