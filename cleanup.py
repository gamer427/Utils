skip_name = ['app', 'dmg', 'epub', 'xip', 'pkg'] # расширене файлов



from pathlib import Path
import sys


remove_all_auto = False
if len(sys.argv) > 1 and sys.argv[1] == '--all':
	remove_all_auto = True


def filter_name(file):
	return file.name.split('.')[-1] not in skip_name


base_dir = Path('.')
queue = [base_dir]
idx = 0
while len(queue) > 0:
	dir = queue.pop(-1)
	for file in dir.iterdir():
		if file.name.startswith("._"):
			endl = " | pass:" if not remove_all_auto else "\n"
			print(idx, file.relative_to(base_dir), sep='\t', end=endl)
			if not remove_all_auto and input() != "":
				continue
			idx += 1
			file.unlink(missing_ok=True)
		elif not file.is_file() and filter_name(file):
			queue.append(file)


print(f"Removed {idx} files")