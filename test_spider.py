from FireCrawlSpider import FireCrawlSpider
from DomainGraphBuilder import DomainGraphBuilder
from JsonHandler import JsonHandler


DOMAIN = "https://www.antler.co/"
JSON_FILE_PATH = "json/antler_graph.json"

def write_to_json(data, file_path):
    try:
        handler = JsonHandler(file_path)
        handler.write_to_json(data)
    except Exception as e:
        raise e

def get_domain_graph(domain):
    
    try:
        spider = FireCrawlSpider()
        links = spider.get_links(domain)
        
        builder = DomainGraphBuilder(domain)
        graph = builder.build_graph(links)
        
        return graph
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    
    try:
        graph = get_domain_graph(DOMAIN)
        write_to_json(graph, JSON_FILE_PATH)
    except Exception as e:
        print(e)
        