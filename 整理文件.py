# 小奀
# 时间：2023/2/11 21:23
# 导入模块
import os
import shutil
from tkinter import filedialog
import datetime

# 确定文件格式
photo = ['jpg', 'png', 'bmp', 'jpeg', 'gif', 'JPG', 'JPEG', 'webp']
video = ['mp4', 'wmv', 'flv', 'mov', 'MP4', 'MOV']
rar = ['rar', 'zip', '7z', 'jar', 'gz']
pdf = ['pdf', 'PDF']
word = ['txt', 'doc', 'docx', ]
excel = ['csv', 'xls', 'xlsx', 'CSV', 'XLS']
ppt = ['ppt', 'pptx', 'PPT']
music = ['mp3', 'flac', 'MP3', 'FLAC']
num = 0

# 文件路径初始化
print('选择你想分类的文件夹')
dir_path = filedialog.askdirectory()

# 目标路径初始化
move_photo = '图片'
move_video = '视频'
move_PDF = 'PDF文件'
move_word = 'word&txt文件'
move_excel = 'excel文件'
move_PPT = 'PPT文件'
move_rar = '压缩包'
move_other = '其他文件'
move_music = '音乐'
frame = ['图片', '视频', 'PDF文件', 'word&txt文件', 'excel文件', 'PPT文件', '压缩包', '其他文件', '音乐']


# 开始分类
def sort_file():
    # 初始化目标路径
    target = ''
    global num
    print('分类开始！')
    print()
    for file in os.listdir(dir_path):
        # 获取文件后缀作为分类依据
        ext = os.path.splitext(file)[1][1:]
        if file in frame:
            continue
        else:
            print(file, end='\t')
            if not os.path.isdir(file):
                if ext in excel:
                    # 确定目标文件夹
                    target = move_excel
                    # 如果不存在目标文件夹则创建
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                elif ext in photo:
                    target = move_photo
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                elif ext in rar:
                    target = move_rar
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                elif ext in video:
                    target = move_video
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                elif ext in word:
                    target = move_word
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                elif ext in ppt:
                    target = move_PPT
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                elif ext in pdf:
                    target = move_PDF
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                elif ext in music:
                    target = move_music
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
                else:
                    target = move_other
                    if not os.path.exists(f'{dir_path}/{target}'):
                        os.mkdir(f'{dir_path}/{target}')
            # 移动文件至目标位置
            shutil.move(f'{dir_path}/{file}', f'{dir_path}/{target}/{file}')
            print(f'已分类成功！,分类至\t{target}')
            num += 1


def time_compute():
    global num
    delta_time = end_time - start_time
    delta_m = int(str(delta_time)[2:4])
    delta_s = int(str(delta_time)[5:7])
    delta_ms = str(delta_time)[8:11]
    if delta_m == 0:
        print(f'\n已全部分类完成！，共耗时 {delta_s}s {delta_ms}ms')
    elif delta_m != 0:
        print(f'\n已全部分类完成！，共耗时 {delta_m}m {delta_s}s {delta_ms}ms')
    print(f"共分类文件:{num}个")


if __name__ == "__main__":
    # 开始计时
    start_time = datetime.datetime.now()
    # 调用分类函数
    sort_file()
    # 结束计时
    end_time = datetime.datetime.now()
    # 计算时间
    time_compute()
