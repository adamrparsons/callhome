
class Filesystem():

    def __init__(self):
        self.mountpoint = ''
        self.size = 0  # in bytes
        self.used = 0  # in bytes

    def _get_filesystems(self):
        '''
        I think this is a factory method, best way I can explain it
        '''
        import psutil
        disk_info = psutil.disk_partitions()
        filesystems = []
        for x in disk_info:
            filesystem = Filesystem()
            filesystem.mountpoint = x.mountpoint
            filesystem.size = psutil.disk_usage(x.mountpoint).total
            filesystem.used = psutil.disk_usage(x.mountpoint).used
            filesystems.append(filesystem.__dict__)
        return filesystems




class ServerReport():
    '''
    Initial scope should contain:
        * Hostname
        * Uptime
        * Filesystems []
            * Size
            * Available
    '''

    def __init__(self):
        self.name = ''
        self.hostname = ''
        self.uptime = 0
        self.filesystems = []


    def fill_data(self):
        # Hostname Info
        import socket
        self.hostname = socket.gethostname()
        
        # Uptime
        import psutil, time
        self.uptime = int(time.time() - psutil.boot_time())

        # Filesystems array
        self.filesystems = Filesystem()._get_filesystems()


    def to_dict(self):
        '''
        Can be replaced with the methods built-in __dict__() method, but this gives more granular control
        '''
        return {
            'hostname': self.hostname,
            'uptime': self.uptime,
            'filesystems': self.filesystems,
        }

