#coding:utf-8
#人民币转换
import sys
d = {0: "零", 1: '壹', 2: '贰', 3: '叁', 4: '肆', 5: '伍', 6: '陆', 7: '柒', 8: '捌', 9: '玖'}
l = ["", "拾", "佰", "仟"]

#判断4位
def qian(s):
    n = len(s)
    num = int(s)
    ss = ''
    q = num//1000
    b = (num%1000)//100
    s = (num%100)//10
    g = num%10
    ll = [g, s, b, q]
    for i in range(n):
        if ll[n-i-1] == 0:
            if ll[n-i] == 0:
                pass
            else:
                ss += d[ll[n-i-1]]
        else:
            ss += d[ll[n-i-1]]
            ss += l[n-i-1]
    while ss[-1] == "零":
        ss = ss[:-1]
    if len(ss) > 1 and ss[0] == '壹' and ss[1] == '拾':
        ss = ss[1:]
    return ss


try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        a = s.split(".")[0]
        b = s.split(".")[1]
        #print(qian(a))
        st = '人民币'
        n = len(a)
        if n > 8:
            #打印亿
            y = a[:-8]
            st += qian(y)
            st += "亿"
            #打印万
            w = a[-8:-4]
            if w[0] == '0':
                st += '零'
            w = str(int(w))
            st += qian(w)
            st += "万"
            #打印元
            yu = a[-4:]
            if yu[0] == '0':
                st += '零'
            yu = str(int(yu))
            st += qian(yu)
            st += "元"
        elif n > 4:
            #打印万
            w = a[:-4]
            st += qian(w)
            st += "万"
            #打印元
            yu = a[-4:]
            if yu[0] == '0':
                st += '零'
            yu = str(int(yu))
            st += qian(yu)
            st += "元"
        else:
            if a == '0':
                pass
            else:
                #打印元
                st += qian(a)
                st += "元"
        #print(st)
        #打印元后面的
        if b[0] == '0' and b[1] == '0':
            st += '整'
        elif b[0] == '0' and b[1] != '0':
            st += '零'
            st += d[int(b[1])]
            st += '分'
        elif b[0] != '0' and b[1] == '0':
            st += d[int(b[0])]
            st += '角'
        else:
            st += d[int(b[0])]
            st += '角'
            st += d[int(b[1])]
            st += '分'
        print(st)


except:
    pass