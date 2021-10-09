def dectobin(decimal):
    return str(bin(int(decimal)).replace("0b", "")  )

def bintodec(binary): 
    bn = str(binary)
    return str(int(bn, 2))