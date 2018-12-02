from scanManager import ScanManager

class Secretary:
    def __init__(self):
        self.scanManager = ScanManager()
        pass

    def working(self):
        self.scanManager.working()

    def start(self):
        self.working()

