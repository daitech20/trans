def get_shipment(data):
    import easypost
    easypost.api_key = "EZAK510fe07cfeb04c8294849086d630f433tWaFTrrcCI9E0bKTctXfag"

    # this address will not be verified
    from_address = easypost.Address.create(
        verify=["delivery"],
        street1=data['from_street_1'],
        street2=data['from_street_2'],
        zip=data['from_zip'],
        country=data['from_country'],
        phone=data['from_phone']
    )

    to_address = easypost.Address.create(
        verify=["delivery"],
        street1=data['to_street_1'],
        street2=data['to_street_2'],
        zip=data['to_zip'],
        country=data['to_country'],
        phone=data['to_phone']
    )

    parcel = easypost.Parcel.create(
        length=data['length'],
        width=data['width'],
        height=data['height'],
        weight=data['weight']
    )

    shipment = easypost.Shipment.create(
        to_address=to_address,
        from_address=from_address,
        parcel=parcel
    )

    return shipment




