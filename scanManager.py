import nmap

class ScanManager:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.target_classes = None
        self.target_number = None
        self.scan_class_number = 0
        pass

    def read_target_classes(self):
        try:
            read_cursor = open("hosts.info", 'r')
            self.target_classes = read_cursor.readlines()
            self.target_number = len(self.target_classes)

            for i in range(0, self.target_number):
                self.target_classes[i] = self.target_classes[i].rstrip('\n')
                print str(i) + ". " + self.target_classes[i]

            read_cursor.close()
        except:
            print "Error! Read HOSTS"

    def scanning(self):
        for self.scan_class_number in range(0, self.target_number):
            self.nm.scan(hosts=self.target_classes[self.scan_class_number], arguments='-v -sV -PB -sS -T2')
            self.save_result()

    def save_result(self):
        print self.nm.command_line()
        print self.nm.all_hosts()
        print(self.nm.csv())
        result_cursor = open(str(self.scan_class_number) + "_" + "result.csv", 'w')
        result_cursor.write(self.nm.csv())
        result_cursor.close()

        hosts_cursor = open(str(self.scan_class_number) + "_" + "hosts.csv", 'a')
        for host in self.nm.all_hosts():
            hosts_cursor.write(host)

        hosts_cursor.close()

    def working(self):
        print "Working ScanManager"
        self.read_target_classes()
        self.scanning()
        print "Done ScanManager"

    def start(self):
        self.working()