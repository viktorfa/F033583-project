# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class IdPipeline(object):
    id_count = 0

    def process_item(self, item, spider):
        item['id'] = self.id_count
        self.id_count += 1

        return item
