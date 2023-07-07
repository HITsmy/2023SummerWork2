import os
def main():
    dir_list = os.listdir("./output/")
    print(dir_list)
    print(len(dir_list))
if __name__ == "__main__":
    main()
