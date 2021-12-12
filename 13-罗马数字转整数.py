def romanToInt(s):
    i = s.count("I")
    v = s.count("V")
    x = s.count("X")
    l = s.count("L")
    c = s.count("C")
    d = s.count("D")
    m = s.count("M")
    iv = s.count("IV")
    ix = s.count("IX")
    xl = s.count("XL")
    xc = s.count("XC")
    cd = s.count("CD")
    cm = s.count("CM")
    a = i*1 + v*5 + x*10 + l*50 + c*100 + d*500 + m*1000
    if "IV" or "IX" in s:
        a_r = a - (iv+ix)*2
    if "XL" or "XC" in s:
        a_re = a_r - (xl+xc)*20
    if "CD" or "CM" in s:
        a_rs = a_re - (cd+cm)*200
    return a_rs

print(romanToInt("MCMXCIV"))



