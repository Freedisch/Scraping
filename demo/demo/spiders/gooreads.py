import scrapy

class GoodReadSpider(scrapy.Spider):{
  #identity
  name="gooreads"

  #reqquest
  def start_requests(self):
    urls=[
      'https://www.goodreads.com/quotes?page=11',
      'https://www.goodreads.com/quotes?page=12',
      'https://www.goodreads.com/quotes?page=13',
      'https://www.goodreads.com/quotes?page=14',
      'https://www.goodreads.com/quotes?page=15',
      'https://www.goodreads.com/quotes?page=16',
      'https://www.goodreads.com/quotes?page=17',
      'https://www.goodreads.com/quotes?page=18',
      'https://www.goodreads.com/quotes?page=19',
      'https://www.goodreads.com/quotes?page=20'
    ]

    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self,response)
      page_number=response.url.split("=")[1]
      _file="{0}.html".format(page_number)
      with open(_file,'wb') as f:
        f.write(reponse.body)
}