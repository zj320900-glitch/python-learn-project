from pathlib import Path
import yaml
def load_config(env: str) -> dict:
    config_path = Path("D:/python3 project/python learn project") / env / "settings.yaml"
    if not config_path.exists():
        raise FileNotFoundError(f"{config_path} 不存在")
    return yaml.safe_load(config_path.read_text())
dev_config = load_config("进阶阶段")
print(dev_config)
prod_config = load_config("进阶阶段")
print(prod_config)

from pathlib import Path
def count_lines_by_extension(directory: Path, extension: str) -> int:
    total_lines = 0
    for file_path in directory.rglob(f"*.{extension}"):
        if file_path.is_file():
            try:
                lines = file_path.read_text().count("\n") + 1
                total_lines += lines
            except UnicodeDecodeError:
                print(f"跳过二进制文件：{file_path}")
    return total_lines
project_dir = Path("D:/python3 project/python learn project/进阶阶段")
py_lines = count_lines_by_extension(project_dir, "py")
print(f"Python 代码总行数：{py_lines}")
from pathlib import Path
import shutil
def organize_downloads_by_type():
    downloads = Path.home() / "Downloads"
    for file_path in downloads.iterdir():
        if file_path.is_file():
            target_dir = downloads / file_path.suffix[1:].lower()
            target_dir.mkdir(exist_ok=True)
            try:
                shutil.move(str(file_path), str(target_dir / file_path.name))
                print(f"已移动：{file_path.name} -> {target_dir.name}")
            except Exception as e:
                print(f"移动失败 {file_path.name}: {e}")
organize_downloads_by_type()      