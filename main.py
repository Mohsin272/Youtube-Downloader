from pytube import YouTube

URL = str(input("Enter video URL: "))
my_video = YouTube(URL)

print('*************** Title ***************')
print(my_video.title)

print('********** Thumbnail Image **********')
print(my_video.thumbnail_url)

print('********** Select Resolution (ITAG) **********')

for stream in my_video.streams.filter(file_extension='mp4', type='video', progressive=True):
    print(stream)

tag = int(input('ITAG: '))
stream = my_video.streams.get_by_itag(tag)
stream.download()
print('Download Complete Enjoy :)')
