import feedparser
import xml.etree.ElementTree as ET
import requests

class RSSFeederIntoXML():


    def __init__(self):
        
        if self.amIOnline() == False:
            self.__showAll__()
        else:
            self.__showByChoice__() 
        

       
            

    def feedMeURL(self,*sites):
        data = ET.Element('RSS')

        for resource in sites:
            feed = feedparser.parse(resource)
            #print(resource)

            for entry in feed.entries:
                temp = ET.SubElement(data, 'Items')
                article_title = entry.title

                ET.SubElement(temp, 'Title').text = article_title
                article_link = entry.link
                ET.SubElement(temp, 'Link').text = article_link

                

                article_published_at = entry.published  # Unicode string
                #article_published_at_parsed = entry.published_parsed  # Time object
                ET.SubElement(temp, 'Date').text = article_published_at

                
                content = entry.summary
                ET.SubElement(temp, 'Content').text = content

        ET.ElementTree(data).write('Data.xml') 
       


    def amIOnline(self):     
        try:
            requests.get('https://www.google.com/').status_code
            print("You're Online")
            return True
        except:
            print("You're Offline!!")
            return False

    
    def __showAll__(self):
        Tree = ET.parse('Data.xml')
        items = Tree.findall('Items')
        print("Wanna show all ? Enter 1: ") 
        val = input()

        if(val == "1"):
            for article in items:
                dateANDtime = article.find('Date').text
                link = article.find('Link').text
                title = article.find('Title').text
                content = article.find('Content').text

                print("{}[{}]".format(dateANDtime, link))
                print("TITLE: {}".format(title))
                print("CONTENT: {} ".format(content)) 
                print("\n\n")   
           

    def __showByChoice__(self):
        Tree = ET.parse('Data.xml')
        items = Tree.findall('Items')
        print("1. Wanna show all ? Enter 1: ")
        print("2. Wanna show by Publisher ? Enter 2: ")
        print("3. Wanna show by Keyword ? Enter 3: ")
        print("4. Wanna show by Publisher and Keyword ? Enter 4: ")
        val = input()
        
        if(val == "1"):
           self.__showAll__()
        elif(val == "2"):
            publish = input("Enter name of publisher: ")
            for article in items:
                link = article.find('Link').text
                if(publish in link):
                    dateANDtime = article.find('Date').text
                    title = article.find('Title').text
                    content = article.find('Content').text
                    print("{}[{}]".format(dateANDtime, link))
                    print("TITLE: {}".format(title))
                    print("CONTENT: {}".format(content))   
                    print("\n\n")             
        elif(val == "3"):
            keyword = input("Enter Keyword: ")
            for article in items:
                content = article.find('Content').text    
                if(keyword in content):
                    dateANDtime = article.find('Date').text
                    title = article.find('Title').text
                    link = article.find('Link').text
                    print("{}[{}]".format(dateANDtime, link))
                    print("TITLE: {}".format(title))
                    print("CONTENT: {}".format(content)) 
                    print("\n\n")            
        elif(val == "4"):
            publish = input("Enter name of publisher: ")
            keyword = input("Enter Keyword: ")
            for article in items:
                link = article.find('Link').text
                content = article.find('Content').text
                if((publish in link) and (keyword in content)):                
                    dateANDtime = article.find('Date').text
                    title = article.find('Title').text                    
                    print("{}[{}]".format(dateANDtime, link))
                    print("TITLE: {}".format(title))
                    print("CONTENT: {}".format(content))
                    print("\n\n") 
        else:
            print("Some input wasn't right")



RSSFeederIntoXML()
#RSSFeederIntoXML.feedMeURL("","https://servis.idnes.cz/rss.aspx?c=zpravodaj", "https://www.novinky.cz/rss")