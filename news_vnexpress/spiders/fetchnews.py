import scrapy


class FetchnewsSpider(scrapy.Spider):
    name = "fetchnews"
    allowed_domains = ["vnexpress.net"]
    start_urls = []
    
    # request function 
    def start_requests(self):
        url_list = ["https://vnexpress.net/thoi-su",
                    "https://vnexpress.net/the-gioi",
                    "https://vnexpress.net/kinh-doanh",
                    "https://vnexpress.net/bat-dong-san",
                    "https://vnexpress.net/khoa-hoc",
                    "https://vnexpress.net/giao-duc",
                    "https://vnexpress.net/suc-khoe",
                    "https://vnexpress.net/doi-song",
                    "https://vnexpress.net/so-hoa"]

        for base_url in url_list:
            urls = [base_url]
            category = base_url.split('/')[-1].replace('-', ' ').title()

            for i in range(10): # max = 21
                url = base_url + f'-p{i}'
                urls.append(url)

            for url in urls: 
                yield scrapy.Request(url = url, callback = self.parse, meta={'category': category})


    # Parse function
    def parse(self, response):
        title_news = response.xpath("//h2[contains(@class, 'title-news')]/a")
        if not title_news:
            title_news = response.xpath("//h3[contains(@class, 'title-news')]/a")
        
        for item in title_news:
            category = response.request.meta['category']

            title = item.xpath(".//@title").get()
            title = title.replace('\n', '').strip()

            href = item.xpath(".//@href").get()

            yield response.follow(url=href, callback=self.parse_link, meta={
                                                                            'category': category,
                                                                            'title': title,
                                                                            'href': href
                                                                        })
    
    def parse_link(self, response):
        category = response.request.meta['category']
        title = response.request.meta['title']
        href = response.request.meta['href']

        time_post = response.xpath("//span[contains(@class, 'date')]/text()").get()

        yield {
            'category': category,
            'title': title,
            'time': time_post,
            'href': href
        }

