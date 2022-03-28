from bs4 import BeautifulSoup
import requests
import json

def scrape_top_list():
    get_url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
    Response= requests.get(get_url)
    # print(Response)
    htmlcontent=Response.content
    # print(htmlcontent) #response ko stoar kiya gaya hai.
    soup=BeautifulSoup(htmlcontent,'html.parser')
    table=soup.find("table",class_="table")
    # print(table)
    tr=table.find_all("tr")
    # print(tr)
    top_movie=[]
    serial_no=1
    for i in tr:
        rank=i.find_all("td",class_="bold")
        for j in rank:
            rank=j.get_text()
        # print(rank)
        movie_rating=i.find_all("span",class_="tMeterScore")# find_all sabhi persentege print hone ke liye lagaya hai

        for rate in movie_rating:
            # rating=k.get_tex().strip()
                
            rating=rate.get_text().strip()
            # print(rating)
        movie_name=i.find_all("a", class_="unstyled articleLink")#all movies ke name print honge
        # print(movie_name)
        for name in movie_name:
            title=name.get_text().strip()
            # print(title)
            list=title.split()
            year=list[-1][1:5] # [1:5] sirf no. print hone ke liye lagaya 
            # print(year)
            year1=int(year)
            name_lenght=len(list)-1
            name=""
            # print(name_lenght)

            for l in range(name_lenght):
                name+=""
                name+=list[l]
            movie_name=name
            # print(movie_name)
        movie_reviews=i.find_all("td",class_="right hidden-xs")
        for rev in movie_reviews:
            reviews=rev.get_text()
            # print(reviews)
        url=i.find_all("a",class_="unstyled articleLink")
        for i in url:
            # print(i)
            link=i["href"]
            # print(link)
            movie_link="https://www.rottentomatoes.com"+link
            #print(movie_link) #top movie ke link
            details={"Movie Rank":"","Movie Rating":"","Movie Name":"","Movie Reviews":"","Movie Url":"","Year":""}
            # print(details)#only details 
            details["Movie Rank"]=rank
            details["Movie Rating"]=rating
            details["Movie Name"]=name
            details["Movie Reviews"]=reviews
            details["Movie Url"]=movie_link

            details["Year"]=year1

            top_movie.append(details.copy())
            # print(top_movie)
        details={'position':'',"name":'','year':'','rating':'','rating':'','url':''}
    with open("task1.json","w")as file:
        json.dump(top_movie,file,indent=2)
        # print(top_movie)
    return top_movie

num=scrape_top_list()

