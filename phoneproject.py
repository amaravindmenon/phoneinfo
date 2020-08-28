class Camera:
    def cam(self):
        print("Camera Available")
    def frontcamera(self,x):
        switcher = {
            8: "It has 8MP front camera",
            16: "It has 16MP front camera",
            32: "It has 32MP front camera",
            64: "It has 64MP front camera",
        }
        print (switcher.get(x))

    def backcamera(self,x):
        switcher = {
            8: "It has 8MP back camera",
            16: "It has 16MP back camera",
            32: "It has 32MP back camera",
            64: "It has 64MP back camera",
        }
        print (switcher.get(x))

class Bluetooth:
    def blue(self):
        print("Bluetooth Available")
        
class fingerprint:
    def indisplay(self):
        print("it has Indisplay fingerprint")
    def backfinger(self):
        print("it has back fingerprint")

class Samsung(Camera,fingerprint,Bluetooth):
    def saph(self):
        print("Samsung Feature")
        print("_________________")
    def get_value(self):    
        Camera.cam(self)
        Camera.frontcamera(self,8)
        Camera.backcamera(self,32)
        fingerprint.indisplay(self)
class MI(Camera,fingerprint,Bluetooth):
    def miph(self):
        print("MI Feature")
        print("____________")
    def get_value(self):
        Camera.cam(self)
        Camera.frontcamera(self,16)
        Camera.backcamera(self,16)
        fingerprint.backfinger(self)
class OPPO(Camera,fingerprint,Bluetooth):
    def opph(self):
        print("OPPO Feature")
        print("____________")
    def get_value(self):
        Camera.cam(self)
        Camera.frontcamera(self,32)
        Camera.backcamera(self,64)
        fingerprint.backfinger(self)

class phone(Samsung,MI,OPPO):
    
     def __init__(self):

        print("A PROJECT BY ARAVIND MENON")

    def get_phone(self,a):
        if (a == 1):
            Samsung.saph(self)
            Samsung.get_value(self)
        elif (a == 2):
            MI.miph(self)
            MI.get_value(self)
        else:
            OPPO.opph(self)
            OPPO.get_value(self)

ph = phone()
print("SELECT YOUR PHONE")
print("1 for Samsung")
print("2 for MI")
print("3 for OPPO")
x = int(input("Enter number: "))
ph.get_phone(x)





'''
sam = samsung()
sam.get_value()
print(" ")
mi = MI()
mi.get_value()'''
