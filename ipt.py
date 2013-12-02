def trans(ipSlashMask):
    ip2bin = lambda ip: ''.join([bin(int(i))[2:].rjust(8,'0') for i in ip.split('.')])
    bin2ip = lambda b: '.'.join([str(int(m,2)) for m in [b[:8],b[8:16],b[16:24],b[24:32]]])
    ip, mask = ipSlashMask.split('/')
    mask = int(mask)
    ipbMasked = ip2bin(ip)[:mask]
    return bin2ip(ipbMasked+'0'*(31-mask)+'1') + '-' + bin2ip(ipbMasked+'1'*(32-mask))
