# Get the Library
import pytube

# Loop the Code
x = "true"
while x == "true":
    
    # Get the URL
    url = input()
    
    # Verify if the text contains an url
    ver = url.find("https://www.youtube.com/watch")
    
    # Get the Video if the text was an url
    if ver == 0:
        youtube = pytube.YouTube(url)
        video = youtube.streams.first()
        print("Got the video")
    
    # Respond if the text wasn't an url
    if ver == -1:
        ver1 = url.find("thank")
        if ver1 == 0:
            print("no problem mr. user")
            break
        else:
            ver1 = url.find("https://youtu.be/")
            if ver1 == 0:
                youtube = pytube.YouTube(url)
                video = youtube.streams.first()
                print("Got the video")
            else:
                print("what")
                break

    # Download the Video
    video.download('../Video')
    print("Download done")
    # fine
    