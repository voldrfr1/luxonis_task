import scrapy
from fetching.items import FetchingItem


def genURL(num_of_pages=5):
    '''
    Generator for URLs of 500 first apartments.
    
    Parameters
    ----------
    num_of_pages : INT, optional
        Number of pages to scrape. The default is 5.

    Yields
    ------
    next_url : YIELD
        Generator of URL addresses.

    '''
    urls=[]
    for num in range(1,num_of_pages+1):
        #get source json from inspect tools/network/XHR --- estates
        #Important!!! content load dynamically
        next_url='https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=100&page=%s' %num
        urls.append(next_url)
    return urls


class SrealitySpider(scrapy.Spider):
    name = "sreality"

    def start_requests(self):
        urls = genURL()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        
        
    def parse(self, response):
        """
        Parse the current response object, and return any Item and/or Request objects
        """

        data=response.json()
        item=FetchingItem()
        # iterate over the list of images
        #get just the first image
        item['name']=[]
        item['img_url']=[]
        for flat in data["_embedded"]['estates']:
            #print(flat["_links"]['images'][0])
            #print(flat["name"])
            item['img_url'].append(str(flat["_links"]['images'][0]['href']))
            item['name'].append(str(flat["name"]).replace("\xb2", ""))
        
        yield item
            
            


