import pickle
import json

'''
从网上查到python持久化数据的方式是通过pickle库来写入和读取二进制数据的方法
'''

# 定义一个数据字典
data = {
    'name': 'Alice',
    'age': 25,
    'gender': 'female'
}

# 从外部读取json文件来获取字典数据
# with open('data.json', 'r', encoding='utf-8') as f:
#     data = json.loads(f.read())

# 将数据持久化到文件中
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# 从文件中读取数据并加载到内存中
with open('data.pickle', 'rb') as f:
    data_bytes = f.read()
    memory_cache = memoryview(data_bytes)

# 从内存缓存中读取数据
data_bytes = memory_cache.tobytes()
data = pickle.loads(data_bytes)

# 查询从内存中读取到的数据
print(data)
