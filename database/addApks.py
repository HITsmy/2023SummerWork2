import os
import openpyxl


def main():
    workbook = openpyxl.load_workbook("./app_protocol.xlsx")
    sheet = workbook['app_protocol']
    apk_names = sheet['B']
    name_list = []  # name of xlsx
    for item in apk_names:
        name_list.append(item.value)
    local_name_list = os.listdir("../test/")
    count = 352
    for item in local_name_list:
        if(not (item[0:-4] in name_list or item[0:-4]+"app" in name_list)):
            count += 1
            data = [count, item[0:-4]]
            sheet.append(data)
    workbook.save("./app_protocol.xlsx")
    print("over!")
if __name__ == "__main__":
    main()