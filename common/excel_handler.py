from pprint import pprint
import openpyxl
class Exexl_handler:
    def __init__(self,excel_file):
        self.workbook = openpyxl.open(excel_file)    #打开表格
    def read(self,sheet_name):
        work_register = self.workbook[sheet_name]     #获取sheet页
        data_sheet = list(work_register.values)       #获取所有数据
        header = data_sheet[0]
        row = data_sheet[1:]
        data_list = []
        for v in row:
            dict_case = dict(zip(header,v))
            data_list.append(dict_case)
        return data_list
if __name__ == '__main__':
    excel = Exexl_handler("cases.xlsx")
    sheet = excel.read("register")
    pprint(sheet)
    