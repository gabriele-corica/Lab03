class Dictionary:
    def __init__(self):
        self.listTerm:list = []

    def loadDictionary(self,path):
        try:
            with open(path,'r',encoding='utf-8') as file:
                righe=file.read()
                ##aggiungo tutti i termini
                self.listTerm=righe.split()


        except FileNotFoundError: print("File not found")


    def printAll(self):
        return self.listTerm



if __name__ == "__main__":
    d = Dictionary()
    # Scrivi il percorso esatto che serve per trovare il file nel tuo PC
    d.loadDictionary("resources/Italian.txt")
    print(f"Parole caricate: {len(d.listTerm)}")