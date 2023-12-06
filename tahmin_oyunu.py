import random

def tahmin_oyunu():
    print("Merhaba! 1 ile 100 arasında bir sayı tahmin etmeye hazır mısın?")
    
    hedef_sayi = random.randint(1, 100)
    tahmin_sayisi = 0
    
    while True:
        tahmin = int(input("Tahmininizi girin: "))
        tahmin_sayisi += 1
        
        if tahmin < hedef_sayi:
            print("Daha yüksek bir sayı tahmin edin.")
        elif tahmin > hedef_sayi:
            print("Daha düşük bir sayı tahmin edin.")
        else:
            print(f"Tebrikler! {hedef_sayi} sayısını {tahmin_sayisi} tahminde buldunuz.")
            break

if __name__ == "__main__":
    tahmin_oyunu()
