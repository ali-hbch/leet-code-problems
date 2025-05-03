def string_to_number (string) :
    chars = list(string)
    result = ''
    print (chars)
    for i in chars :
        if i == ' ' :
            result = result + '0'
            result = result + ' '
            continue
        elif  ord(i) <= 122 and ord(i) >= 119 : 
            for j in range(ord(i)-118 ) :
                result = result + f'{int((ord(i)-95)/4) + 3}'
                continue
            result = result + ' '
        elif ord(i) <= 115 and ord(i) >= 112 :
            for j in range(ord(i) - 111) :
                result = result + f'{int((ord(i)-95)/4) + 3 }'
                continue
            result = result + ' '
        else :
            for j in range ((ord(i)-97)%3 + 1) :
                result = result + f'{int((ord(i)-97)/3) + 2}'
            result = result + ' '
    return result
def number_to_string (string) :
    numbers =string.split()
    print (numbers)
    result = ''
    for i in numbers :
        if (i == '0') :
            result = result + ' '
            continue
        j = int(i[0])
        if (j ==9) :
            result = result+ chr(int((j-3)*4 + 95) + (len(i)+3)%4)
            continue
        
        if (j ==7) :
            result = result+chr(int((j-3)*4 + 96) + (len(i)+3)%4)
            continue
        result = result + chr(int((j-2)*3 + 96) + (len(i)+2)%3)
    return result

print ("0 : string to nokia numbers")
print ("1 : nokia numbers to string")

choice = input ()

if (choice == '0') :
    print ("enter the string : ")
    x = input ()
    print (string_to_number(x))

if (choice == '1') :
    print ("enter the string : ")
    x = input ()
    print (number_to_string(x))