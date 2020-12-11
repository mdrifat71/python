from bs4 import BeautifulSoup
import requests


# (Oppo P7 ==> oppo-p7)
def str_to_url(s):
    s = s.replace(" ","-")
    s = s.replace("/","-")
    s = s.replace(",","")
    s = s.lower()
    return s

# (Oppo P7 ==> oppo+p7)
def str_to_search_query(s):
    s = s.replace(" ", "+")
    s = s.replace("/", "+")
    s = s.replace("-","")
    s = s.lower()
    return s


def extract():

    #main url
    url = "https://www.mobiledokan.co/product/"

    #search url
    search_url = "https://www.mobiledokan.co/?s="

    product_name = input("product name: ")

    #specific product route
    product_route = url + str_to_url(product_name)

    #product searching route
    search_route = search_url + str_to_search_query(product_name)
    
    #make a request for specific product
    source = requests.get(product_route).text
    soup = BeautifulSoup(source, "lxml")

    try:
        #imgae url
        image = soup.find("img", class_="aps-image-zoom").attrs['src']
        #price
        price = soup.find("span", class_="aps-price-value").text
        #title
        title = soup.find("h1", class_="aps-main-title").text
        print(title)
        print(image)
        print(price)
    except:
        #if product route not found
        #searching for given key
        source = requests.get(search_route).text
        soup = BeautifulSoup(source, "lxml")
        
        #all search results heading for given key
        titles = soup.find_all("h2", class_="post-title")

        if len(titles) != 0:
            print("Please search specific.............")
            for title in titles:
                print(title.a.text)
        else:
            print("No product found!!")
   
    
extract()
