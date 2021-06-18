class CheckContentPipeline(object):
    def process_item(self, item, spider):
        if item['newstext'] is None:
            raise DropItem('Missing Info in here')
        else:
            return item

