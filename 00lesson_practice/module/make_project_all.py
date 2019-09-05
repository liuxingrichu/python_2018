"""
功能描述：自动化生成项目结构
需求描述：
    1. 在文件当前目录，自动生成项目，其包含包bin、conf、core、db、log和readme.md文件。
    2. 可指定默认项目名称，默认项目名称为"project_demo"。
    3. 当项目名称存在时，保持原项目，即对项目内容不进行任何改变。
    4. readme.md文件中，逐行书写项目创建人姓名、创建时间及项目说明。
"""
import os
import sys
import time

path = os.path.dirname(__file__)


def start_project():
    """
        功能：生成目录
    """
    project_name = 'project_demo'
    if len(sys.argv) > 1:
        project_name = sys.argv[1]

    dirs = ['bin', 'conf', 'core', 'db', 'log']
    for dir in dirs:
        dir_path = os.path.join(path, project_name, dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(os.path.join(dir_path, '__init__.py'), 'w'):
            pass
    with open(os.path.join(path, project_name, 'readme.md'), 'w') as f:
        f.write("项目创建人：Tom")
        f.write('\n')
        f.write("项目创建时间：%s" % time.ctime())
        f.write('\n')
        f.write("项目说明: 自动化生成项目结构")


def main():
    start_project()


if __name__ == "__main__":
    main()
