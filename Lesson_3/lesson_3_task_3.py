from address import Address
from mail import Mailing

to_address = Address(101003, "Moscow", "Gorky str.", "120", "23")
from_address = Address(125130, "Moscow", "Mitinskaya str.", "19", "3")
my_mail = Mailing(to_address, from_address, 150, "12544806")

print(f"Отправление {my_mail.track} из {my_mail.from_address.index}, {my_mail.from_address.city}, {my_mail.from_address.street}"
      f", {my_mail.from_address.house} - {my_mail.from_address.appartment} в {my_mail.to_address.index}, {my_mail.to_address.city}"
      f", {my_mail.to_address.street}, {my_mail.to_address.house} - {my_mail.to_address.appartment}. Стоимость {my_mail.cost} рублей.")
