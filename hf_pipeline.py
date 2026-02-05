from transformers import pipeline 

print("Model is loading...")

duygu_analizi = pipeline("sentiment-analysis")

while True: 
    metin = input("Duygu analizi yapmak istediğiniz metni giriniz: ")

    if metin.lower() == "exit":
        break
 
    sonuc = duygu_analizi(metin)
    print(sonuc)