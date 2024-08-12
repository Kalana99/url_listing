from genericpath import isfile
from ntpath import join
from os import listdir
import pandas as pd

INPUT_DOMAINS = "excel/client_domains_003_missing.xlsx"
OUTPUT_URLS = "output/out_client_urls_004_missing.xlsx"
IGNORED_URLS = "ignored/ignored_client_urls_004_missing.xlsx"

TEST_INPUT_DOMAINS = "excel/test0.xlsx"
TEST_OUTPUT_URLS = "output/test0.xlsx"
TEST_IGNORED_URLS = "ignored/test0.xlsx"

class ExcelHandler:
    
    @staticmethod
    def read_web():
        return ExcelHandler.read_excel_file(INPUT_DOMAINS)
    
    @staticmethod
    def write_web(out_list, ignored_list):
        ExcelHandler.write_to_excel(OUTPUT_URLS, out_list)
        ExcelHandler.write_to_excel(IGNORED_URLS, ignored_list)
    
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
        
    # write list of dictionaries to given excel sheet in a excel file
    @staticmethod
    def write_to_excel(file_path, data):
        
        try:
            df = pd.DataFrame(data)
            df.to_excel(file_path, index=False)
        except Exception as e:
            print(f"Error writing to Excel file: {e}")
            return Exception("Error writing to Excel file" + str(e))
    
    @staticmethod    
    def merge_excel_files(input_files, output_file):
        merged_data = []
        
        for file_path in input_files:
            try:
                df = pd.read_excel(file_path, "Sheet1")
                merged_data.append(df)
            except Exception as e:
                print(f"Error reading Excel file: {e}")
                return Exception("Error reading Excel file" + str(e))
        sorted(merged_data, key=lambda x: x.iloc[0, 0])
        try:
            merged_df = pd.concat(merged_data)
            merged_df.to_excel(output_file, index=False)
        except Exception as e:
            print(f"Error writing to Excel file: {e}")
            return Exception("Error writing to Excel file" + str(e))
        
    # Get the list of filename in the given directory
    @staticmethod
    def get_files_in_dir(directory):
        return [join(directory, f) for f in listdir(directory) if isfile(join(directory, f))]
    
if __name__ == '__main__':
    
    input_files = ExcelHandler.get_files_in_dir("output") + ExcelHandler.get_files_in_dir("ignored")
    output_file = "final/final_soretd.xlsx"
    
    ExcelHandler.merge_excel_files(input_files, output_file)
