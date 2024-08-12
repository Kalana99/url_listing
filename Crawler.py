import urllib.request
from urllib.parse import urlsplit, urlunsplit, urljoin, urlparse
import re
from ExcelHandler import ExcelHandler

class Crawler:

    def __init__(self, exclude=None, no_verbose=False):

        self.url = None
        self.host = None
        self.exclude = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.pdf', '.css', '.js', '.ico', '.woff', '.woff2', '.ttf', '.eot']
        self.no_verbose = no_verbose
        self.found_links = []
        self.visited_links = []
        self.ignored_links = []

    def start(self, url):
        
        self.url = self.normalize(url)
        self.host = urlparse(self.url).netloc
        self.found_links.append(self.url)
        self.visited_links.append(self.url)
        
        self.crawl(self.url)

        return self.found_links


    def crawl(self, url):
        if not self.no_verbose:
            print("Parsing " + url)
            
        # Define custom headers
        # headers = {
        #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',  # A common user-agent string
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',  # Accept header
        #     'Accept-Language': 'en-US,en;q=0.5'  # Accept-Language header
        # }
        
        # req = urllib.request.Request(url, headers=headers)
        
        try:
            response = urllib.request.urlopen(url, timeout=15)
            # response = urllib.request.urlopen(req, timeout=15)
        except Exception as e:
            print(e)
            print('404 error')
            self.ignored_links.append(url)
            return
        
        page = str(response.read())

        pattern = '<a [^>]*href=[\'|"](.*?)[\'"].*?>'

        found_links = re.findall(pattern, page)
        links = []

        for link in found_links:
            is_url = self.is_url(link)

            if is_url:
                is_internal = self.is_internal(link)

                if is_internal:
                    self.add_url(link, links, self.exclude)
                    self.add_url(link, self.found_links, self.exclude)

        for link in links:
            if link not in self.visited_links:
                link = self.normalize(link)

                self.visited_links.append(link)
                self.crawl(urljoin(self.url, link))

    def add_url(self, link, link_list, exclude_pattern=None):
        link = self.normalize(link)

        if link:			
            not_in_list = link not in link_list
            # not_in_list = not self.is_url_in_list(link, link_list)

            excluded = False

            if exclude_pattern:
                
                for pattern in exclude_pattern:
                    excluded = re.search(pattern, link)
                    if excluded:
                        break

            if not_in_list and not excluded:
                link_list.append(link)
    
    def is_url_in_list(self, url, url_list):
        
        if url[-1] == '/':
            url = url[:-1]
        
        for link in url_list:
            
            if link[-1] == '/':
                link = link[:-1]
                
            if url == link:
                return True
        
        return False

    def normalize(self, url):
        scheme, netloc, path, qs, anchor = urlsplit(url)
        return urlunsplit((scheme, netloc, path, qs, anchor))

    def is_internal(self, url):
        host = urlparse(url).netloc
        return host == self.host or host == ''	

    def is_url(self, url):
        scheme, netloc, path, qs, anchor = urlsplit(url)
        
        if url != '' and scheme in ['http', 'https', '']:
            return True 
        else:
            return False
        
    def is_url_force(self, url):
        scheme, netloc, path, qs, anchor = urlsplit(url)
        
        if url != '' and scheme in ['http', 'https']:
            return True 
        else:
            return False
        
if __name__ == '__main__':
    
    # url = "http://www.merkle.com.au"
    # crawler = Crawler()
    # out = crawler.start(url)
    
    # for i in out:
    #     print(i)
    
    scanned_urls = []
    
    # (scanned_names, scanned_urls) = ExcelHandler.read_excel_file("output/out_client_urls_001.xlsx")
    # (scanned_names2, scanned_urls2) = ExcelHandler.read_excel_file("output/out_client_urls_002_ignored.xlsx")
    # (scanned_names3, scanned_urls3) = ExcelHandler.read_excel_file("output/out_client_urls_003_ignored.xlsx")
    
    # scanned_urls = scanned_urls + scanned_urls2 + scanned_urls3
    
    out_list = []
    ignored_list = []
    (names, domains) = ExcelHandler.read_web()
    
    for i in range(len(names)):
        
        name = names[i].strip()
        domain = domains[i].strip()
        crawler = Crawler()
        
        url_list = crawler.start(domain)
        
        for url in url_list:
            
            # if crawler.is_url_force(url):
            out_list.append({'Client Name': name, 'Website Address (url)': url})
            
        for url in crawler.ignored_links:
            ignored_list.append({'Client Name': name, 'Website Address (url)': url})
            
    print(len(out_list))
    print(len(ignored_list))
    
    # count distinct names in the out_list
    print(len(set([x['Client Name'] for x in out_list])))
    print(len(set([x['Client Name'] for x in ignored_list])))
    
    ExcelHandler.write_web(out_list, ignored_list)
