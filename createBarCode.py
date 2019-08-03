import barcode
ean = barcode.get('ean13', '123456789102')
# Now we look if the checksum was added
ean.get_fullcode()

filename = ean.save('ean13')


options = dict(compress=True)
filename = ean.save('ean13', options)
