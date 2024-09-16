from pytube import Playlist, YouTube
import asyncio

playlist = Playlist("https://www.youtube.com/playlist?list=PL7ersPsTyYt1HnCgrT6Up-pan4yLBpyFs")

video_url = playlist.video_urls
async def download(url , index : int):
    print("Downloading {}".format(index))

    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()

    await asyncio.to_thread(video.download)

    print("Downloaded {}".format(index))

async def main():
    ls=[]
    for idx , url  in enumerate(video_url , start=1):
        ls.append(download(url , idx))

    await asyncio.gather(*ls)
asyncio.run(main())