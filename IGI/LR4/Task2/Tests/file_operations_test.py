import pytest
import os
import tempfile
from Lab4.Task2.file_operations import FileOperations


class TestFileOperations:
    @pytest.fixture
    def sample_data(self):
        return {"test": [1, 2, 3]}

    def test_zip_creation(self, sample_data):
        with tempfile.NamedTemporaryFile(suffix='.json') as json_tmp:
            FileOperations.save_results(sample_data, json_tmp.name)

            with tempfile.NamedTemporaryFile(suffix='.zip') as zip_tmp:
                info = FileOperations.zip_file(json_tmp.name, zip_tmp.name)
                assert info['file_size'] > 0
                assert os.path.exists(zip_tmp.name)
