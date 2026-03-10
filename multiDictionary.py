import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.listDizionari:dict={}

    def printDic(self, language):
        if language in self.listDizionari:
            self.listDizionari[language].printAll()
        else:
            print("Il dizionario non è stato ancora caricato")

    def aggiungiDizionario(self,path,language):
        dTemp= d.Dictionary()
        dTemp.loadDictionary(path)
        self.listDizionari[language]=dTemp

    def searchWord(self, words, language):

        ##individuo il dizionario corretto
        if language in self.listDizionari:
            dTemp=self.listDizionari[language]
        else:
            self.aggiungiDizionario("resources/"+language+".txt",language)
            dTemp=self.listDizionari[language]


        ##separo i termini in ingresso
        listaInput=words

        listadiRitorno=[]
        for i in listaInput:
            if i in dTemp.listTerm:
              rwTemp=rw.RichWord(i)
              rwTemp.corretta=True
              listadiRitorno.append(rwTemp)
            else:
                rwTemp = rw.RichWord(i)
                rwTemp.corretta = False
                listadiRitorno.append(rwTemp)

        return listadiRitorno


if __name__ == "__main__":
    md = MultiDictionary()

    # Prepariamo una piccola lista di parole di prova
    parole_test = ["ciao", "mondo", "pappagallo_inesistente"]
    lingua = "Italian"  # Assicurati che coincida col nome del file Italian.txt

    print(f"--- Inizio Test MultiDictionary per {lingua} ---")

    # Eseguiamo la ricerca: questo deve innescare il caricamento del file
    risultati = md.searchWord(parole_test, lingua)

    # Verifichiamo cosa è successo
    print(f"Oggetti RichWord ricevuti: {len(risultati)}")

    for rw in risultati:
        # Stampiamo la parola e il suo stato booleano
        esito = "CORRETTA" if rw.corretta else "ERRATA"
        print(f"Parola: {rw} -> Esito: {esito}")

    # Verifichiamo se il dizionario è ora nella cache
    if lingua in md.listDizionari:
        print(f"✅ Successo: Il dizionario {lingua} è stato salvato nella cache.")
    else:
        print(f"❌ Fallimento: Il dizionario non è stato memorizzato.")