# insta-post-downloader
downloads posts from instagram using python requests
instagram session ID needed

# how to use it (for those who are new to python):
1. download python and set as path in the installation (3.10.9+)
2. download the zip file and put it in a directory you want the videos to be saved in -
[download](https://github.com/Hecker5556/insta-post-downloader/archive/refs/heads/main.zip)
3. open command prompt, navigate to the directory with the file (for example cd C:\Users\USER\Downloads)
4. type pip install requests, wait for the module to install
5. type python main.py
6. enjoy

# how to get your instagram session id (to replace in the .env file)

1. go on instagram.com
2. press ctrl+shift+i to bring up developer tab
3. go to the network tab 
![image](https://github.com/Hecker5556/insta-post-downloader/assets/96238375/2d9dbd1b-7306-4c02-aee6-e7333635ce7a)
4. go to dms
5. search for this (or whatever will have ur cookies)  ![image](https://github.com/Hecker5556/insta-post-downloader/assets/96238375/b4bb6f41-e9be-4e48-9291-5dddda6dfd8e)

6. right click the request and copy as curl (bash) 

![image](https://github.com/Hecker5556/insta-post-downloader/assets/96238375/58823efb-e10a-4781-8316-e64b5ce78f37)

[the curl converter](https://curlconverter.com)
7. now copy the session ID and paste it in the .env file 
 ![image](https://github.com/Hecker5556/insta-post-downloader/assets/96238375/1ef01a71-caf1-4e38-8c35-0acee8eec01a)
 ![image](https://github.com/Hecker5556/insta-post-downloader/assets/96238375/1c23a364-217b-4f09-8b7b-78fc83eff5c3)



