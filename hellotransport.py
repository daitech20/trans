import easypost
easypost.api_key = "EZAK510fe07cfeb04c8294849086d630f433tWaFTrrcCI9E0bKTctXfag"

data = {
    'from_street_1': '2',
    'from_street_2': '2',
    'from_city': '2',
    'from_state': '2',
    'from_zip': '2',
    'from_country': '2',
    'from_phone': '2'
}

# print(data['from_street_1'])

address = easypost.Address.create(
    verify=["delivery"],
    street1='417 montgomery streat',
    street2='FL 5',
    zip='94104',
    country='US',
    phone='11231231'
)

print(address.verifications)