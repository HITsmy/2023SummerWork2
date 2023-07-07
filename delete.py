import os


def main():
    pathList = os.listdir("./output/")
    for item in pathList:
        os.system(f"rm ./test/{item[0:-4]}")
        print("over")

if __name__ == "__main__":
    main()