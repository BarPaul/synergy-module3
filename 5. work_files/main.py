class FileManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
    
    def read(self) -> str:
        try:
            with open(self.file_path, 'r') as file:
                file_text = file.read()
            return file_text
        except FileNotFoundError:
            return f"Файл {self.file_path} не найден!"


def main() -> str:
    fm = FileManager('sample.txt')
    readed_file = fm.read()
    print(readed_file)
    return readed_file


if __name__ == '__main__':
    main()
