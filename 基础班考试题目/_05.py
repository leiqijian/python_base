# 1、手动在当前项目根目录下创建singer.txt文件，内容如下： 沉默是金，张国荣 少女的祈祷，杨千嬅 暗里着迷，刘德华 难念的经，周华健（内容见附件）
#
# 2、定义一个singer类(歌手类)，包含初始化init方法： 成员属性: 歌曲名 歌手名字 成员方法：fans()：打印“XXX歌手的YYY歌曲持续打榜，粉丝为喜欢的歌手打call” XXX为对象的歌手名字，YYY为对象的歌曲名。
#
# 3、在歌手类外面完成以下功能：
#
# 1）通过程序逐行读取singer.txt文件内容，根据每行数据创建对应歌手对象并赋值，依次将歌手对象存入列表。
#
# 2）遍历列表，获取元素并调用对象的fans方法

class Singer():
    def __init__(self, song, singer_name):
        self.song = song
        self.singer_name = singer_name

    def fans(self):
        print(f"{self.singer_name}歌手的{self.song}歌曲持续打榜，粉丝为喜欢的歌手打call")


def load_data():
    singer_list = []
    with open('singer.txt', "r", encoding='utf-8') as f:
        data = f.read()
        list = data.split("\n")
        for e in list:
            e = e.split("，")
            singer = Singer(e[0], e[1])
            singer_list.append(singer)
    return singer_list

if __name__ == '__main__':
    singer_list = load_data()
    for singer in singer_list:
        singer.fans()