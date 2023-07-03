import os
import openpyxl
def main():
    workbook = openpyxl.load_workbook("./sni_info.xlsx")
    HTTPS = workbook['HTTPS']
    HTTP = workbook['HTTP']
    HTTPS_lines = HTTPS[2:1064]
    HTTP_lines = HTTP[2:811]
    pre_apk= ""
    print("开始处理https模块")
    for line in HTTPS_lines:
        if(line[4].value != pre_apk):
            print(f"Now on line {line[4].value}, input your keyword for these lines")
            keyword = input()
        sni_url = line[2].value
        tmp_list = sni_url.split('.')
        if(keyword in tmp_list):
            line[3].value = "是"
        else:
            line[3].value = "否"

        pre_apk = line[4].value
    pre_apk = ""
    print("开始处理http模块")
    for line in HTTP_lines:
        if(line[3].value != pre_apk):
            print(f"Now on line {line[3].value}, input your keyword for these lines")
            keyword = input()
        url = line[1].value
        tmp_list = url[7:].split('.')
        if(keyword in tmp_list):
            line[2].value = "是"
        else:
            line[2].value = "否"
        pre_apk = line[3].value
    workbook.save('sni_info.xlsx')

if __name__ == "__main__":
    main()