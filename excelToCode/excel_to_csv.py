#coding:utf-8

import sys
from xlrd import *
import glob
def buildCsv(filePath):
    try:        
        data = open_workbook(filePath)
        sheet = data.sheet_by_index(0)
        csvFile = open(filePath[0:-5] + ".csv", "wb")
        for i in range(0,sheet.nrows):
            row = sheet.row_values(i)
            #处理整数变成x.0的问题
            for v in range(0,len(row)):
                if type(row[v]) is float:
                    if row[v] % 1 == 0:
                        row[v] = int(row[v])
            #转换类型为str
            for v in range(0,len(row)):
                if type(row[v]) is not str:
                    row[v] = str(row[v])

            rowStr = '\t'.join(row)
            if rowStr.find('#') == -1:
                csvFile.write(rowStr)
                csvFile.write('\n')
        csvFile.close()
    except IOError as err:
        print("Error:" + str(err))
#导出csv目录下所有文件
reload(sys)
sys.setdefaultencoding('utf-8')

csvFiles = glob.glob("csv\\*.xlsx")
for eachFile in csvFiles:
    buildCsv(eachFile)
	
print("excel_to_csv ok.")
#input()
