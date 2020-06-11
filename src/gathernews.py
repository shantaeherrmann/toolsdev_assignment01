# Shantae Herrmann
# Professor Lim
# ATCM 3311.0U1
# Assignment 01
# 06/12/2020
# Description: This program scrapes and summarizes news articles

#Import the libraries
import nltk
import newspaper
from newspaper import Article
from newspaper import news_pool
import webbrowser

#Get the article
denGeek_web = newspaper.build('https://www.denofgeek.com/', memoize_articles=False, keep_article_html=True)
techRadar_web = newspaper.build('https://www.techradar.com/', memoize_articles=False, keep_article_html=True)
polygon_web = newspaper.build('https://www.polygon.com/', memoize_articles=False, keep_article_html=True)

#Prints article information to 'news_summary.txt' file
myFile = open('news_summary.txt','w')

nltk.download('punkt')

#Gets input from the user
userinput = input("Please enter any keyword(press enter to continue): ")
print("You entered the keyword: ", userinput)

#Get the DenOfGeek website
for article in denGeek_web.articles:
    title = article.title
    author = article.authors
    summary = article.summary
    article.download()
    article.parse()
    article.nlp()
    article.keywords
    article.html
    article.text
    
    #Print the information of articles based on keywords
    if userinput in article.keywords:
        print(article.title, ' - ', article.authors)
        print(article.summary)
        print('\n')
        print(article.url)
        print('\n')

#Write article information to news_summary.txt file
        myFile.write(article.title)
        myFile.write(' - ')
        myFile.write(str(article.authors))
        myFile.write('\n')
        myFile.write(article.summary)
        myFile.write('\n')
        myFile.write('\n')

#Get the Tech Radar website
for article in techRadar_web.articles:
    title = article.title
    author = article.authors
    summary = article.summary
    article.download()
    article.parse()
    article.nlp()
    article.keywords
    article.html
    article.text

    #Print the information of articles based on keywords
    if userinput in article.keywords:
        print(article.title, ' - ', article.authors)
        print(article.summary)
        print('\n')
        print(article.url)
        print('\n')

#Write article information to news_summary.txt file
        myFile.write(article.title)
        myFile.write(' - ')
        myFile.write(str(article.authors))
        myFile.write('\n')
        myFile.write(article.summary)
        myFile.write('\n')
        myFile.write('\n')

#Get the Polygon website
for article in polygon_web.articles:
    title = article.title
    author = article.authors
    summary = article.summary
    article.download()
    article.parse()
    article.nlp()
    article.keywords
    article.html
    article.text

    #Print the information of articles based on keywords
    if userinput in article.keywords:
        print(article.title, ' - ', article.authors)
        print(article.summary)
        print('\n')
        print(article.url)
        print('\n')

#Write article information to news_summary.txt file
        myFile.write(article.title)
        myFile.write(' - ')
        myFile.write(str(article.authors))
        myFile.write('\n')
        myFile.write(article.summary)
        myFile.write('\n')
        myFile.write('\n')

myFile.close()

#opens the url in a browser
newinput = input("Would you like to open the articles in a browser? 'Y' or 'N': ")

if newinput.upper() in ['Y']:
    webbrowser.open_new(article.url)