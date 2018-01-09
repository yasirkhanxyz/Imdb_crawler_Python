from bs4 import BeautifulSoup
import requests
import re
import colorama
from colorama import Fore, Back, Style
colorama.init()

global actors_name

def get_actor():
     actors_name = raw_input( "Enter Hero Name :" )
     return actors_name


"""" This Function Used to Take input Actor name and can be used as global variable """


def get_actor_url():

    endfix = '&s=all'
    actors_name1 = actors_name.replace( " ", "+" )
    get_search_list_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + actors_name1 + endfix
    print(Fore.RED + "Stage 1 Url :" + get_search_list_url)
    # print "Stage 1 Url :" + get_search_list_url
    return get_search_list_url


    """" This Function Used to fetch the Actor name and parse to URL to Search """


def pattern_matching(url):
    response = requests.get(url);
    page = response.text
    #print response
    soup = BeautifulSoup( page, 'lxml');
    actor_segment = soup.find( "td", attrs={"class": "result_text"} )
    relevant_actor = actor_segment.find( 'a' )['href']
    actor_url = "http://www.imdb.com" + relevant_actor + "#actor"
    part1="http://www.imdb.com" + relevant_actor
    print "Stage 2 Url :" + actor_url
    # print part1
    # response1 = requests.get(part1);
    # page2 = response1.text
    # soup3 = BeautifulSoup( page2, 'lxml' );
    # # print soup3
    # view = soup3.find( "span", attrs={"itemprop": "name"} ).get_text()
    # print view
    return actor_url


    """" This Function Used to fetch the Actor name and parse to URL to Search """


def filmography(url):
    response = requests.get(url);
    page = response.text
    soup1 = BeautifulSoup(page, 'lxml');
    movie_segment = soup1.find("div",attrs={"id":"filmo-head-actor"}).get_text()
    x = movie_segment.splitlines()
    movie_no = x[-1]
    m = re.search( 'Actor \((.+?)credits', movie_no )
    if m:
        found = m.group( 1 )

    response1 = requests.get(url);
    page2 = response1.text
    soup3 = BeautifulSoup( page2, 'lxml' );
    # print soup3
    view = soup3.find( "span", attrs={"itemprop": "name"} ).get_text()
    # print(Back.GREEN + text + Style.RESET_ALL)
    print (Back.BLACK + "Currently you are viewing profile of : "  + Style.RESET_ALL)+ (Fore.GREEN + view + Style.RESET_ALL )
    print actors_name + " Has worked in " + (Fore.GREEN + found + Style.RESET_ALL ) + "Movies as an actor."


    """" This Function Used to fetch the list Number movies & Director Done by this Actor """

def movie_listing(url):
    response = requests.get(url);
    page = response.text
    soup = BeautifulSoup( page, 'lxml' );
    movie_list = soup.find( "div", attrs={"data-category": "actor"}).find_next_sibling("div").find("div")
    return movie_list.find_all('a')
    # print(movie_list.get('b'))
    # movie_list = soup.find( "div", attrs={"data-category": "actor"}).find_next_sibling("div").find("a")
    # find all tag and then get by attribute
    # print relevant_list

# print movie_segment
# print movie_segment.find_next_sibling("div")

actors_name = raw_input( "Enter Hero Name :")
filmography(pattern_matching(get_actor_url()))
movielist = movie_listing(pattern_matching(get_actor_url()))
# print movielist
for movie in movielist:
    print movie

# def urlfetching(segmet1):
#     response = str(segment1)
#     soup = BeautifulSoup(patternmatching(segment1)),"lxml");
#     actoredsnip = soup.find_all("a")
#     print actoredsnip


# actoredurl=soup.find_all('a')

# soup.find_all( "a", attrs={"class": "sister"} )
# for actored in soup.find_all( "a", class_="findList" ):
#     print(actored.get( "a" ))
# for actor in soup.find_all('a href'):
#  print(actor.get("b"))
# find_all('title', limit=1)
# td class="primary_photo"


# print soup

# url = "http://www.imdb.com/name/nm0000158/?ref_=nv_sr_1";
# response = requests.get(url);
# page = response.text;
# soup = BeautifulSoup(page);
#
# #find all tag and then get by attribute
# for movie in soup.find_all('a href'):
#     print (movie.get('b'))


# runLoop = 1
# while runLoop:
#     x1 = soup.find( "div", attrs={"data-category": "actor"} ).find_next_sibling( "div" ).find( "b" )
#     if x1 is not None:
#         print (x1.get( 'a' ))
#     else:
#         runLoop = 0
