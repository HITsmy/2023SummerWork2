import os
import shutil
def main():
    apks = os.listdir("/home/smy/Capreolus/test/")
    for apk in apks:
        print(apk[0:-4])
        print(f"./{apk}.txt")
        print(os.path.exists(f"/home/smy/Capreolus/output{apk}.txt") or os.path.exists(f"/home/smy/Capreolus/{apk}.txt"))
        # if(os.path.isdir(f"./tempfiles/{apk[0:-4]}")):
        #     shutil.rmtree(f"./tempfiles/{apk[0:-4]}")
        #     print("over")


def test():
        # while(True):
        # if(os.path.exisits(f"./output{apk}.txt") or os.path.exisits(f"./{apk}.txt")):
        #     print("delete!")
        #     shutil.rmtree(f"./tempfiles/{apk[0:-4]}")
        #     break
   
if __name__ == "__main__":
    main()