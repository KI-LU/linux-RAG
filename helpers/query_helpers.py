
### hier sind helpers für die Fragen an den RAG-Bot
### und für die Erstellung eines Benchmark-Datensatzes 
### für das Eintragen von Inhalten in den Benchmark-Datensatz

### Eingeben einer Frage an den RAG-Bot
def set_query(task: str):
    TASK = 'WRITE'
    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}
    query = str(input("Gebe hier deine Frage ein: ")).translate(special_chars)
    return query


### Erstellen eines Benchmark-Datensatzes
### der Datensatz wird in einer JSON-Datei gespeichert
import json
bench_df = [] 
def fill_bench_df(question: str, ground_truth: str, GPT_answer: str, GPT_score: str , RAG_answer: str, RAG_relevance: str, RAG_use: str, RAG_completeness: str, filename: str = 'benchmark.json'):
    try:
        with open(filename, 'r') as file:
            bench_df = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        bench_df = []
       
    id = len(bench_df) + 1
    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}
    question = str(input("Gebe hier deine Frage ein: ")).translate(special_chars)
    ground_truth = str(input("Gebe hier die richtige Antwort ein: ")).translate(special_chars)
    GPT_answer = ""
    GPT_score  = ""
    RAG_answer = "" 
    RAG_relevance = ""
    RAG_use = ""
    RAG_completeness = "" 

    

    entry = {"id": id}, {"Frage": question}, {"richtige Antwort": ground_truth}, {"GPT Antwort": GPT_answer}, {"Bewertung GPT":GPT_score}, {"RAG-Bot Antwort": RAG_answer}, {"Textnutzung":RAG_use}, {"Relevanz":RAG_relevance}, {"Vollständigkeit":RAG_completeness}
    bench_df.append(entry)

    with open(filename, 'w') as file:
        json.dump(bench_df, file)
    return bench_df    


### Funktion zum Eintragen der Antworten von PHI in den Benchmark-Datensatz
def insert_GPT_answer(filename: str = 'benchmark.json'):
    filename = 'benchmark.json'

    with open(filename, 'r') as file:
        bench_df = json.load(file)

    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}

    id_input = input("Gebe hier die ID der Frage ein: ")
    found = False

    for entry in bench_df: 
        print(f"this is entry: {entry}")
        for d in entry:  
            print(f"this is d: {d}")
            if d.get("id") == int(id_input):

                for d2 in entry:
                    if "GPT Antwort" in d2:
                        neue_antwort = str(input("Gebe hier die Antwort von ChatGPT ein: ")).translate(special_chars)
                        d2["GPT Antwort"] = neue_antwort
                        print(f"Die Antwort von ChatGPT für Frage Nummer {id_input} wurde aktualisiert.")
                        found = True
                        break
                    
            if found:
                break
        if found:
            break
    if not found:
        print(f"Keine Frage mit der ID {id_input} gefunden.")

    with open(filename, 'w') as file:
        json.dump(bench_df, file)
    return bench_df        


### Funktion zum Eintragen der Antworten von RAG-BOT in den Benchmark-Datensatz
def insert_rag_answer(filename: str = 'benchmark.json'):
    filename = 'benchmark.json'

    with open(filename, 'r') as file:
        bench_df = json.load(file)

    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}

    id_input = input("Gebe hier die ID der Frage ein: ")
    found = False

    for entry in bench_df: 
        
        for d in entry:    
            if d.get("id") == int(id_input):
                for d2 in entry:
                    if "RAG-Bot Antwort" in d2:
                        neue_antwort = str(input("Gebe hier die Antwort von RAG-Bot ein: ")).translate(special_chars)
                        d2["RAG-Bot Antwort"] = neue_antwort
                        print(f"Die Antwort von RAG-Bot für Frage Nummer {id_input} wurde aktualisiert.")
                        found = True
                        break
            if found:
                break
        if found:
            break
    if not found:
        print(f"Keine Frage mit der ID {id_input} gefunden.")                
                        
    with open(filename, 'w') as file:
        json.dump(bench_df, file)
    return bench_df   

