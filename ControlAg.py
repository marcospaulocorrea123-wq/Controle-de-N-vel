from colorama import Fore, Style, init
import time

# Inicializa colorama
init(autoreset=True)

# ================= BASE DE ALARMES =================

alarmes = [
    {"codigo": "A1", "mensagem": "Muito baixo (crítico)", "nivel": "CRITICO"},
    {"codigo": "A2", "mensagem": "Nível de água muito baixo", "nivel": "BAIXO"},
    {"codigo": "A3", "mensagem": "Pressão fora do padrão", "nivel": "MEDIO"},
    {"codigo": "A4", "mensagem": "Sistema operando normalmente", "nivel": "ALTO"},
    {"codigo": "A5", "mensagem": "Nível de água muito alto", "nivel": "ALERTA"}
]

# ================= CORES =================

def definir_cor(nivel):
    if nivel == "CRITICO":
        return Fore.RED + Style.BRIGHT
    elif nivel == "BAIXO":
        return Fore.YELLOW + Style.BRIGHT
    elif nivel == "MEDIO":
        return Fore.GREEN
    elif nivel == "ALERTA":
        return Fore.CYAN + Style.BRIGHT
    elif nivel == "NORMAL":
        return Fore.BLUE
    else:
        return Fore.WHITE

# ================= EXIBIÇÃO =================

def exibir_alarme(alarme):
    cor = definir_cor(alarme["nivel"])
    
    print(cor + "==============================")
    print(cor + f" CÓDIGO : {alarme['codigo']}")
    print(cor + f" NÍVEL  : {alarme['nivel']}")
    print(cor + f" STATUS : {alarme['mensagem']}")
    print(cor + "==============================\n")

# ================= SIMULAÇÃO =================

def simular_alarmes():
    print("🚨 SISTEMA DE ALARMES ATIVO 🚨\n")
    
    for alarme in alarmes:
        exibir_alarme(alarme)
        time.sleep(1)

    print(Style.RESET_ALL)

# ================= EXECUÇÃO =================

if __name__ == "__main__":
    simular_alarmes()

