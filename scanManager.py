import nmap

class ScanManager:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.targets = None
        pass



    def save_result(self):
        print(self.nm.csv())
        result_cursor = open("", 'w')
        result_cursor.write(self.nm.csv())
        result_cursor.close()

    def working(self):
        print "ScanManager work"


    def start(self):
        self.working()