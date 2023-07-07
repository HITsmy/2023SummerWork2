import os
import openpyxl


def main():
    workbook1 = openpyxl.load_workbook("./app_pro_type_assc.xlsx")
    workbook2 = openpyxl.load_workbook("./app_protocol.xlsx")
    sheet1 = workbook1['app_pro_type_assc']
    sheet2 = workbook2['app_protocol']

    count = 345
    sheet2_list = sheet2[278:538]
    for item in sheet2_list:
        print(f"Now is on line {item[1].value}")
        print("Please input type_id")
        type_id = input()
        count += 1
        data = [count, item[0].value, type_id]
        sheet1.append(data)


    workbook1.save("./app_pro_type_assc.xlsx")
    print("over!")
if __name__ == "__main__":
    main()