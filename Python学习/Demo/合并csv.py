import csv
import os
from timeit import Timer


def process_csv(dictory_path):

    # all_content_path = os.path.join(dictory_path, 'all_content.csv')
    # if os.path.exists(all_content_path):
    #     # print("已经存在，先删掉")
    #     os.remove(all_content_path)


    for path, dirs, files in os.walk(dictory_path):
        # csv_all_file = open(all_content_path, 'w', encoding="utf-8")
        # writter = csv.writer(csv_all_file)
        if path == dictory_path:
            for file in files:
                if os.path.splitext(file)[-1] == ".csv":
                    full_path = os.path.join(path, file)

                    # csv_file = open(full_path, 'r', encoding="utf-8")
                    # reader = csv.reader(csv_file)
                    # writter.writerows(reader)
                    # csv_file.close()

        # csv_all_file.close()



def process_csv2(dictory_path):

    # all_content_path = os.path.join(dictory_path, 'all_content.csv')
    # if os.path.exists(all_content_path):
    #     # print("已经存在，先删掉")
    #     os.remove(all_content_path)

    for path, dirs, files in os.walk(dictory_path):
        if path != dictory_path:
            continue
        else:
            files = (os.path.join(path, file) for file in files if os.path.splitext(file)[-1] == '.csv')

        # files = [os.path.join(path, file) for file in files if os.path.splitext(file)[-1] == '.csv']

        # if path != dictory_path:
        #     continue

        # csv_all_file = open(all_content_path, 'w', encoding="utf-8")
        # writter = csv.writer(csv_all_file)
        #
        for file in files:
            pass
        #     csv_file = open(file, 'r', encoding="utf-8")
        #     reader = csv.reader(csv_file)
        #     writter.writerows(reader)
        #     csv_file.close()
        #
        # csv_all_file.close()


# directory_path = input('文件夹路径：')
# # process_csv(directory_path)
# process_csv2(directory_path)

T1 = Timer("process_csv2(dictory_path='/Users/yantao/Desktop/python/Python学习/Demo/CSVs')", "from __main__ import process_csv2")
print("process_csv2", T1.timeit(100000))

T2 = Timer("process_csv(dictory_path='/Users/yantao/Desktop/python/Python学习/Demo/CSVs')", "from __main__ import process_csv")
print("process_csv", T2.timeit(100000))