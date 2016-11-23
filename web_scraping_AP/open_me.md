## Web Scraping challenge
### IUST AP951

This is a markdown file, so if you open it with notepad, you will see some strange characters. To view the file properly do one of these:  
    - go to [here](https://jbt.github.io/markdown-editor) and copy all text in this file at the left side of the website to see the output in the right side :) 
    - Download a markdown viewer application for linux or windows
-----------------
### Crawler

1. Go to tabnak.ir
2. Find out about the html tags and classes containing the articles in the main page.
3. Create an empty XML file, named news.xml.
4. Using urllib2 and BeatifulSoup (or any other replacements) scrape the page and get these for each article in the page:  
    - Title of the newsarticle
    - Description of the news article
    - url of the news article
    - Generate a unique ID for each article
5. For each crawled article add these to the news.xml file:
```
<news>
    <id> {your unique ID} </id>
    <title> { article title } </title>
    <link> { article link } </link>
    <desc> { article description } </desc>
</news>
```
look at the sample_news.xml file. Your output must be similar.  

### Git

6. After you read this file, add your name to the end of it in th provided space and push it to the server so that I know you have read it.  

7. After you wrote the code, Create a directory named scrper **in your git project folder** and put two files in it:  
    - The python code for your scraper
    - the news.xml file

--------
```
############################
##### your name here #######
############################
```