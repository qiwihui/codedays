"""
编译项目
环境安装：
  - Linux： python-devel, gcc
    apt-get install python3-dev gcc
  - Python: cython
    pip install Cython
使用：
    usage: compile.py [-h] [--rebuild] [parent_path]
    positional arguments:
      parent_path  编译目录
    optional arguments:
      -h, --help   show this help message and exit
      --rebuild    重新编译目录
生成结果：
    目录 build 下
注意：
    1. 当源文件中使用 __file__ 变量时会出错，__file__ 是运行时环境确定，故 __init__.py 也需要保留
"""
import argparse
import os
import py_compile
import shutil
import time
from distutils.core import setup
from Cython.Build import cythonize


def get_py(base_path="", relative_path="", entry="", exclude_files=list(), exclude_folders=list()):
    """
    获取 python文件的列表
    :param base_path: 源文件目录
    :param relative_path: 相对与base_path的路径
    :param entry: 文件夹
    :param exclude_files:
    :param exclude_folders:
    :return: 对应三种形式文件的路径列表
    """
    so_files = []
    pyc_files = []
    py_files = []
    entry_full_path = os.path.join(base_path, relative_path, entry)
    for file_name in os.listdir(entry_full_path):
        file_path = os.path.join(entry_full_path, file_name)
        # 文件夹
        if os.path.isdir(file_path):
            # 不处理的文件夹
            if file_name in exclude_folders:
                pass

            elif file_name in ["migrations"]:
                # migrations文件
                # Django 只能加载 .py 文件作为 migrations 文件
                # -> https://code.djangoproject.com/ticket/23406
                for migrations_file_name in os.listdir(file_path):
                    ext = os.path.splitext(migrations_file_name)[1]
                    if ext == ".py":
                        migrations_file_path = os.path.join(
                            relative_path, entry, "migrations", migrations_file_name)
                        # print(migrations_file_path)
                        py_files.append(migrations_file_path)
                        # py_compile.compile(migrations_file_path)
            else:
                sub_so_files, sub_pyc_files, sub_py_files = get_py(
                    base_path=base_path,
                    relative_path=os.path.join(relative_path, entry),
                    entry=file_name,
                    exclude_files=exclude_files,
                    exclude_folders=exclude_folders)
                if sub_so_files:
                    so_files += sub_so_files
                if sub_pyc_files:
                    pyc_files += sub_pyc_files
                if sub_py_files:
                    py_files += sub_py_files
        elif os.path.isfile(file_path):
            ext = os.path.splitext(file_name)[1]
            file_relative_name = os.path.join(relative_path, entry, file_name)
            if ext in ('.c', '.pyc'):
                pass
            elif file_name in exclude_files:
                # 排除的文件(相同文件名的)
                if file_name in ["manage.py"]:
                    py_files.append(file_relative_name)
                elif file_name not in ["local_settings.py", __file__]:
                    pyc_files.append(file_relative_name)
            elif ext in ('.py',):
                if file_name.startswith("__"):
                    # __init__.py 文件
                    pyc_files.append(file_relative_name)
                else:
                    so_files.append(file_relative_name)

    return so_files, pyc_files, py_files


def copy_soc_static_file(base_path, dst_dir):
    """
    处理项目需要的静态文件
    :return:
    """
    # 不需要编译的文件夹和静态文件列表，会原样复制
    targets = [
        # 基础数据
        "cad_server/local_settings_prod.py",
        "kb/kb.json",
        "cad_server/sites.json",
        "subscriber/templates",
        "utils/static",
        "cad_server_celery.conf",
        "cad_server_celerybeat.conf",
        "cad_server_gunicorn.conf",
        "Dockerfile",
        "mysql_operations.patch",
        "requirements.txt",
        "setup.sh",
    ]

    for target in targets:
        # print(target)
        target_path = os.path.join(base_path, target)
        # dst_path = os.path.join(base_path, dst_dir, target)
        # FIXME
        dst_path = os.path.join(dst_dir, target)
        # print(dst_path)
        if os.path.isdir(target_path):
            # 静态文件
            if os.path.exists(dst_path):
                shutil.rmtree(dst_path)
            shutil.copytree(target, dst_path)
        elif os.path.isfile(target_path):
            target_dst_path = os.path.dirname(dst_path)
            if not os.path.exists(target_dst_path):
                # print("make")
                os.makedirs(target_dst_path)
            shutil.copy(target_path, dst_path)
        else:
            print("Error: 未知文件或路径: " + target)

    print("Done!")


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


