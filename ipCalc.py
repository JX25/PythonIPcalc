import socket

# from http://commandline.org.uk/python/how-to-find-out-ip-address-in-python/
def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('INSERT SOME TARGET WEBSITE.com', 0))
    return s.getsockname()[0]

ip = getNetowrkIp()