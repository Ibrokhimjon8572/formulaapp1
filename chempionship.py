from driver import Driver

class Chempionship:
    def __init__(self) -> None:
        self.driver_list: list[Driver] = []

    def create_driver(self, name):
        driver = Driver(name)
        self.driver_list.append(driver)
        print('driver yaratildi')
        return driver
    
    def get_drivers(self):
        return self.driver_list
    
    def get_driver(self, driver_name):
        for driver in self.driver_list:
            if driver.name == driver_name:
                return driver
        return None

