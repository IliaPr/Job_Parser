import json

class Connector:
    """
    Класс коннектор к файлу, обязательно файл должен быть в json формате
    не забывать проверять целостность данных, что файл с данными не подвергся
    внешнего деградации
    """
    __data_file = None

    def __init__(self, file_path):
        self.data_file = file_path

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, value):
        self.__data_file = value
        self.__connect()

    def __connect(self):
        """
               Проверка на существование файла с данными и
               создание его при необходимости
               Также проверить на деградацию и возбудить исключение
               если файл потерял актуальность в структуре данных
        """
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(self.data_file, 'w') as f:
                json.dump([], f)
            data = []

        if not isinstance(data, list):
            raise TypeError("Файл должен содержать список")

    def insert(self, data):
        """
        Запись данных в файл с сохранением структуры и исходных данных
        """
        with open(self.data_file, 'r+') as f:
            file_data = json.load(f)
            file_data.append(data)
            f.seek(0)
            json.dump(file_data, f)

    def select(self, query):
        """
        Выбор данных из файла с применением фильтрации
        query содержит словарь, в котором ключ это поле для
        фильтрации, а значение это искомое значение
        """
        with open(self.data_file, 'r') as f:
            file_data = json.load(f)
            results = []
            for row in file_data:
                match = True
                for key, value in query.items():
                    if row.get(key) != value:
                        match = False
                        break
                if match:
                    results.append(row)
            return results

    def delete(self, query):
        """
        Удаление записей из файла, которые соответствуют запрос,
        как в методе select. Если в query передан пустой словарь, то
        функция удаления не сработает
        """
        if not query:
            raise ValueError("Query must not be empty")
        with open(self.data_file, 'r+') as f:
            file_data = json.load(f)
            f.seek(0)
            json.dump([row for row in file_data if not all(row.get(key) == value for key, value in query.items())], f)
            f.truncate()

if __name__ == '__main__':
    df = Connector('df.json')

    data_for_file = {'id': 1, 'title': 'tet'}

    df.insert(data_for_file)
    data_from_file = df.select(dict())
    assert data_from_file == [data_for_file]

    df.delete({'id':1})
    data_from_file = df.select(dict())
    assert data_from_file == []
