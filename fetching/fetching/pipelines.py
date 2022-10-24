# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2

class FetchingPipeline:
    
    def __init__(self):         
        self.conn = psycopg2.connect(database = "postgres", user = "postgres", 
                                password = "postgres", host = "database", port = "5432")
        print("Opened database successfully")
        self.cur = self.conn.cursor()


    def process_item(self, item, spider):
        '''
        Proccess the data

        Parameters
        ----------
        item : dict
        spider : spider

        Returns
        -------
        item : TYPE
            DESCRIPTION.

        '''
        for name, img in zip(item['name'],item['img_url']):
            self.cur.execute('INSERT INTO flats (NAME, IMG_URL)'
                             'VALUES (%s,%s)', 
                (name, img))
        ## Execute insert of data into database
        self.conn.commit()
        print('ITEM PROCCESSED SUCCESSFULLY!')
        return item
    
    
    def close_spider(self, spider):
        '''
        Closes connection

        Parameters
        ----------
        spider : spider

        Returns
        -------
        None.

        '''
        ## Close cursor & connection to database
        self.cur.close()
        self.conn.close()
