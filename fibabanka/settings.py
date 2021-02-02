BOT_NAME = 'fibabanka'
SPIDER_MODULES = ['fibabanka.spiders']
NEWSPIDER_MODULE = 'fibabanka.spiders'
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'fibabanka.pipelines.DatabasePipeline': 300,
}
