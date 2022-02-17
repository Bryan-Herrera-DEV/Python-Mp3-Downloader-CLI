import youtube_dl

class Download(object):
    def __init__(self, url, quality, playlist = False):
      self.url = url
      self.qualities = {
        "Best": "1400",
        "Semi": "320",
        "Worst": "180",
      }
      self.quality = self.qualities[quality]
      self.playlist = playlist
    
    def mp3_download(self):
        opts = {
            'format': 'bestaudio/best',
            'fixup': 'detect_or_warn',
            "verbose": False,
            "extract-audio": True,
            "audio-format": "mp3",
            "outtmpl": "/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }]
        }
        Download_obj = youtube_dl.YoutubeDL(opts)
        Download_obj.download([self.url])

        