### Funktion zum Eintragen der Bewertung von RAG-BOTS TEXTNUTZUNG in den Benchmark-Datensatz
def insert_rag_use(filename: str = 'benchmark.json'):
    filename = 'benchmark.json'
    with open(filename, 'r') as file:
        bench_df = json.load(file)

    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}

    id_input = input("Gebe hier die ID der Frage ein: ")
    found = False

    for entry in bench_df: 
        
        for d in entry:    
            if d.get("id") == int(id_input):
                for d2 in entry:
                    if "Textnutzung" in d2:
                        neue_antwort = str(input("Wurden die Texte aus der Wissensbasis für Erzeugung die Antwort genutzt? Gebe hier deine Bewertung ein: ")).translate(special_chars)
                        d2["Textnutzung"] = neue_antwort
                        print(f"Die Bewertung der Textnutzung für Frage Nummer {id_input} wurde aktualisiert.")
                        found = True
                        break
            if found:
                break
        if found:
            break
    if not found:
        print(f"Keine Frage mit der ID {id_input} gefunden.")                
                        
    with open(filename, 'w') as file:
        json.dump(bench_df, file)
    return bench_df 

### Funktion zum Eintragen der Bewertung von PHIS ANTWORT in den Benchmark-Datensatz
def insert_GPT_score(filename: str = 'benchmark.json'):
    filename = 'benchmark.json'
    with open(filename, 'r') as file:
        bench_df = json.load(file)

    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}

    id_input = input("Gebe hier die ID der Frage ein: ")
    found = False

    for entry in bench_df: 
        
        for d in entry:    
            if d.get("id") == int(id_input):
                for d2 in entry:
                    if "Bewertung GPT" in d2:
                        neue_antwort = str(input("Gebe hier deine Bewertung für ChatGPT's Performance ein: ")).translate(special_chars)
                        d2["Bewertung GPT"] = neue_antwort
                        print(f"Die Bewertung für Frage Nummer {id_input} wurde aktualisiert.")
                        found = True
                        break
            if found:
                break
        if found:
            break
    if not found:
        print(f"Keine Frage mit der ID {id_input} gefunden.")                
       
    with open(filename, 'w') as file:
        json.dump(bench_df, file)
    return bench_df 

### Funktion zum Eintragen der Bewertung von RAG-BOTS RELEVANZ in den Benchmark-Datensatz
def insert_rag_relevance(filename: str = 'benchmark.json'):
    filename = 'benchmark.json'
    with open(filename, 'r') as file:
        bench_df = json.load(file)

    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}

    id_input = input("Gebe hier die ID der Frage ein: ")
    found = False

    for entry in bench_df: 
        
        for d in entry:    
            if d.get("id") == int(id_input):
                for d2 in entry:
                    if "Relevanz" in d2:
                        neue_antwort = str(input("Wie relevant sind die Text-Chunks welche gefunden wurden? Gebe hier deine Bewertung ein: ")).translate(special_chars)
                        d2["Relevanz"] = neue_antwort
                        print(f"Die Bewertung für Frage Nummer {id_input} wurde aktualisiert.")
                        found = True
                        break
            if found:
                break
        if found:
            break
    if not found:
        print(f"Keine Frage mit der ID {id_input} gefunden.")                
                       
   
    with open(filename, 'w') as file:
        json.dump(bench_df, file)
    return bench_df 



### Funktion zum Eintragen der Bewertung von RAG-BOTS VOLLSTÄNDIGKEIT in den Benchmark-Datensatz
def insert_rag_completeness(filename: str = 'benchmark.json'):
    filename = 'benchmark.json'
    with open(filename, 'r') as file:
        bench_df = json.load(file)

    special_chars = {ord('ä'):'ae', ord('ü'):'ue', ord('ö'):'oe', ord('ß'):'ss'}

    id_input = input("Gebe hier die ID der Frage ein: ")
    found = False

    for entry in bench_df: 
        
        for d in entry:    
            if d.get("id") == int(id_input):
                for d2 in entry:
                    if "Vollständigkeit" in d2:
                        neue_antwort = str(input("Sind alle relevanten Aspekte in der Antwort von RAG-Bot enthalten? Gebe hier deine Bewertung ein: ")).translate(special_chars)
                        d2["Vollständigkeit"] = neue_antwort
                        print(f"Die Bewertung für Frage Nummer {id_input} wurde aktualisiert.")
                        found = True
                        break
            if found:
                break
        if found:
            break
    if not found:
        print(f"Keine Frage mit der ID {id_input} gefunden.")                
                       
    with open(filename, 'w') as file:
        json.dump(bench_df, file)
    return bench_df 