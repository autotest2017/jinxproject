#!/urs/bin/env python
#encoding:utf - 8

import  xlwt

datas = [[u'学号',u'姓名',u'成绩'],['12',u'张三','98'],['13',u'李四','99']]
file_path = 'F:\homework\score_table.xls'

f = xlwt.Workbook()
sheet1 = f.add_sheet('count1')

row_count = len(datas)
col_count = len(datas[0])
for row in range(0,row_count):
      col_count = len(datas[row])
      for  col in range(0,col_count):
          if row == 0:
              sheet1.write(row, col, datas[row][col])
          else:
              sheet1.write(row, col,datas[row][col] )
f.save(file_path)

if __name__ == 'main':
    write_excel()