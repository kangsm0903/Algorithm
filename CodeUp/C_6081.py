a = input()

a = int(a,16)

for i in range(1,16):
    mix = a * i
    if i >= 10:
        print("{}*{}={}".format(format(a,'X'),format(i,'X'),format(mix,'X')))
    else:
        print("{}*{}={}".format(format(a,'X'),i,format(mix,'X')))
