import requests
import re
import os
from dotenv import load_dotenv
import time
load_dotenv()
def insta(url):
  if 'instagram.com' not in url:
    print("please give me an instagram link")
    return
  cookies = {
   'sessionid': os.getenv("INSTAID")}
  response = requests.get(url, cookies=cookies)
  response = response.text
  response = response.replace("\/", "/")
  try:
      patternvideo = r'"contentUrl":"(.*?)","thumbnailUrl"'
      matchesvideo = re.findall(patternvideo, response)
      patternimages = r'"url":"(https://scontent\.cdninstagram\.com/[^"]+)(?=.*"}],"interactionStatistic")'
      matchesimages = re.findall(patternimages, response)
      if matchesimages == []:
         matchesimages = re.findall(r'"url":"(https:\/\/scontent-waw1-1\.cdninstagram\.com\/[^"]+)(?=.*"}],"interactionStatistic")', response) #images might sometimes be on regional servers, change it to your preference
      if matchesimages == [] and matchesvideo == []:
         print("couldnt find media links")
         return
  except Exception as e:
      print("ERROR: ", e)
      print("failed to find content urls")
      return
  video = "funnyvideo"
  for i in matchesvideo:
    i = i.encode('utf-8').decode('unicode_escape')
    try:
        currenttime = time.strftime("%d-%m-%y_%H-%M-%S", time.localtime())
        with open(video + currenttime + ".mp4", "wb") as f1:
            response = requests.get(i, stream=True)
            f1.write(response.content)
        print(f"succesfully saved {video + currenttime + '.mp4'}")
    except Exception as e:
            print("ERROR: ", e)
  image = "funnyimage"
  for i in matchesimages:
    i = i.encode('utf-8').decode('unicode_escape')
    try:
       currenttime = time.strftime("%d-%m-%y_%H-%M-%S", time.localtime())
       with open(image + currenttime + ".jpg", "wb") as f1:
            response = requests.get(i)
            f1.write(response.content)
            print(f"succesfully saved {image + currenttime + '.jpg'}")
    except Exception as e:
            print("ERROR: ", e)
       
url = str(input("URL to instagram post: "))
insta(url)
