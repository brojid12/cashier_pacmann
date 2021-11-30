def diskon(total_harga, discount):
    if (total_harga > 100000):
        diskon = 0.1
    elif (total_harga > 50000):
        diskon = 0.05
    else:
        diskon = 0


    return diskon
