import pandas as pd

class ExcelHandler:
    
    @staticmethod
    def read_web():
        return ExcelHandler.read_excel_file("excel/client_domains_000.xlsx")
    
    @staticmethod
    def read_news():
        return ExcelHandler.read_excel_file("utils/news.xlsx")
    
    @staticmethod
    def read_excel_file(file_path):

        try:
            df = pd.read_excel(file_path, "Sheet1")
            return (df.iloc[:, 0].tolist(), df.iloc[:, 1].tolist())
        except Exception as e:
            print(f"Error reading Excel file: {e}")
            return Exception("Error reading Excel file" + str(e))
