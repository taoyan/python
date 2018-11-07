
import pymongo

# 链接mongod服务
mongo_py = pymongo.MongoClient()

# 数据库
# db = mongo_py['six']

# 表，集合
# collection = mongo_py['six']['stu']
collection = mongo_py.six.stu

# 插入数据
one = {"name":"章三","age":50}

two_many = [
    {"name":"章3","age":100},
    {"name":"李四","age":40},
    {"name":"王五","age":30},
    {"name":"大花","age":20}
]

try:
    # collection.insert_one(one)
    # collection.insert_many(two_many)

    # 删了第一个
    # collection.delete_one({"age":50})
    collection.delete_many({"age":50})

#     修改
#     collection.update({"age":20},{"$set":{"name":"小王 "}})
    collection.update_many({"age": 20}, {"$set": {"name": "小王 "}})

#     查询
    result = collection.find({"age":100})
    for i in result:
        print(result)

    result = collection.find_one({"age": 100})
    print(result)

except Exception as e:
    print(e)

finally:
    # 关闭数据库
    mongo_py.close()