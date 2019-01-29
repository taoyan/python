import csv
import os


def process_csv(directory_path):

    all_content_path = os.path.join(directory_path, 'all_content.csv')
    if os.path.exists(all_content_path):
        print("已经存在，先删掉")
        os.remove(all_content_path)


    for path, dirs, files in os.walk(directory_path):
        csv_all_file = open(all_content_path, 'w', encoding="utf-8")
        writter = csv.writer(csv_all_file)
        if path == directory_path:
            for file in files:
                if os.path.splitext(file)[-1] == ".csv":
                    full_path = os.path.join(path, file)

                    csv_file = open(full_path, 'r', encoding="utf-8")
                    reader = csv.reader(csv_file)
                    writter.writerows(reader)
                    csv_file.close()

        csv_all_file.close()


directory_path = input('文件夹路径：')
process_csv(directory_path)

