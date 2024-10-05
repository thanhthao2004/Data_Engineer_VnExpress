# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
import json
# from bson.objectid import ObjectId
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import csv
import os

class MongoDBVnexpressDataWarehousePipeline:
    def __init__(self):
        # Connection String
        econnect = str(os.environ['Mongo_HOST'])
        # self.client = pymongo.MongoClient('mongodb://mymongodb:27017')
        self.client = pymongo.MongoClient('mongodb://'+econnect+':27017')
        self.db = self.client['vnexpressdatawarehouse'] #Create Database      
    
    def process_item(self, item, spider):
        
        collection =self.db['tblVnexpress'] #Create Collection or Table
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")       

class JsonDBVnexpressDataWarehousePipeline:
    def process_item(self, item, spider):
        with open('jsondatavnexpress.json', 'a', encoding='utf-8') as file:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            file.write(line)
        return item

class CSVDBVnexpressDataWarehousePipeline:
    def process_item(self, item, spider):
        with open('csvdatavnexpress.csv', 'a', encoding='utf-8', newline='') as file:
            fieldnames = ['title', 'author', 'date', 'location','disease_name', 'count_comments', 'total_like', 'content']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if isinstance(item, dict):
                writer.writerow([
                    item['title'],
                    item['author'],
                    item['date'],
                    item['location'],
                    item['disease_name'],
                    item['count_comments'],
                    item['total_like'],
                    item['content']
                ])
        return item