from pytube import YouTube

def download(link):
    YouTubeObject = YouTube(link)
    res = input("Please enter the resolution: ")
    YouTubeObject = YouTubeObject.streams.filter(file_extension = 'mp4', res = f'{res}p')[0]
    try:
        YouTubeObject.download()
    except:
        print("Something went wrong")
    else:
        print("Download successful")

link = input("Please enter the link here: ")
download(link)