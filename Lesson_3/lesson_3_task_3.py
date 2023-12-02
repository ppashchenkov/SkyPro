from address import Address
from mail import Mailing

to_address = Address(101003, "Moscow", "Gorky str.", "120", "23")
from_address = Address(125130, "Moscow", "Mitinskaya str.", "19", "3")
my_mail = Mailing(to_address, from_address, 150, "12544806")

print("Отправление ",my_mail.track," из ",from_address.index,", ",from_address.city,", ",from_address.street,", "
    ,from_address.house," - ",from_address.appartment," в ",to_address.index,", ",to_address.city,", ",to_address.street
    ,", ",to_address.house," - ",to_address.appartment,". Стоимость ",my_mail.cost," рублей.",sep="")