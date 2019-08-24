#Author : Roche Christopher
#File created on 24 Aug 2019 10:16 AM

from pdf2image import convert_from_path
from pyzbar import pyzbar

class QRCodeDownloader:

    def __init__(self, file_path):
        self.file_path = file_path

    def get_qr_codes_url(self):

        #convert pdf to images
        pages = convert_from_path(self.file_path, 100,  first_page=11)

        #print(len(pages))
        #exit()
        i =1
        qr_codes_data = []
        for page in pages:


            barcodes = pyzbar.decode(page)
            if len(barcodes) > 0:
                print(i)
            for barcode in barcodes:

                barcodeData = barcode.data.decode('utf-8')
                print(barcodeData)
                qr_codes_data.append(barcodeData)
            i = i + 1
        print(len(qr_codes_data))


filepath = 'B321,322_STD_4_TAMIL,ENGLISH_LANG_TERM 1.pdf'
qr_cd_Obj = QRCodeDownloader(filepath)
qr_cd_Obj.get_qr_codes_url()

