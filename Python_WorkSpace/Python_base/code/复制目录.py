import os

first_dir = 'D:\\Git\\gitee\\open_source\\Python_WorkSpace\\Python_base\\file'
second_dir = 'D:\\Git\\gitee\\open_source\\Python_WorkSpace\\Python_base\\file2'


def copyfile():
    all_files = os.listdir(first_dir)
    for file in all_files:
        filename = os.path.join(first_dir, file)
        with open(filename, 'r', encoding='utf-8') as rstream:
            # print(filename)
            # print(rstream.readlines())
            wfilename = os.path.join(second_dir, file)
            print(wfilename)
            with open(wfilename, 'w', encoding='utf-8') as wstream:
                wstream.writelines(rstream.readlines())


copyfile()
