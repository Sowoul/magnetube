#First and basic version of boredflix, a simple scraper for movies on piratebay and yts, with the most basic gui, and opens the movie in the desired browser.
from urllib.request import Request, urlopen
import re
import webbrowser
cond=1
movie=input('What do you feel like watching today :3\n')
movie=movie.replace(' ','%20')
try:
    f=Request(f'YOUR SOURCE 1', headers={'User-Agent': 'Mozilla/5.0'})
    f=urlopen(f).read().decode()
    f=re.split('<a href="magnet:',f)
    stop1=re.search('"',f[1])
except IndexError:
    pass
try:
    yts=Request(f'YOUR SOURCE 2', headers={'User-Agent': 'Mozilla/5.0'})
    yts=urlopen(yts).read().decode()
    yts=re.split('<a class="magnet-download" href="magnet:',yts)
    ytstop=re.search('"',yts[1])
except IndexError:
    pass
try:
    pirate1='magnet:'+str((f[1])[:stop1.start()])
    print('A valid piratebay magnet was found')
    cond=2
except:
    print('No valid piratebay magnets found :(')
try:
    yts1='magnet:'+str((yts[1])[:ytstop.start()])
    print('A valid YTS mirror was found')
    cond=2
except:
    print('No valid yts magnets found :(')
if cond == 2:
    choice=int(input('Which one would u like, 1 or 2?\n'))
    if choice==1:
        magnet='magnet:'+str((f[1])[:stop1.start()])
    elif choice==2:
        magnet = 'magnet:' + str((yts[1])[:ytstop.start()])
    # magnet='https://webtor.io/#/'+magnet
    webbrowser.open(magnet)
