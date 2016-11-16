import re
import xlrd


class PreProcessor:

    File_PATH = '../data2/training-Obama-Romney-tweets.xlsx'

    def __init__(self, file_path):
        self.File_PATH = file_path
        self.spreadsheet = xlrd.open_workbook(file_path)
