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
    # print(Fore.RED + "Stage 1 Url :" + get_search_list_url)
    # print "Stage 1 Url :" + get_search_list_url
    return get_search_list_url


    """" This Function Used to fetch the Actor name and parse to URL to Search """


def pattern_matching(url):
    response = requests.get(url);
    page = response.text
    # print response
    soup = BeautifulSoup( page, 'lxml');
    actor_segment = soup.find( "td", attrs={"class": "result_text"} )
    relevant_actor = actor_segment.find( 'a' )['href']
    actor_url = "http://www.imdb.com" + relevant_actor + "#actor"
    part1 = "http://www.imdb.com" + relevant_actor
    # print "Stage 2 Url :" + actor_url
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
    view = soup3.find( "span", attrs={"itemprop": "name"} ).get_text()
    print (Back.BLACK + "Currently you are viewing profile of : "  + Style.RESET_ALL)+ (Fore.GREEN + view + Style.RESET_ALL )
    print actors_name + " Has worked in " + (Fore.GREEN + found + Style.RESET_ALL ) + "Movies as an actor."


    """" This Function Used to fetch the list Number movies & Director Done by this Actor """


def movie_listing(url):
    response = requests.get(url);
    page = response.text
    soup = BeautifulSoup( page, 'lxml' );

    movie_list = soup.find( "div", attrs={"data-category": "actor"}).find_next_sibling("div").find_all("div")
    # print movie_list
    # Tv_list = soup.find("div", attrs={"data-category": "actor"}).find_next_sibling("div").find_all("div", attrs={"class": "filmo-episodes"})
    # print Tv_list
    a = []
    for movie in movie_list:
        anchorArray = movie.find_all( 'a', href= True)
        if len( anchorArray ) > 0:
            a += anchorArray
    # 'a' gives you the list of the "a" <tag> than we need to fetch href so we passing to created_movie_url
    created_movie_url = []
    for index in range( len( a ) ):
        created_movie_url.append("http://www.imdb.com"+a[index].get('href'))
        # print(index, "http://www.imdb.com"+a[index].get('href'))

    valid_url1 = []
    sub = 'pro'
    for valid_url in created_movie_url:
        if sub not in valid_url:
            valid_url1.append(valid_url)
            # print(valid_url1)

    valid_url_fetched = []
    hashexclusion = '#'
    for valid_url2 in valid_url1:
        if hashexclusion not in valid_url2:
            valid_url_fetched.append(valid_url2)
    # print(valid_url_fetched)

    """"" 'valid_url_fetched' is giving the url of each movie of the actor.Need to pass it to Url to fetch rating"""

    rated=[]
    for rating in valid_url_fetched:
        # print rating
        response = requests.get(rating);
        # print response
        page = response.text
        soupr = BeautifulSoup( page, 'lxml' );
        try:
            movie_rating = soupr.find( "span", attrs={"itemprop": "ratingValue"} ).get_text()
            rated.append(movie_rating)
            # print movie_rating
        except AttributeError:
            pass

    rated = map(lambda val: float(val), rated)
    average= sum(rated) / len(rated)
    average1 = round(average,1)
    max_rate= max(rated)
    min_rate = min(rated)

    print (Back.BLACK + "Average Rating of " + Style.RESET_ALL)+actors_name +":" + (Fore.GREEN + str(average1)+ Style.RESET_ALL)
    print (Back.BLACK + "maximum Rating of " + Style.RESET_ALL)+actors_name +" is :" + (Fore.GREEN + str(max_rate)+ Style.RESET_ALL)
    print (Back.BLACK + "Minimum Rating of " + Style.RESET_ALL)+actors_name +" is :" + (Fore.GREEN + str(min_rate)+ Style.RESET_ALL)



actors_name = raw_input( "Enter Hero Name :")
filmography(pattern_matching(get_actor_url()))
movie_listing(pattern_matching(get_actor_url()))

