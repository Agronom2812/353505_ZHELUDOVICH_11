import zipfile
import json
from pathlib import Path


class FileOperations:
    @staticmethod
    def save_results(data, output_path):
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @staticmethod
    def zip_file(file_path, zip_path):
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(file_path, arcname=Path(file_path).name)

        with zipfile.ZipFile(zip_path, 'r') as zipf:
            info = zipf.getinfo(Path(file_path).name)
            return {
                "filename": info.filename,
                "file_size": info.file_size,
                "compress_size": info.compress_size,
                "date_time": info.date_time
            }

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as f:
            return f.read()
