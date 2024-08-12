import pandas as pd
from urllib.parse import urlsplit, urlunsplit, urljoin, urlparse

def read_excel_file(file_path):

    try:
        df = pd.read_excel(file_path, "Sheet1")
        return (df.iloc[:, 0].tolist(), df.iloc[:, 1].tolist())
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return Exception("Error reading Excel file" + str(e))
    
def write_to_excel(file_path, data):
        
    try:
        df = pd.DataFrame(data)
        df.to_excel(file_path, index=False)
    except Exception as e:
        print(f"Error writing to Excel file: {e}")
        return Exception("Error writing to Excel file" + str(e))
    

(names, urls) = read_excel_file("excel/client_domains_003_missing.xlsx")
input_list = []

for i in range(len(names)):
    input_list.append({"name": names[i], "url": urls[i]})
    
(scanned_names, scanned_urls) = read_excel_file("output/out_client_urls_004_missing.xlsx")
out_list = []

for i in range(len(scanned_names)):
    out_list.append({"name": scanned_names[i], "url": scanned_urls[i]})
    
final_list = []    
for i in range(len(out_list)):
    
    if out_list[i]["url"] != "/":
        
        domain = ""
        
        for item in input_list:
            
            if item["name"] == out_list[i]["name"]:
                domain = item["url"]
                break
            
        if domain != "":
            
            if domain == out_list[i]["url"]:
                final_list.append({"Client Name": out_list[i]["name"], "Website Address (url)": out_list[i]["url"]})
            else:
                final_list.append({"Client Name": out_list[i]["name"], "Website Address (url)": urljoin(domain, out_list[i]["url"])})

print(len(final_list))
write_to_excel("final/final_004_missing.xlsx", final_list)    
