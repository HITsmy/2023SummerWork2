import os
import openpyxl

def main():
    txt_files = os.listdir("./output")
    HTTP_list = []
    HTTPS_list = []
    fileName_list = []
    for file in txt_files:
        fileName = file[0:-8]
        fileName_list.append(fileName)
        HTTP_listForFile = []
        HTTPS_listForFile = []
        with open(f"./output/{file}") as f:
            url_list = f.readlines()    #包含\n,需要进行处理
            for url in url_list:
                if(url[0:5] == 'https'):
                    HTTPS_listForFile.append(url[0:-1])
                elif(url[0:4] == 'http'):
                    HTTP_listForFile.append(url[0:-1])
        HTTP_list.append(HTTP_listForFile)
        HTTPS_list.append(HTTPS_listForFile)

    os.chdir(r"F:\大二下\小学期\2023SummerWork2")
    workbook = openpyxl.load_workbook("sni_info.xlsx")
    HTTPS = workbook['HTTPS']
    HTTP = workbook['HTTP']
    HTTPindex = HTTPSindex = 0
    for i in range(0, len(HTTPS_list)):
        for url in HTTPS_list[i]:
            HTTPSindex += 1
            sni_url = url[8:]
            tmp_list = sni_url.split('.')
            if(len(tmp_list) > 3):
                sni_url = f"{tmp_list[-3]}.{tmp_list[-2]}.{tmp_list[-1]}"
            data = [HTTPSindex, url, sni_url, "是", fileName_list[i]]
            HTTPS.append(data)
            print("over1")

    for i in range(0, len(HTTP_list)):
        for url in HTTP_list[i]:
            HTTPindex += 1
            data = [HTTPindex, url, "是", fileName_list[i]]
            HTTP.append(data)
            print("over2")

    workbook.save("sni_info.xlsx")

   
if __name__ == "__main__":
    main()