ord = input("Enter the order: ")


def shekvetis_gaketeba(ord):
    order = ord.split(" ")
    xachapuri = 0
    xinkali = 0
    mcvadi = 0
    kababi = 0
    salata = 0

    for i in range(0, len(order)):

        if order[i] != "xachapuri" and order[i] != "xinkali" and order[i] != "mcvadi" and order[i] != "kababi" and order[i] != "salata":
            return 0

        else:
            if order[i] == "xachapuri":
                xachapuri += 1

            if order[i] == "xinkali":
                xinkali += 1

            if order[i] == "mcvadi":
                mcvadi += 1

            if order[i] == "kababi":
                kababi += 1

            if order[i] == "salata":
                salata += 1

    print(
        "xachapuri: " + str(xachapuri) + "; xinkali: " + str(xinkali) + "; mcvadi: " + str(mcvadi) + "; kababi: " + str(
            kababi) + "; salata: " + str(salata))


shekvetis_gaketeba(ord)
