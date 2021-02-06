def timeConversion(s):
    # Python3 program to Split string into characters
    a = [char for char in s]
    a[0: 2] = [''.join(a[0: 2])]
    if a[7]=='P':
        a[0]=int(a[0])+12
    a.pop(7)
    a.pop(7)
    for i in a:
        print(i,end='')

if __name__ == '__main__':

    s = input()
    timeConversion(s)