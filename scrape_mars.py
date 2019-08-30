from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd

#take each part and put into into its wn py function
def mars():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def mars_soup_news():
    # !/usr/bin/env python
    # coding: utf-8

    # In[1]:

    # Set the executable path and initialize the chrome browser in splinter
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser("chrome", **executable_path)

    # In[2]:

    browser.visit("https://mars.nasa.gov/news")

    # In[3]:

    html = browser.html

    # In[4]:

    news_soup = BeautifulSoup(html, 'html.parser')

    # In[5]:

    title = news_soup.find("div", class_="content_title").get_text()
    # find = part of BS to find and assign info to varable

    # In[6]:

    title

    # In[7]:

    text = news_soup.find("div", class_="article_teaser_body")

    # In[8]:

    text

    # In[9]:

    browser.visit("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    html_b = browser.html

    # In[10]:

    # image = news_soup.find("div", src="/spaceimages/images/wallpaper/PIA23344-640x350.jpg")

    # In[11]:

    site = "https://www.jpl.nasa.gov"

    # In[12]:

    image_soup = BeautifulSoup(html_b, 'html.parser')
    button = image_soup.find('a', class_='button fancybox')
    button

    # In[13]:

    image = image_soup.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
    image

    # In[14]:

    awesome_image = site + image
    awesome_image

    # In[15]:

    browser.visit("https://twitter.com/marswxreport?lang=en")
    html_c = browser.html

    # In[16]:

    tweet_soup = BeautifulSoup(html_c, 'html.parser')

    # In[17]:

    twitter = tweet_soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')

    # In[18]:

    weather = twitter.text.strip()

    # In[19]:

    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
    # url ="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # In[20]:

    # data = pd.read_html(url)

    # In[21]:

    html_d = browser.html
    hem_soup = BeautifulSoup(html_d, 'html.parser')

    # In[22]:

    hem = hem_soup.find_all('h3')
    hem

    # In[23]:

    for_loop = [h3.text.strip() for h3 in hem]

    # In[24]:

    for_loop

    # In[ ]:


#one function for all 4, then a 5th function that excutes all of these

# helper function to build surf report
def build_report(mars_report):
    final_report = ""
    for p in mars_report:
        final_report += " " + p.get_text()
        print(final_report)
    return final_report
