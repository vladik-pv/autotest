from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "16", "+79444651102")
phone2 = Smartphone("Xiaomi", "Note 8", "+79004772311")
phone3 = Smartphone("Nokia", "3310", "+79647385631")
phone4 = Smartphone("Google", "Pixel 6", "+79123457892")
phone5 = Smartphone("Samsung", "Galaxy S21", "+79657483651")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} {phone.model} {phone.number}")