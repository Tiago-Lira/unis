
def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        # A variável 'trocado' é usada para otimizar o algoritmo, parando o loop se nenhuma troca for realizada
        trocado = False

        # Comparar elementos adjacentes da lista e trocá-los se necessário
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocado = True

        # Se nenhuma troca foi realizada, a lista já está ordenada
        if not trocado:
            break

    return lista

def exemplo():
    # Exemplo de uso do Bubble Sort
    lista_exemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista_exemplo)

    lista_ordenada = bubble_sort(lista_exemplo)
    print("Lista ordenada:", lista_ordenada)

    
if __name__ == "__main__":
  exemplo()
