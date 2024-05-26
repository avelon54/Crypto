#Route Şifre Algoritması
def route_sifre_coz(sifreli_metin, sutun_sayisi):
    satir_sayisi = len(sifreli_metin) // sutun_sayisi
    if len(sifreli_metin) % sutun_sayisi != 0:
        raise ValueError("Metin uzunluğu sütun sayısına tam bölünmüyor.")       
    ızgara = [['' for _ in range(sutun_sayisi)] for _ in range(satir_sayisi)]
    satir_index= 0
    sutun_index= sutun_sayisi -1
    increase_satir = -1
    increase_sutun = 1
    sifreli_index = 0
    direction = 0
    satir_direction=1
    sutun_direction = 1
    kalan_sutun_index = sutun_sayisi -1
    kalan_satir_index = satir_sayisi -1
    baslangıc_satir_index = 0
    baslangıc_sutun_index= 0
    rotate = True
    while sifreli_index < satir_sayisi*sutun_sayisi:
        ızgara[satir_index][sutun_index] = sifreli_metin[sifreli_index]
        sifreli_index  += 1
        if rotate:
            if satir_direction == 0 and satir_index == baslangıc_satir_index and satir_index != kalan_satir_index:
                
                satir_direction = 1
                baslangıc_satir_index += 1
                direction = 1
                increase_sutun *= -1
                
            elif sutun_direction == 0 and sutun_index == baslangıc_sutun_index and sutun_index != kalan_sutun_index:
                
                sutun_direction = 1
                baslangıc_sutun_index += 1
                direction = 0
                increase_satir *= -1    
                
            elif satir_direction == 1 and satir_index == kalan_satir_index and satir_index != baslangıc_satir_index:
                
                satir_direction = 0
                increase_sutun *= -1
                kalan_satir_index -= 1
                direction = 1
                
            elif sutun_direction == 1 and sutun_index == kalan_sutun_index and sutun_index != baslangıc_sutun_index:
                
                sutun_direction = 0
                direction = 0
                increase_satir *= -1
                kalan_sutun_index -= 1   
            if kalan_satir_index == baslangıc_satir_index == satir_index:
                direction = 1
                increase_sutun *= -1
                rotate = False
            if kalan_sutun_index == baslangıc_sutun_index == sutun_index:
                direction= 0
                increase_satir *= -1
                rotate = False 
        
        if direction == 0:
            satir_index += increase_satir
        if direction == 1:
            sutun_index += increase_sutun
        
    cozulmus_metin = ''
    for satir in range(satir_sayisi):
        for sutun in range(sutun_sayisi):
            cozulmus_metin += ızgara[satir][sutun]
    
    return cozulmus_metin

route_sifreli_metin = 'AİRERXXEDRANNVATÇEHEYNHİ'
print(len(route_sifreli_metin))