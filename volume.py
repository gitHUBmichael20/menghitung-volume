import math
print("Program Penghitung Volume")
print("1. Kubus")
print("2. Balok")
print("3. Bola")
print("4. Kerucut")
print("5. Limas Segitiga")
print("MASUKKAN DALAM SATU SATUAN!!!")
while True:
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    
    if pilihan in '1':
        print("VOLUME KUBUS")
        sisi_kubus = float(input("Masukkan sisi kubus : "))
        print("Volume Kubus = ", (sisi_kubus * sisi_kubus * sisi_kubus))
    
    elif pilihan in '2':
        print("VOLUME BALOK")
        panjang_balok = float(input("Panjang balok : "))
        tinggi_balok = float(input("Tinggi balok : "))
        lebar_balok = float(input("Lebar : "))
        print("Volume balok = ", (panjang_balok * tinggi_balok * lebar_balok))
    
    elif pilihan in '3':
        print("VOLUME BOLA")
        radius_bola = float(input("Masukkan jari jari bola : "))
        pi = float(3.14285714286)
        print("Volume bola = ", (4/3 * pi * (radius_bola**3) ))
    
    elif pilihan in '4':
        print("VOLUME KERUCUT")
        tinggi_krct = float(input("Tinggi Kerucut : "))
        jari_krct = float(input("Jari jari : "))
        pi = float(3.14285714286)
        print("Volume kerucut = ", (3/4 * (pi * jari_krct * jari_krct) * tinggi_krct))

    elif pilihan in '5':
        print("VOLUME LIMAS SEGITIGA") 
        
        #luas alas = 1/2 x panjang x lebar alas
        panjang_als = float(input("Panjang alas : "))
        lbr_alas = float(input("Lebar alas : "))
        luas_alas = float(1/2 * (panjang_als * lbr_alas))
        
        #Volume limas = ⅓ × luas alas × tinggi
        tinggi_lms = float(input("Tinggi limas : "))
        print("Volume limas segitigas = ", (1/3 * luas_alas * tinggi_lms))
    
    next_kalkulasi = input("Ulangi konversi ( Y / N ): ")
    if next_kalkulasi != 'Y':
        break
else:
    print("Invalid")