import time
from concurrent.futures import ThreadPoolExecutor

# -------------------------------
# Função para ler o arquivo
# -------------------------------
def ler_numeros(caminho):
    with open(caminho, 'r') as f:
        return [int(linha.strip()) for linha in f]


# -------------------------------
# Soma serial
# -------------------------------
def soma_serial(numeros):
    inicio = time.time()

    total = sum(numeros)

    fim = time.time()
    tempo = fim - inicio

    return total, tempo


# -------------------------------
# Soma parcial (para threads)
# -------------------------------
def soma_parcial(lista):
    return sum(lista)


# -------------------------------
# Soma paralela
# -------------------------------
def soma_paralela(numeros, num_threads):
    inicio = time.time()

    tamanho = len(numeros)
    bloco = tamanho // num_threads

    partes = []
    for i in range(num_threads):
        inicio_idx = i * bloco
        # último pega o resto
        if i == num_threads - 1:
            fim_idx = tamanho
        else:
            fim_idx = (i + 1) * bloco

        partes.append(numeros[inicio_idx:fim_idx])

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        resultados = executor.map(soma_parcial, partes)

    total = sum(resultados)

    fim = time.time()
    tempo = fim - inicio

    return total, tempo


# -------------------------------
# MAIN
# -------------------------------
if __name__ == "__main__":
    arquivo = "numero2.txt"

    print("Lendo arquivo...")
    numeros = ler_numeros(arquivo)

    print(f"Total de números: {len(numeros)}")

    # ---------------- SERIAL ----------------
    total_serial, tempo_serial = soma_serial(numeros)

    print("\n--- SERIAL ---")
    print(f"Soma: {total_serial}")
    print(f"Tempo: {tempo_serial:.4f} segundos")

    # ---------------- PARALELO ----------------
    threads_list = [2, 4, 8, 12]

    print("\n--- PARALELO ---")
    for t in threads_list:
        total_paralelo, tempo_paralelo = soma_paralela(numeros, t)

        print(f"\nThreads: {t}")
        print(f"Soma: {total_paralelo}")
        print(f"Tempo: {tempo_paralelo:.4f} segundos")
