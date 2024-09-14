import os
import inspect
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

# Load environment variables from .env file
load_dotenv()
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')

class FireCrawlSpider:
    
    def __init__(self):
        self.app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)

    def get_links(self, domain):
        
        try:
            map_result = self.app.map_url(domain)
            
            print(f'[{self.__class__.__name__} - line {inspect.currentframe().f_lineno}] No. of links: {len(map_result)}')
            return map_result
        except Exception as e:
            raise e
    
if __name__ == "__main__":
    
    try:
        spider = FireCrawlSpider()
        links = spider.get_links("https://www.antler.co/")
        print(len(links))
    except Exception as e:
        print(e)

# {
#   "status": "success",
#   "links": [
#     "https://firecrawl.dev",
#     "https://www.firecrawl.dev/pricing",
#     "https://www.firecrawl.dev/blog",
#     "https://www.firecrawl.dev/playground",
#     "https://www.firecrawl.dev/smart-crawl",
#     ...
#   ]
# }
