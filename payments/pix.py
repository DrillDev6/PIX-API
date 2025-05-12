import uuid
import qrcode
class Pix:
    def __init__(self):
        pass


    def create_payment(self, base_dir=""):
        #Create payment from the financial institution
        bank_payment_id = str(uuid.uuid4())

        #copy & paste code
        hash_payment = f'hash_payment{bank_payment_id}'
        #qrcode
        img = qrcode.make(hash_payment)
        #create image as png
        img.save(f"{base_dir}static/img/qrcode_payment_{bank_payment_id}.png")

        return {"bank_payment_id": bank_payment_id,
                "qrcode_path": f"qrcode_payment_{bank_payment_id}"}

