import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        self.multi_dict = md.MultiDictionary()
        self.dictResult:dict={}


    def gestisciRisultato(self,t_inizio,t_fine,listaParoleErrate:list,nParoleErrate:int):
            self.dictResult["tTotale:"]=t_fine-t_inizio
            self.dictResult["n_errori:"]=nParoleErrate
            self.dictResult["ListaParoleErrate"]=listaParoleErrate

            res = self.dictResult
            print("______________________________\n")
            print("tempo richiesto: " + str(res["tTotale:"]) + "\n")
            print("numero di parole errate: " + str(res["n_errori:"]) + "\n")
            print("parole errate:\n")
            print(res["ListaParoleErrate"])
            print("______________________________\n")

    def handleSentence(self, txtIn, language):
        t_inizio= time.perf_counter()
        countErrate=0
        listaErrate=[]
        lTemp=replaceChars(txtIn).lower().split()
        listaRisultato=self.multi_dict.searchWord(lTemp,language)
        for i in listaRisultato:
            if i.corretta==False:
                countErrate=countErrate+1
                listaErrate.append(str(i))

        t_fine=time.perf_counter()
        return self.gestisciRisultato(t_inizio,t_fine,listaErrate,countErrate)

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text


if __name__ == "__main__":
    # 1. Istanziamo il Controller
    sc = SpellChecker()

    # 2. Definiamo un caso di test reale
    # 'melaa' e 'mondoo' sono errori certi
    test_frase = "Ciao, come va? La melaa è sul tavoloo."
    test_lingua = "Italian"

    print(f"--- COLLAUDO SPELLCHECKER ---")
    print(f"Testo in ingresso: {test_frase}")

    # 3. Eseguiamo la logica
    # Nota: handleSentence popola self.dictResult tramite gestisciRisultato
    sc.handleSentence(test_frase, test_lingua)

    # 4. Verifichiamo il contenuto del dizionario dei risultati
    res = sc.dictResult
    print(f"Tempo totale registrato: {res['tTotale:']} secondi")
    print(f"Numero errori trovati: {res['n_errori:']}")
    print(f"Elenco parole errate: {res['ListaParoleErrate']}")

    # 5. Controllo di qualità
    if res['n_errori:'] > 0:
        print("✅ Il sistema identifica correttamente gli errori.")
    else:
        print("❌ Errore: Il sistema non ha trovato errori in una frase palesemente sbagliata.")