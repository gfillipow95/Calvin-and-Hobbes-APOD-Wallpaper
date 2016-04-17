import time
import ctypes
from bs4 import BeautifulSoup
from PIL import Image
import urllib.request
import os

def make_soup(url):
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, "html.parser")

def get_images(url):
    soup = make_soup(url)
    images = [img for img in soup.findAll('img')]
    print (str(len(images)) + " images found.")
    if not os.path.exists('C:\\Users\\Gen\\Documents\\Astro\\'):
        os.makedirs('C:\\Users\\Gen\\Documents\\Astro\\')
    image_links = [each.get('src') for each in images]
    astropic = "http://apod.nasa.gov/apod/"+image_links[0]
    filename = "DailyAstroPic.jpg"
    if image_links[0][-3:] != "jpg":
        return image_links
    fullfilename = 'C:\\Users\\Gen\\Documents\\Astro\\'+filename
    urllib.request.urlretrieve(astropic, fullfilename)
    return image_links

def ChangeWallpaper():
    SPI_SETDESKWALLPAPER = 0x14     #which command (20)
    SPIF_UPDATEINIFILE   = 0x2 #forces instant update
    src = r"C:\Users\Gen\Documents\Astro\New.jpg" #full file location
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, src, SPIF_UPDATEINIFILE)

def CombineImages():
    BackgroundAstroPic = Image.open("C:\\Users\\Gen\\Documents\\Astro\\DailyAstroPic.jpg")
    CalvinHobbes = Image.open("C:\\Users\\Gen\\Documents\\Astro\\CalvinandHobbes.jpg")

    width, height = CalvinHobbes.size

    New_BackgroundAstroPic = BackgroundAstroPic.resize((width, height), Image.ANTIALIAS)

    New_BackgroundAstroPic.paste(CalvinHobbes, (0, 0), CalvinHobbes)
    New_BackgroundAstroPic.save("C:\\Users\\Gen\\Documents\\Astro\\New.jpg", "JPEG", quality=90)


if __name__ == '__main__':
    images = get_images("http://apod.nasa.gov/apod/astropix.html")
    if len(images) != 0:
        CombineImages()
        ChangeWallpaper()
