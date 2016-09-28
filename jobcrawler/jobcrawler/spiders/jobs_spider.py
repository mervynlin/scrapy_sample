# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import os
import time

class JobsSpider(scrapy.Spider):
    name = "jobs"

    def start_requests(self):
        urls = [
            'http://www.jobstreet.com.sg/en/job-search/job-vacancy.php?src=16&ojs=6'
        ]

        minPage = 2
        maxPage = 151

        for x in range(minPage, maxPage):
            urls.append("http://www.jobstreet.com.sg/en/job-search/job-vacancy/%s/?ojs=6" % x)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'job-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


