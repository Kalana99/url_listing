import pandas as pd
from urllib.parse import urlsplit, urlunsplit, urljoin, urlparse

def read_excel_file(file_path, two_columns=True):

    try:
        df = pd.read_excel(file_path, "Sheet1")
        if not two_columns:
            return df.iloc[:, 0].tolist()
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
    
(names, urls) = read_excel_file("excel/client_domains_000.xlsx")
input_list = []

for i in range(len(names)):
    input_list.append({"name": names[i], "url": urls[i]})
    
scanned_names = read_excel_file("excel/client_names_003_missing.xlsx", False)

final_list = []
for i in range(len(scanned_names)):
    
    for item in input_list:
        
        if item["name"] == scanned_names[i]:
            final_list.append({"Client Name": item["name"], "Website Address (url)": item["url"]})
            break
        
print(len(final_list))
write_to_excel("excel/client_domains_003_missing.xlsx", final_list)
