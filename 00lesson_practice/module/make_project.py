"""
功能描述：自动化生成项目目录结构
需求描述：
    1. 在文件当前目录，自动生成项目，其包含目录bin、conf、core、db、log。
    2. 可指定默认项目名称，默认项目名称为"project_demo"。
    3. 当项目名称存在时，保持原项目，即对项目内容不进行任何改变。
"""
import os
import sys

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


def main():
    start_project()


if __name__ == "__main__":
    main()
