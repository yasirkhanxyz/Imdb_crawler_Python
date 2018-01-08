from bs4 import BeautifulSoup
import requests
import re


def get_actor_url():
    actors_name = raw_input( "Enter Hero Name :" )
    endfix = '&s=all'
    actors_name1 = actors_name.replace( " ", "+" )
    get_search_list_url = "http://www.imdb.com/find?ref_=nv_sr_fn&q=" + actors_name1 + endfix
    print get_search_list_url
    return get_search_list_url
    """" This Function Used to fetch the Actor name and parse to URL to Search """


def pattern_matching(url):
    response = requests.get(url);
    page = response.text
    print response
    soup = BeautifulSoup( page, 'lxml');
    actor_segment = soup.find( "td", attrs={"class": "result_text"} )
    relevant_actor = actor_segment.find( 'a' )['href']
    # actor_segment = soup.find_all("td", attrs={"class": "result_text"})
    # relevant_actor = actor_segment[0].find('a')['href']
    # create actor url
    actor_url = "http://www.imdb.com" + relevant_actor + "#actor"
    print actor_url
    return actor_url
    # print relevant_actor
    """" This Function Used to fetch the Actor name and parse to URL to Search """


# pattern_matching(get_actor_url())


def filmography(url):
    response = requests.get(url);
    page = response.text
    soup1 = BeautifulSoup(page, 'lxml');
    print response
    # movie_segment = soup1.select_one(".filmo-head-actor")
    movie_segment = soup1.find("div",attrs={"id":"filmo-head-actor"})
    print movie_segment.find_next_sibling("div")
    #print movie_segment

    # for strong_tag in soup1.find( "div",attrs={"id":"filmo-head-actor"}):
    #     print strong_tag.next_sibling

    # print strong_tag.next_sibling
    # segmented = movie_segment.soup1.get_text('div')
    # print movie_segment
    # print segmented
    """" This Function Used to fetch the list Number movies & Director Done by this Actor """


filmography(pattern_matching(get_actor_url()))

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
