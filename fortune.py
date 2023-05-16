exception = [11, 22, 33]

def reduce_num(num):
    if (num in exception) or (num < 10): 
        return num
        
    s = 0
    while num: 
        s += num % 10;
        num = num // 10;
        
    return reduce_num(s)

def calc_life_number(dob):
    dd = int(dob[:2])
    mm = int(dob[2:4])
    yyyy = int(dob[4:])
    
    # Cộng rút gọn
    type1 = reduce_num(reduce_num(dd)+reduce_num(mm)+reduce_num(yyyy))
    
    # Cộng gộp ngang
    type2 = reduce_num(sum(list(map(int, list("22031997")))))
    
    # Cộng gộp dọc
    type3 = reduce_num(dd+mm+yyyy)

    return [type1, type2, type3]
    
def calc_destiny_number(name):
    name = name

name = input("Tên (không dấu): ").upper()
dob = input("Ngày sinh (ddmmyyyy): ")

life_number = calc_life_number(dob)
destiny_number = calc_destiny_number(name)

print(f"Số đường đời: {life_number}")
print(f"Số vận mệnh: {destiny_number}")