def print_list(a_list):
    for a in a_list:
        print(a)


def compile_and_copy():
    """
    编译并复制到目的地
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rebuild", action="store_true",
                        help='rebuild whole project')
    parser.add_argument("-d", "--dst_dir", default='build',
                        help='build dst dir')
    parser.add_argument("-t", "--temp_dir", default='temp',
                        help='temp dir')
    parser.add_argument("parent_path", nargs='?',
                        help='compile folder', default="")
    args = parser.parse_args()

    # 开始时间
    start_time = time.time()

    # 源文件目录
    source_dir = os.path.abspath(".")
    parent_path = args.parent_path

    # 编译后的文件目录
    dst_dir = args.dst_dir
    temp_dir = args.temp_dir

    # 排除编译成 .so 的文件和目录
    exclude_files = [
        "manage.py",
        "local_settings.py",
        "local_settings.py",
        "local_settings_prod.py",
        "tasks.py",
        "utils.py",
        __file__,
    ]
    exclude_folders = [
        dst_dir,
        "tests",
        "docs",
        "coverage_report"
    ]

    rebuild = args.rebuild
    if rebuild:
        # 删除上次的编译
        print("重新编译...")
        # 删除临时文件
        if os.path.exists(temp_dir):
            print("删除之前的temp目录")
            shutil.rmtree(temp_dir)
            os.makedirs(temp_dir)

        if os.path.exists(dst_dir):
            print("删除之前的编译目录")
            shutil.rmtree(dst_dir)
            os.makedirs(dst_dir)
    else:
        print("使用之前的temp和编译目录")
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

    # 获取需要编译的文件
    so_files, pyc_files, py_files = get_py(
        base_path=source_dir,
        relative_path=parent_path,
        entry="",
        exclude_files=exclude_files,
        exclude_folders=exclude_folders)

    # print_list(pyc_files)
    # print_list(so_files)
    # print_list(py_files)
    # print(len(pyc_files))
    # print(len(so_files))
    # print(len(py_files))
    # 编译并生成文件
    try:
        print("复制静态文件")
        copy_soc_static_file(source_dir, dst_dir)
        # so
        print("Compiling .so files")
        build_dst_dir = dst_dir
        if parent_path:
            build_dst_dir += "/" + parent_path
        setup(ext_modules=cythonize(so_files, build_dir=temp_dir),
              script_args=["build_ext", "-b", build_dst_dir, "-t", temp_dir])
        # pyc
        print("Compiling .pyc files")
        for pyc in pyc_files:
            pyc_source = os.path.join(source_dir, pyc)
            # pyc_dst = os.path.join(source_dir, dst_dir + "/" + pyc + 'c')
            # FIXME
            pyc_dst = os.path.join(dst_dir, pyc + 'c')
            # print("source: " + pyc)
            # print("dst: " + pyc_dst)
            pyc_dst_path = os.path.dirname(pyc_dst)
            if not os.path.exists(pyc_dst_path):
                os.makedirs(pyc_dst_path)
            py_compile.compile(pyc_source, cfile=pyc_dst)

        # py 保持原样
        print("Copying .py files")
        for py in py_files:
            py_source = os.path.join(source_dir, py)
            # FIXME
            # py_dst = os.path.join(source_dir, dst_dir + "/" + py)
            py_dst = os.path.join(dst_dir, py)
            # print(py_dst)
            # print("source: " + pyc)
            # print("dst: " + pyc_dst)
            py_dst_path = os.path.dirname(py_dst)
            if not os.path.exists(py_dst_path):
                os.makedirs(py_dst_path)
            shutil.copyfile(py_source, py_dst)

    except Exception as e:
        print(e)
    else:
        pass

    print("completed! Total time: " + str(time.time() - start_time) + ' s')


if __name__ == "__main__":
    compile_and_copy()
