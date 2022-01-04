#    3.	 Write a function named shekvetis_gaketeba which takes a string named shekveta as a parameter. The string can contain only the following words:
#    xachapuri, xinkali, mcvadi, kababi, salata (with space separated from each other).
#    The function returns a string that counts the number of each product and displays it in the form shown in the examples (see below). If the order does not contain any product,
#    in this case the quantity of the product will be zero. for example:
#    • If the order is "xachapuri xinkali xachapuri kababi salata mcvadi salata" the function returns "xachapuri: 2 xinkali: 1 mcvadi: 1 kababi: 1 salata: 2"
#    • If the order is = "xachapuri xinkali xachapuri salata mcvadi salata" "function returns" xachapuri: 2 xinkali: 1 mcvadi: 1 kababi: 0 salata: 2 "

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
