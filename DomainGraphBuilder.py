from urllib.parse import urlparse

class DomainGraphBuilder:
    
    def __init__(self, domain):
        parsed_domain = urlparse(domain)
        self.domain = f"{parsed_domain.scheme}://{parsed_domain.netloc}"
        self.graph = {"domain": self.domain, "children": []}

    def add_url(self, url):
        path_parts = urlparse(url).path.strip("/").split("/")
        current_level = self.graph["children"]

        for part in path_parts:
            # Check if this part of the path is already in the current level
            existing_path = next((node for node in current_level if node["path"] == f"/{part}"), None)
            
            if not existing_path:
                # If it doesn't exist, create it
                new_node = {"path": f"/{part}", "children": []}
                current_level.append(new_node)
                current_level = new_node["children"]
            else:
                # If it exists, move to the next level
                current_level = existing_path["children"]

    def build_graph(self, urls):
        for url in urls:
            self.add_url(url)
        return self.graph

# Example usage:
urls = [
    "https://example.org",
    "https://example.org/page1",
    "https://example.org/page2",
    "https://example.org/page3",
    "https://example.org/page4",
    "https://example.org/page1/subpage1",
    "https://example.org/page1/subpage2",
    "https://example.org/page2/subpage1",
    "https://example.org/page2/subpage2",
    "https://example.org/page3/subpage1"
]

builder = DomainGraphBuilder("https://example.org")
graph = builder.build_graph(urls)

print(graph)

# {
#     "domain": "https://example.org",
#     "children": [
#         {
#             "path": "/page1",
#             "children": [
#                 {
#                     "path": "/subpage1",
#                     "children": []
#                 },
#                 {
#                     "path": "/subpage2",
#                     "children": []
#                 }
#             ]
#         },
#         {
#             "path": "/page2",
#             "children": [
#                 {
#                     "path": "/subpage1",
#                     "children": []
#                 },
#                 {
#                     "path": "/subpage2",
#                     "children": []
#                 }
#             ]
#         },
#         {
#             "path": "/page3",
#             "children": [
#                 {
#                     "path": "/subpage1",
#                     "children": []
#                 }
#             ]
#         },
#         {
#             "path": "/page4",
#             "children": []
#         }
#     ]
# }

