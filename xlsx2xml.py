import sys
import xlrd


if __name__ == '__main__':
    """
    [Requirements]
    1. Python 3.x
    2. xlrd

    [Installation]
    $ pip3 install xlrd

    [Usage]
    $ python3 xlsx2xml.py [input_file] [output_file]
    """

    if len(sys.argv) != 3:
        print("未输入文件名或文件无法打开")
        exit()

    input, output = sys.argv[1:]
    data = xlrd.open_workbook(input)
    table = data.sheets()[0]

    nrows = table.nrows
    if nrows:
        f = open(output, 'w')
        f.write("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n")
        f.write("<point xmlns:xsi=\"http://www.w3.org/2001XMLSchema-instance\">\n")
        for i in range(nrows):
            row = table.row_values(i)
            f.write("\t<point{}>\n".format(i+1))
            f.write("\t\t<x>{}</x>\n".format(row[0]))
            f.write("\t\t<y>{}</y>\n".format(row[1]))
            f.write("\t\t<z>{}</z>\n".format(row[2]))
            f.write("\t</point{}>\n".format(i+1))
        f.write("</point>")
        f.close()
    else:
        print("Excel文件为空")
