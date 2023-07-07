import os
import shutil
from concurrent.futures import ThreadPoolExecutor
def execute(apk):
    os.system(f"./capreolus -sni -f test/{apk} -noida -o output/{apk}.txt")
    while(True):
        if(os.path.exists(f"./output/output{apk}.txt") or os.path.exists(f"./output/{apk}.txt")):
            print("delete!")
            shutil.rmtree(f"./tempfiles/{apk[0:-4]}")
            break
    

def main():
    apks = os.listdir("./test")
    with ThreadPoolExecutor(5) as t:
        for apk in apks:	
            t.submit(execute, apk)

        

if __name__ == '__main__':
    main()
