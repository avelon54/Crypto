def sezar_sifre_coz(ciphertext, anahtar):
    kucuk_alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    buyuk_alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    cozulmus_metin = ''
    
    for karakter in ciphertext:
        if karakter in kucuk_alfabe:
            pozisyon = kucuk_alfabe.find(karakter)
            yeni_pozisyon = (pozisyon - anahtar) % 29
            cozulmus_metin += kucuk_alfabe[yeni_pozisyon]
        elif karakter in buyuk_alfabe:
            pozisyon = buyuk_alfabe.find(karakter)
            yeni_pozisyon = (pozisyon - anahtar) % 29
            cozulmus_metin += buyuk_alfabe[yeni_pozisyon]
        else:
            cozulmus_metin += karakter
    
    return cozulmus_metin

def sezar_sifrele(metin, anahtar):
    kucuk_alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'
    buyuk_alfabe = 'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ'
    sifreli_metin = ''
    
    for karakter in metin:
        if karakter in kucuk_alfabe:
            pozisyon = kucuk_alfabe.find(karakter)
            yeni_pozisyon = (pozisyon + anahtar) % 29
            sifreli_metin += kucuk_alfabe[yeni_pozisyon]
        elif karakter in buyuk_alfabe:
            pozisyon = buyuk_alfabe.find(karakter)
            yeni_pozisyon = (pozisyon + anahtar) % 29
            sifreli_metin += buyuk_alfabe[yeni_pozisyon]
        else:
            sifreli_metin += karakter
    
    return sifreli_metin
sifreli_metin = 'CEZES NĞNS LIÜ ES LIÜ ÇIÜHI'
orijinal_metin = 'MERHABA'

anahtarlar = [5,3,4]
cozulmus_metin = sezar_sifre_coz(sifreli_metin, anahtarlar[0])
kriptolanmis_metin = sezar_sifre_coz(orijinal_metin, anahtarlar[1])

print('----1. Soru----')
print('Şifreli Metin: ', sifreli_metin)
print('Çözülmüş metin:', cozulmus_metin)
print('---------------')
print('----2. Soru----')
print('Orijinal Metin: ', orijinal_metin)
print('Kriptolanmış metin:', kriptolanmis_metin)
print('---------------')



