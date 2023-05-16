import re

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
    sum_parts = []
    name_parts = name.split()
    for part in name_parts:
        s = sum(list(map(lambda c: (ord(c) - 0x41) % 9 + 1, list(part))))
        sum_parts.append(s)
        
    type1 = reduce_num(sum([reduce_num(part) for part in sum_parts]))
    
    return [type1]
    
def calc_soul_number(name):
    name = re.sub("[AEIOUY]","",name)
    
    sum_parts = []
    name_parts = name.split()
    for part in name_parts:
        s = sum(list(map(lambda c: (ord(c) - 0x41) % 9 + 1, list(part))))
        sum_parts.append(s)
        
    type1 = reduce_num(sum([reduce_num(part) for part in sum_parts]))
    
    return [type1]
    
def calc_act_number(name):
    name = re.sub("[^AEIOUY ]","",name)
    
    sum_parts = []
    name_parts = name.split()
    for part in name_parts:
        s = sum(list(map(lambda c: (ord(c) - 0x41) % 9 + 1, list(part))))
        sum_parts.append(s)
        
    type1 = reduce_num(sum([reduce_num(part) for part in sum_parts]))
    
    return [type1]

name = input("Tên (không dấu): ").upper()
dob = input("Ngày sinh (ddmmyyyy): ")

print(f"Số đường đời: {calc_life_number(dob)}")
print(f"Số vận mệnh: {calc_destiny_number(name)}")
print(f"Số linh hồn: {calc_soul_number(name)}")
print(f"Số hành vi: {calc_act_number(name)}")
