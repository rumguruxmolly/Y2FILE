from pytube import YouTube as mayhem
link=input('Insert youtube Link: ')
yt= mayhem(link)
type=3
while type!='1' and type!='2':
    type=input("MP3: 1 or MP4: 2")
if type=='1':
    stream = yt.streams.get_audio_only()
else:
    stream = yt.streams.get_highest_resolution()

print('File downloading...')

stream.download()

print('download finished!')
