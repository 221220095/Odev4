import sqlite3

def kaan_benzerlik(text1, text2):
    def sesli_harf_orani(text):
        sesli_harfler = "aeıioöuü"
        text = text.lower()
        sesli_harf_sayisi = sum(1 for char in text if char in sesli_harfler)
        toplam_karakter_sayisi = len(text)
        return sesli_harf_sayisi / toplam_karakter_sayisi if toplam_karakter_sayisi > 0 else 0.0
    
    oran1 = sesli_harf_orani(text1)
    oran2 = sesli_harf_orani(text2)
    
    print(oran1)
    print(oran2)
    
    benzerlik_skoru = abs(oran1 / oran2)  # Sesli harf oranlarını kullanarak benzerlik hesapladım.
    
    return benzerlik_skoru

text1 = input("Lütfen ilk metni girin: ")
text2 = input("Lütfen ikinci metni girin: ")

# Gerçek veritabanı oluşturmadım DB Browser kurmam gerekti, sadece kod içinde tanımladım.
connection = sqlite3.connect(':memory:')  #  Onun yerine bellekte geçici bir veritabanı oluşturdum.
# connection = sqlite3.connect('metinler.db') Ortam kuracak olsaydım bu satırı kullanırdım.
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS metinler (id INTEGER PRIMARY KEY, metin TEXT)''')
cursor.execute('''INSERT INTO metinler (metin) VALUES (?)''', (text1,))
cursor.execute('''INSERT INTO metinler (metin) VALUES (?)''', (text2,))

connection.commit()

similarity_score = kaan_benzerlik(text1, text2)

print("Metinler arasındaki benzerlik katsayısı:", similarity_score)

with open('benzerlik_durumu.txt', 'w') as file:
    file.write(f"Metinler arasındaki benzerlik katsayısı: {similarity_score}")
