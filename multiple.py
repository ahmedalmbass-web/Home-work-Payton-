
class Device:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)


class Phone(Device):
    def __init__(self, brand, screen_size):
        Device.__init__(self, brand)
        self.screen_size = screen_size

    def make_call(self):
        print("Making a call")


class Camera(Device):
    def __init__(self, brand, resolution):
        Device.__init__(self, brand)
        self.resolution = resolution

    def take_photo(self):
        print("Taking a photo")


class SmartPhone(Phone, Camera):
    def __init__(self, brand, screen_size, resolution):
        Phone.__init__(self, brand, screen_size)
        Camera.__init__(self, brand, resolution)

    def show_smartphone_details(self):
        self.show_brand()
        print("Screen Size:", self.screen_size)
        print("Resolution:", self.resolution)


phone = SmartPhone("Samsung", 6.7, "108 MP")

phone.show_smartphone_details()
phone.make_call()
phone.take_photo()
