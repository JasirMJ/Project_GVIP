import requests

country = "in"
category = "sports"
# url = (f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey=498b712c865a429496403df3698c9dcb")
# response = requests.get(url)
# newdata = response.json()
#
# if len(newdata['articles']):
#     for index,news in enumerate(newdata['articles']):
#         print(index+1 ," : " ,news['title'])
#         print("Description : " ,news['description'])
#         print("------------------------------------------------------------")
# else:
#     print(f"No matching news found for {category}")
#

c = None
while 1:
    c = input("enter category ")
    if len(c):
        print("Input got, Loop is breaking ... ")
        break
    else:
        print("Input not got please do it again...")
print("c is ",c )