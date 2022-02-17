from downloader_methods import Download
import sys
import time

inicio = """ 
  Script by Bryan Herrera
[+]---------------------[+]
  Youtube-dl-downloader CLI
"""
for c in inicio:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep( 0.01)


url = input("\n Ingresa la URL del video: ")
quality = input("\n Ingresa la calidad del video(Best|Semi|Worst): ")
playlist = input("\n ¿Es una playlist? (True/False): ")


Download(url, quality, playlist).mp3_download()