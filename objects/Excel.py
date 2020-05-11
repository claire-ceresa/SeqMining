import xlsxwriter as x
import datetime as d

class Excel:

    def __init__(self, title=None):
        self.title = self.set_title(title)
        self.workbook = x.Workbook(self.title)
        self.worksheets = []

    def set_title(self, title):
        if title is None:
            now = d.datetime.now()
            return now.strftime("%Y%m%d_%H%M%S.xlsx")
        else:
            return title

    def add_worksheet(self, title=None):
        """Add a worksheet to the workbook"""
        worksheet = self.workbook.add_worksheet(title)
        self.worksheets.append(worksheet)
        return worksheet

    def close(self):
        """Close the workbook"""
        self.workbook.close()

    def add_data(self, worksheet, datas):
        """
        Adding data to a worksheet
        :param worksheet : Worksheet object
        :param datas : dictionnary {'column_names':[], 'rows':[[]]}
        """
        columns_name = datas["column_names"]
        format_columns_name = self.workbook.add_format({'bold':True, 'valign':'center'})
        worksheet.write_row(0, 0, columns_name)
        worksheet.set_row(0, None, format_columns_name)

        for row, row_data in enumerate(datas["rows"]):
            worksheet.write_row(row+1, 0, row_data)
            print("ok")