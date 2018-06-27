
class Image():
    def __init__(self):
        self.date_created = None
        self.original_name = None
        self.lat = None
        self.lon = None
        self.address = None
        self.new_name = None
    
    def get_date_created(self):
        return self.date_created

    def get_original_name(self):
        return self.original_name

    def get_lat(self):
        return self.lat
    
    def get_lon(self):
        return self.lon
    
    def get_address(self):
        return self.address

    def get_new_name(self):
        return self.new_name

    def set_date_created(self, date):
        self.date_created = date

    def set_original_name(self, original_name):
        self.original_name = original_name

    def set_lat(self, lat):
        self.lat = lat
    
    def set_lon(self, lon):
        self.lon = lon
    
    def set_address(self, address):
        self.address = address

    def set_new_name(self, new_name):
        self.new_name = new_name
