import pymongo
from pymongo import MongoClient
from gridfs import GridFS


class GFS(object):
    def __init__(self, file_db, file_table):
        self.file_db = file_db
        self.file_table = file_table

    def createDB(self):  # 连接数据库，并创建文件数据库与数据表
        client = MongoClient('localhost', 27017)
        db = client[self.file_db]
        file_table = db[self.file_table]
        return (db, file_table)

    def insertFile(self, db, filePath, query):  # 将文件存入数据表
        fs = GridFS(db, self.file_table)
        if fs.exists(query):
            print('已经存在该文件')
        else:
            with open(filePath, 'rb') as fileObj:
                data = fileObj.read()
                ObjectId = fs.put(data, filename=filePath.split('/')[-1])
                print(ObjectId)
                fileObj.close()
            return ObjectId

    def getID(self, db, query):  # 通过文件属性获取文件ID，ID为文件删除、文件读取做准备
        fs = GridFS(db, self.file_table)
        ObjectId = fs.find_one(query)._id
        return ObjectId

    def getFile(self, db, id):  # 获取文件属性，并读出二进制数据至内存
        fs = GridFS(db, self.file_table)
        gf = fs.get(id)
        bdata = gf.read()  # 二进制数据
        attri = {}  # 文件属性信息
        attri['chunk_size'] = gf.chunk_size
        attri['length'] = gf.length
        attri["upload_date"] = gf.upload_date
        attri["filename"] = gf.filename
        attri['md5'] = gf.md5
        print(attri)
        return (bdata, attri)

    # def listFile(self,db): #列出所有文件名
    #     fs = GridFS(db, self.file_table)
    #     gf = fs.list()

    # def findFile(self,db,file_table): #列出所有文件二进制数据
    #     fs = GridFS(db, table)
    #     for file in fs.find():
    #         bdata=file.read()

    def write_2_disk(self, bdata, attri):  # 将二进制数据存入磁盘
        name = "get_" + attri['filename']
        if name:
            output = open(name, 'wb')
        output.write(bdata)
        output.close()
        print("fetch image ok!")

    def remove(self, db, id):  # 文件数据库中数据的删除
        fs = GridFS(db, self.file_table)
        fs.delete(id)  # 只能是id


if __name__ == '__main__':
    gfs = GFS('fileDB', 'fileTable')
    (file_db, fileTable) = gfs.createDB()  # 创建数据库与数据表
    filePath = 'G:/file/pix/IMG_0061.JPG'  # 插入的文件
    query = {'filename': 'IMG_0061.JPG'}
    id = gfs.insertFile(file_db, filePath, query)  # 插入文件
    id = gfs.getID(file_db, query)
    (bdata, attri) = gfs.getFile(file_db, id)  # 查询并获取文件信息至内存
    gfs.write_2_disk(bdata, attri)  # 写入磁盘
    # gfs.remove(file_db,id) #删除数据库中文件
