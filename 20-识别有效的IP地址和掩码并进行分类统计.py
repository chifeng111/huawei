#-*- coding:utf-8 -*-
#识别有效的IP地址和掩码并进行分类统计

import sys
li = ["254", "252", "248", "240", "224", "192", "128", "0"]
def mask_is_legal(mask):
    l = mask.split(".")
    if len(l) != 4:
        return False
    if l[0] == '255':
        if l[1] == '255':
            if l[2] == '255':
                if l[3] in li:
                    return True
                else:
                    return False
            elif l[2] in li and l[3] == '0':
                return True
            else:
                return False
        elif l[1] in li and l[2] == l[3] == '0':
            return True
        else:
            return False
    elif l[0] in li and l[1] == l[2] == l[3] == '0':
        return True
    else:
        return False

try:
    a = b = c = d = e = 0
    f = g = 0
    while 1:
        s = sys.stdin.readline().strip()
        if s == "":
            break
        ip = s.split("~")[0]
        mask = s.split("~")[1]
        if mask_is_legal(mask) and len(ip.split(".")) == 4 and ip.split(".")[0] != '' and ip.split(".")[1] != '' \
                and ip.split(".")[2] != '' and ip.split(".")[3] != '':
            if 1 <= int(ip.split(".")[0]) <= 126:
                a += 1
            if 128 <= int(ip.split(".")[0]) <= 191:
                b += 1
            if 192 <= int(ip.split(".")[0]) <= 223:
                c += 1
            if 224 <= int(ip.split(".")[0]) <= 239:
                d += 1
            if 240 <= int(ip.split(".")[0]) <= 255:
                e += 1
            if ip.split(".")[0] == '10' or \
                ip.split(".")[0] == '172' and 16 <= int(ip.split(".")[1]) <= 31 or \
                ip.split(".")[0] == '192' and ip.split(".")[1] == '168':
                g += 1
        else:
            f += 1
    print(a,b,c,d,e,f,g)
    #print(mask_is_legal('255.0.0.0'))

except:
    pass