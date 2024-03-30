from pytube import YouTube
import os
import bs4 
from html2image import Html2Image
def downloader(url):
    yt_vid = YouTube(url).streams.filter(progressive=True)
    yt_vid.order_by('resolution').desc().first().download()
    return yt_vid.order_by('resolution').desc().first().default_filename
def make_header(game_name, resolution):
    html_path = r'C:\Users\Raj\autoai_art\styling\header.html'
    with open(html_path) as inf:
        txt = inf.read()
        soup = bs4.BeautifulSoup(txt)
    soup.find(id='game_name').string = game_name
    title_html = soup.prettify()
    hti = Html2Image()
    hti.screenshot(html_str=title_html,save_as='tmp_imp.png', size=resolution)