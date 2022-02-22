def parser(node, dict):
    count = 0
    product = ""
    value = ""
    while (node[count] != ';'):
        product += node[count]
        count += 1
    for i in range(count + 1 ,len(node) - 1):
        value += node[i]
    dict[product] = float(value)
    return dict 
    
def get_dict_price():
    read_file = open("reader.ns", "r")
    dict = {}
    for lines in read_file.readlines():
        dict = parser(lines, dict)
    return dict

PRIX = get_dict_price()

def disponible(product ,PRIX):
    return product in PRIX

def prix_moyen(PRIX):
    if (len(PRIX) == 0):
        return
    moyenne = 0
    for i in PRIX.values():
        moyenne += i
    return (moyenne / len(PRIX.values()))


def fourchette_prix(mini, maxi, PRIX):
    tab = []
    for i in PRIX.items():
        if (i[1] >= mini and i[1] <= maxi):
            tab.append(i[0])
    return tab

panier_dict = {"Sabre laser": 3, "Coussin Linux": 2, "Slip Goldorak": 1}

def tous_disponible(panier_dict, prix):
    for node in panier_dict.keys():
        if node not in prix:
            return False
    return True

def recup_elements(node, prix):
    for i in prix.items():
        if i[0] == node[0]:
            return (i[1] * node[1])


def prix_achat(panier_dict, prix):
    if (tous_disponible(panier_dict, prix) == False):
        print ("il manque 1 ou plusieurs produit")
        return 0
    value = 0
    for node in panier_dict.items():
        value += recup_elements(node, prix)
    return value


print(prix_achat(panier_dict, PRIX))
fourchette_prix(50, 200, PRIX)
prix_moyen(PRIX)