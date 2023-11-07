"""
Собирание файлов '.py' из каталогов в один файл с названием каталога
и названиями файлов внутри
"""
import os


def find_files(dir_files) -> list:
	"""Создать список файлов в каталоге"""
	list_files = []
	for root, dirs, files in os.walk(dir_files):
		for item in files:
			if item.endswith('py'):
				list_files.append(dir_files + '\\' + item)
	return list_files


def final_files(dir_base):
	""" Главный модуль"""
	all_folders = sorted(find_dirs(dir_base))
	for folder in all_folders:
		make_file(folder)


def make_file(dirs):
	"""Создать один файл из нескольких в каталоге"""
	new_list = find_files(dirs)
	new_dict = {}
	if len(new_list) > 0:
		new_file = os.path.basename(dirs)
		path_files = '\\'.join(dirs.split('\\')[:-1])
		for one_file in new_list:
			with open(one_file, 'r', encoding='utf-8') as fr:
				new_dict[one_file] = fr.readlines()
		write_file(path_files, new_file + '.py', new_dict)


def write_file(dirs, new_file, new_dict):
	"""Сохранить общий файл под именем папки"""
	name_new_file = '\\'.join([dirs, new_file])
	with open(name_new_file, 'w+', encoding='utf-8') as fw:
		for key, value in new_dict.items():
			fw.writelines("'''\n")
			fw.writelines(key.split('\\')[-1].upper())
			fw.writelines("\n'''\n\n")
			fw.writelines(value)
			fw.writelines('\n')
			print(key)


def find_dirs(main_path) -> set:
	"""Поиск папок, где есть файлы Python"""
	list_dirs = set()
	for (root, dirs, files) in os.walk(main_path, topdown=True):
		for f in files:
			block_dir = main_path + '\\' + 'venv'
			if block_dir not in root:
				if '.py' in f and not root == main_path:
					list_dirs.add(root)
	return list_dirs


if __name__ == '__main__':
	dir_names = input("Введите каталог или <Enter> для текущего:\n")
	if len(dir_names) > 1:
		files_path = dir_names
		print(files_path.encode('utf-8').decode('utf-8'))
	else:
		file = os.path.abspath('merge_py.py')
		files_path = os.path.dirname(file)
		print(files_path.encode('utf-8').decode('utf-8'))
	final_files(files_path)
