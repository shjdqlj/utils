import os

import xlrd

name = "胡骏"
student_num = "116039910015"
dirname = "2016.09-2017.08研究生综合测评公示区"
found_files = set()

for dirpath, dirnames, filenames in os.walk(dirname):
    for filename in filenames:
        fname = os.path.join(dirpath, filename)
        if fname.endswith('.xls') or fname.endswith('.xlsx'):
            # print(fname + " -----> yes")
            wb = xlrd.open_workbook(fname)

            for sheet in range(wb.nsheets):
                sh = wb.sheet_by_index(sheet)

                # 获取行数
                nrows = sh.nrows
                # 获取列数
                ncols = sh.ncols
                # print("nrows %d, ncols %d" % (nrows, ncols))

                # 获取各行数据
                # row_list = []
                for i in range(nrows):
                    # row_data = sh.row_values(i)
                    # row_list.append(row_data)
                    for j in range(ncols):
                        cell_value = str(sh.cell_value(i, j))
                        if cell_value.strip() == name or cell_value.strip() == student_num:
                            found_files.add(fname)

print("found {} files".format(len(found_files)))
for filename in found_files:
    print("=====> found: [{}]".format(filename))
