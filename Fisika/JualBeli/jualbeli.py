def Diskon (diskon):
    def potonganHarga(harga):
        return harga*((100-diskon)/100)
    return potonganHarga