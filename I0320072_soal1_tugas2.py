def menu():
    print("Pilihlan mana yang akan anda hitung")
    print("-----------------------------------")
    print("1. Luas Persegi Panjang")
    print("2. Luas Lingkaran")
    print("3. Luas Kubus")
    print("4. Konversi suhu Celcius ke Fahrenheit")
    print("5. Konversi suhu Reamur ke Kelvin")

def persegipanjang():
    panjang = float(input("Masukkan Panjang: "))
    lebar = float(input("Masukkan Lebar: "))
    luas = panjang * lebar
    print("Luas Persegi Panjang: ", luas)

def lingkaran():
    jarijari = float(input("Masukkan Jari Jari Lingkaran"))
    Luas = 3.14 * (jarijari ** 2)
    print("Luas Lingkaran: ", Luas)

def kubus():
    sisi  = float(input("Masukkan sisi: "))
    Luas = 6 * (sisi ** 2)
    print("Luas Kubus: ", Luas)

def suhucelciuskefahrenheit():
    celcius = float(input("Masukkan suhu Celcius: "))
    fahrenheit = (celcius * 9/5) + 32
    print("Suhu Fahrenheit: ", fahrenheit)

def suhureamurkekelvin():
    reamur = float(input("Masukkan suhu Reamur: "))
    kelvin = (5/4 * reamur) + 273
    print("suhu kelvin: ", kelvin)

#ProgramUtama
print("Program Python Menghitung Luas Benda dan Konversi Suhu")
menu()
pilih = input("Masukkan pilihan: ")
print("------------------------------------------------------")

if pilih == ("1"):
    persegipanjang()
elif pilih == ("2"):
    lingkaran()
elif pilih == ("3"):
    kubus()
elif pilih == ("4"):
    suhucelciuskefahrenheit()
elif pilih == ("5"):
    suhureamurkekelvin()
else :
    print("salah input")