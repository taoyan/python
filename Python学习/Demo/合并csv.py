import csv

import os


def process_csv(dictory_path):

    all_content_path = os.path.join(directory_path, 'all_content.csv')
    if os.path.exists(all_content_path):
        print("已经存在，先删掉")
        os.remove(all_content_path)


    for path, dirs, files in os.walk(dictory_path):
        csv_all_file = open(all_content_path, 'w', encoding="utf-8")
        writter = csv.writer(csv_all_file)
        if path == dictory_path:
            for file in files:
                if os.path.splitext(file)[-1] == ".csv":
                    full_path = os.path.join(path, file)
                    print(full_path)
                    csv_file = open(full_path, 'r', encoding="utf-8")
                    reader = csv.reader(csv_file)
                    writter.writerows(reader)
                    # for row in reader:
                    #     writter.writerow(row)
                    csv_file.close()
                    print('aaaaa')

        csv_all_file.close()


 for path, dirs, files in os.walk(dictory_path):
        files = [os.path.join(path, file) for file in files if os.path.splitext(file)[-1] == '.csv']

        if path != dictory_path:
            continue

        csv_all_file = open(all_content_path, 'w', encoding="utf-8")
        writter = csv.writer(csv_all_file)

        for file in files:
            csv_file = open(file, 'r', encoding="utf-8")
            reader = csv.reader(csv_file)
            # writter.writerows(reader)
            for row in reader:
                writter.writerow(row)
            csv_file.close()
            print('aaaaa')

        csv_all_file.close()


directory_path = input('文件夹路径：')
process_csv(directory_path)

