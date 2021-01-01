import time
def calculation(number):
    a = 0.9900990099009901
    cem = 0
    for i in range(number):
        a = a + a/100
        cem += a
    return a,cem
def cem_calculation(answer):
    cem = 0
    a = 0.9900990099009901
    number_days = 0
    while True:
        number_days += 1
        a = a + a/100
        cem += a
        if cem>=answer:
            break
        
    return a, cem, number_days   
def function(info):
    assert info in {"Yanvar", "Fevral", "Mart","Aprel","May","Iyun","Iyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"}
    return  info
while True:
    a = 0.9900990099009901
    cem = 0
    previous_time = 1609444800

    following_time = time.time()

    difference = following_time - previous_time

    number_days = 0



    print("1/2/3 reqemlerinden birini daxil etmekle davam edin;\n1 --> Calculation \n2 --> Review\n3 --> Total\n4 --> Date")
    secim = input("Seciminizi daxil edin: ")
    while True:
        if secim not in {"1","2","3", "4"}:
            secim = input("Seciminiz Yanlisdir! Zehmet olmasa, bir daha daxil edin: ")
                    
        if secim == "1":
            while True:
                number_days += 1
                a = a + a/100
                cem += a
                if (number_days - 1) * 86400 < difference <= (number_days) * 86400:
                    
                    if number_days <= 31:
                        print(f"{number_days} Yanvar")
                        break
                    elif number_days <= 59:
                        print(f"{number_days- 31} Fevral")
                        break
                    elif number_days <= 90:
                        print(f"{number_days - 59} Mart")
                        break
                    elif number_days <= 120:
                        print(f"{number_days - 90} Aprel")
                        break
                    elif number_days <= 151:
                        print(f"{number_days - 120} May")
                        break
                    elif number_days <= 181:
                        print(f"{number_days- 151} Iyun")
                        break
                    elif number_days <= 212:
                        print(f"{number_days - 181} Iyul")
                        break
                    elif number_days <= 243:
                        print(f"{number_days- 212} Avqust")
                        break
                    elif number_days <= 273:
                        print(f"{number_days - 243} Sentyabr")
                        break
                    elif number_days <= 304:
                        print(f"{number_days - 273} Oktyabr")
                        break
                    elif number_days <= 334:
                        print(f"{number_days - 304} Noyabr")
                        break
                    elif number_days <= 365:
                        print(f"{number_days - 334} Dekabr")
                        break
                    
                
            print(f"{number_days}.gun")
            print(f"a = {a}")
            print(f"Bugune qeder izlenmis videolarin total minutes: {cem}")
            #answer =  input("Davam etmek isteyirsiz? (Yes/No) ")
            #while answer not in {"Yes", "No"}:
                #answer = input("Zehmet olmasa, Yes/No dan istisna her hansi bir melumat daxil etmeyin! ")
                
            break

        if secim == "2":
            print("Burada sizin teyin etdiyiniz edede gore \"a\" ededinin qiymetini ve hemin qiymeti aldigi tarixi mueyyen ede bileceksiniz. \nDiqqet! Yalniz \"a\"  verilen ededden sonra gelen (ededin ozu de daxil olmaqla) birinci ededin qiymetini alacaq")
            while True:
                try:                 
                    first = float(input("Bir teyin edin: "))
                    print()
                    break
                except ValueError:
                    print("Xeta cixdi! Zehmet olmasa eded daxil etdiyinizden emin olun!")
                    print()
            while True:
                number_days += 1
                a = a + a/100
                cem += a         
                if first <= a:
                        if number_days <= 31:
                            print(f"{number_days} Yanvar")
                            break
                        elif number_days <= 59:
                            print(f"{number_days- 31} Fevral")
                            break
                        elif number_days <= 90:
                            print(f"{number_days - 59} Mart")
                            break
                        elif number_days <= 120:
                            print(f"{number_days - 90} Aprel")
                            break
                        elif number_days <= 151:
                            print(f"{number_days - 120} May")
                            break
                        elif number_days <= 181:
                            print(f"{number_days - 151} Iyun")
                            break
                        elif number_days <= 212:
                            print(f"{number_days - 181} Iyul")
                            break
                        elif number_days <= 243:
                            print(f"{number_days- 212} Avqust")
                            break
                        elif number_days <= 273:
                            print(f"{number_days - 243} Sentyabr")
                            break
                        elif number_days <= 304:
                            print(f"{number_days - 273} Oktyabr")
                            break
                        elif number_days <= 334:
                            print(f"{number_days - 304} Noyabr")
                            break
                        elif number_days <= 365:
                            print(f"{number_days - 334} Dekabr")
                            break
            print(f"a = {a}")
            print(f"Bugune qeder izlenmis videolarin total minutes: {cem}")
            print()
            break
            
        elif secim == "3":
            print("Ceme gore hesablama")
            while True:
                try:
                    answer = float(input("Nezerinizde tutdugunuz Total ededi daxil edin: "))
                    a, cem, number_days = cem_calculation(answer)
                    print(f"a ededi --> {a}\ncem --> {cem}")
                    if number_days <= 31:
                        print(f"{number_days} Yanvar")
                        break
                    elif number_days <= 59:
                        print(f"{number_days- 31} Fevral")
                        break
                    elif number_days <= 90:
                        print(f"{number_days - 59} Mart")
                        break
                    elif number_days <= 120:
                        print(f"{number_days - 90} Aprel")
                        break
                    elif number_days <= 151:
                        print(f"{number_days - 120} May")
                        break
                    elif number_days <= 181:
                        print(f"{number_days - 151} Iyun")
                        break
                    elif number_days <= 212:
                        print(f"{number_days - 181} Iyul")
                        break
                    elif number_days <= 243:
                        print(f"{number_days- 212} Avqust")
                        break
                    elif number_days <= 273:
                        print(f"{number_days - 243} Sentyabr")
                        break
                    elif number_days <= 304:
                        print(f"{number_days - 273} Oktyabr")
                        break
                    elif number_days <= 334:
                        print(f"{number_days - 304} Noyabr")
                        break
                    elif number_days <= 365:
                        print(f"{number_days - 334} Dekabr")
                        break
  
                except ValueError:
                    print("Xeta cixdi!")
                except Exception as e:
                    print(e)
            break
                                  
        elif secim == "4":
            print()
            print("Burada siz daxil etdiyiniz tarixlere gore \"a\" ededini ve hemin tarixe qeder olan \"cem\" tapa bileceksiniz, hemcinin verilmis tarixlere kimi totally gunler teqdim edilecek")
            print()
            
            try:
                while True:
                    number1, info = input("Tarixi daxil edin ").split()
                    number = int(number1)
                    function(info)
                    if info == "Yanvar":
                        if number <= 31:
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        
                        else:
                            print(f"{info} ayi 31 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                        break
                    elif info == "Fevral":
                        if number <= 28:
                            number += 31
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 28 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                            
                    elif info == "Mart":
                        if number <= 31:
                            number += 59
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 31 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "Aprel":
                        if number<= 30:
                            number += 90
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 30 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "May":
                        
                        if number <= 31:
                            number += 120
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 31 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "Iyun":
                        
                        if number <= 30:
                            number += 151
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 30 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "Iyul":
                        if number <= 31:
                            number += 181
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 31 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "Avqust":
                        if number <= 31:
                            number += 212
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 31 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "Sentyabr":
                        if number <= 30:
                            number += 243
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 30 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "Oktyabr":
                        if number<= 31:
                            number += 273
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 31 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    elif info == "Noyabr":
                        if number <= 30:
                            number += 304
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 30 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                        
                    elif info == "Dekabr":
                        if number <= 31:
                            number += 334
                            a,cem = calculation(number)
                            print(f"{number} gun kecib")
                            print(f"{number1} {info} tarixinde alinan qiymet {a}-e beraberdir")
                            print(f"Total: {cem}")
                            break
                        else:
                            print(f"{info} ayi 31 gunden ibaretdir!")
                            print("Zehmet olmasa, tarixi bir daha deqiqliyine diqqet yetirerek daxil edin ")
                            print()
                    print()
                    break
                            

            except AssertionError:
                print("Xeta cixdi!")
            except ValueError:
                print("Xeta cixdi!")
        break
                

