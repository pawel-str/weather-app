from datetime import datetime

def save_log(response_code: str):
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open('log.txt','a',encoding='utf-8') as file:
        if response_code == 200:
            file.write(f"{current_time} - Pobrano dane pogodowe\n")
        else:
            file.write(f"{current_time} - Wystąpił błąd\n") 
    
    
def read_log():
    try:
        with open('log.txt','r', encoding="utf-8") as file:
            content = file.read()
            print(content)
            
    except FileNotFoundError:
        print("Plik log.txt nie istnieje!")
    
