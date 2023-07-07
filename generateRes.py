import os
import openpyxl

def main():
    workbook1 = openpyxl.load_workbook("./sni_info.xlsx")
    workbook2 = openpyxl.load_workbook("./database/app_protocol.xlsx")
    sheet1 = workbook1['HTTPS']
    sheet2 = workbook2['app_protocol']
    tmp_list = sheet2['B2:B560']
    name_list = []
    for item in tmp_list:
        for name in item:
            name_list.append(name.value.replace(" ",""))
    print(name_list)
    id_list = []
    tmp_list = sheet2['A2:A560']
    for item in tmp_list:
        for id in item:
            id_list.append(id.value)        
    pre_name = ""
    id = 0
    count = 3893
    lines = sheet1[2:101784]
    for line in lines:
        sni = line[2].value
        name = line[4].value.replace(" ","")
        if(name != pre_name):
            if(name in name_list):
                id = id_list[name_list.index(name)]
            else:
                id = id_list[name_list.index(f"{name}app")]
        count += 1
        with open("./DF_SSL_REGION_SNI_国外", encoding="utf-8", mode="a") as f:
            f.write(f"{count}   {id}    SNI    {sni}    0   0   0   1\n")    
    print("over")
if __name__ == "__main__":
    main()
