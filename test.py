import pandas as pd

def read_excel_file(file_path):

    try:
        df = pd.read_excel(file_path, "Sheet1")
        return (df.iloc[:, 0].tolist(), df.iloc[:, 1].tolist())
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return Exception("Error reading Excel file" + str(e))
    
# (names, domains) = read_excel_file("excel/client_domains_000.xlsx")
# (names2, urls) = read_excel_file("output/out_client_urls_001.xlsx")
# names2 = list(set(names2))

# ignored = []

# for name in names:
#     if name not in names2:
#         ignored.append(name)
        
# print(ignored)

# ['Black Nova Capital Pty Ltd ', 'Afterwork Ventures Pty Ltd ', 'Empress Capital Pty Ltd ', 'Ten 13 Investment Management Pty Ltd ', 'For Purpose Investment Partners Ltd ', 'Holon Global Investment Partners Pty Ltd ', 'Olive Financing Entity Ltd ', 'Social Impact Funds Management Pty Ltd ']

a = [1, 2, 3, 4, 5]
b = [0, 0, 0, 0, 0, 0]
print(a + b)