from pathlib import Path

file_ex = Path("/tmp") / "test_file.txt"
print(f'File:    {file_ex}')
print(f'Stem:    {file_ex.stem}')
print(f'Suffix:  {file_ex.suffix}')
print(f'Exists:  {file_ex.exists()}')
print(f'Resolve: {file_ex.resolve()}')
print(f'String:  {str(file_ex)}')
print(f'File?:   {file_ex.is_file()}')
print(f'Dir?:    {file_ex.is_dir()}')
