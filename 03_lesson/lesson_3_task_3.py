from Address import Address
from Mailing import mailing

to_address = Address("101000", "Москва", "Тверская", "1", "2")
from_address = Address("102000", "Санкт-Петербург", "Невский", "2", "3")

mailing = mailing(to_address, from_address, 250.0, "TRK123456")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
      f"{mailing.from_address.street}, {mailing.from_address.home} - {mailing.from_address.flat} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
      f"{mailing.to_address.home} - {mailing.to_address.flat}. Стоимость {mailing.cost} рублей.")