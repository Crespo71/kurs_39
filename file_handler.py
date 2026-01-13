import json


class FileHandler:
    def read_dane(self):
        with open("dane.json") as file:
            reader = json.load(file)

            print(reader)
            return reader
    def write_dane(self, historia, saldo, magazyn):
        with open("dane.json", "w") as file:
            file.write(json.dumps({"historia": historia, "saldo": saldo, "magazyn": magazyn}))




filehandler = FileHandler()
