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
    street1='a 2',
    street2='a 1 2',
    city='1',
    state='1',
    zip='1',
    country='1',
    phone='1'
)
