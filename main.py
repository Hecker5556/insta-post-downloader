import requests
import re
import os
from dotenv import load_dotenv
load_dotenv()
def insta(url):
  cookies = {
   'sessionid': os.getenv("INSTAID")}
  response = requests.get(url, cookies=cookies)
  response = response.text
  response = response.replace("\/", "/")
  response = response.encode('utf-8').decode('unicode_escape')
  try:
      patternvideo = r'"contentUrl":"(.*?)","thumbnailUrl"'
      matchesvideo = re.findall(patternvideo, response)
      patternimages = r'"url":"(https://scontent\.cdninstagram\.com[^"]+)"}'
      matchesimages = re.findall(patternimages, response)
  except:
      print("failed to find content urls")
  count = 0
  video = "funnyvideo" #change file name to your preference
  for i in matchesvideo:
      with open(video + str(count) + ".mp4", "wb") as f1: 
         response = requests.get(i, stream=True)
         f1.write(response.content)
         print(f"downloaded {video + str(count)}")
         count += 1
  count = 0
  image = "funnyimage" #change file name to your preference
  for i in matchesimages:
      with open(image + str(count) + ".jpg", "wb") as f1:
         response = requests.get(i)
         f1.write(response.content)
         print(f"downloaded {image + str(count)}")
         count += 1
       
url = str(input("URL to instagram post: "))
insta(url)
