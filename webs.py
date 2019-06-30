
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

my_url='https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient=uReq(my_url)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,"html.parser")
containers=page_soup.findAll("div",{"class":"_1-2Iqu row"})
#print(len(containers))
#print(soup.prettify(containers[0]))
container=containers[0]
#(price)
price=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
#print(price[0].text)
#(rating)
ratings=container.findAll("div",{"class":"niH0FQ"})
#print(ratings[0].text)
#(name)
product_name=container.findAll("div",{"class":"_3wU53n"})
#print(product_name[0].text)

filename="products.csv"
f=open(filename,"w")

headers="product_name,pricing,ratings\n"
f.write(headers)
#for all such containers
for container in containers:
	product_container=container.findAll("div",{"class":"_3wU53n"})
	product_name=product_container[0].text

	price_container=container.findAll("div",{"class":"col col-5-12 _2o7WAb"})
	price=price_container[0].text.strip()
	#striping for any extra characters

	rating_conatiner=container.findAll("div",{"class":"niH0FQ"})
	rating=rating_conatiner[0].text

	#print("product_n:"+product_name)
	#print("price:"+price)
	#print("ratings:"+rating)

	trim_price=''.join(price.split(','))
	rm_rupee=trim_price.split("₹")
	add_rs_price="Rs."+rm_rupee[1]
	split_price=add_rs_price.split('E')
	final_price=split_price[0]

	split_rating=rating.split(",")
	split_new=split_rating[0].split(" ")
	final_rating=split_new[0]

	print(product_name.replace(",","|")+","+final_price+","+final_rating+"\n")
	f.write(product_name.replace(",","|")+","+final_price+","+final_rating+"\n")
        #writing to products.csv
f.close()
