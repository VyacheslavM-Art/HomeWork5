# Задание 1
with open(input("Введите название файла: ")+".txt","w") as file_obj:
    print("Введите текст, для записи в файл:")
    while True:
        s=input()
        if s == "":
            break
        file_obj.writelines(s,"\n")


# Задание 2
with open("my_file.txt") as file_obj:
    contens = file_obj.readlines()
for i in range(len(contens)):
    m = contens[i].split()
    print("В строке {}, слов {}".format(i+1,len(m)))


# Задание 3
with open("asd.txt") as file_obj:
    i = file_obj.readlines()
m=[]
for j in i:
    m.append(j.split())
sums=0
for k,s in m:
    sums += int(s)
    if int(s) < 20000:
        print("Сотрудник {} иммет оклад меньше 20 000".format(k))
print("Средний оклад: ", sums/len(m))


# Задание 4

file1_obj=open("mns.txt")
f2_ob=open("mns1.txt","w")
d={"One":"Один","Two":"Два","Three":"Три","Four":"Четыре"}
for s in file1_obj:
    k=s.split(" - ")
    f2_ob.writelines(d[k[0]]+" — "+k[1])
file1_obj.close()
f2_ob.close()

# Задание 5

with open("Sums.txt","r+") as file_obj:
    file1_obj.write("12 120 154 121 4 512 4 54 21 5 4 21 54 2 1 24 5 21")
    m = file_obj.readline()
k2=[int(i) for i in m.split()]
print("Sum:",sum(k2))

# Задание 6

def remove(value, deletechars):
    for c in deletechars:
        value = value.replace(c, '')
    return value

my_dict={}
with open("Tasks.txt","r", encoding='utf-8') as file1_obj:
    for s in file1_obj:
        m=s.split()
        m[0]=remove(m[0],":")
        for i in range(1,len(m)):
            m[i]=remove(m[i],": ()прлабл-—")
            print(m)
        my_dict[m[0]]= (int(m[1]) if m[1].isdigit() else 0) + (int(m[2]) if m[2].isdigit() else 0) + (int(m[3]) if m[3].isdigit() else 0)
print(my_dict)

# Задание 7

import json
avg_sum = 0
avg_count=0
my_list=[]
my_dict={}
with open("firms.txt","r", encoding='utf-8') as file1_obj:
    for s in file1_obj:
       m=s.split()
       if float(m[2])-float(m[3]) >0:
           avg_sum += float(m[2])-float(m[3])
           avg_count +=1
       print("Прибыль {} составляет {}".format(m[1]+" "+m[0],float(m[2])-float(m[3])))
       my_dict[m[0]]=float(m[2])-float(m[3])
my_list.append(my_dict)
my_dict={"average_profit": avg_sum/avg_count}
my_list.append(my_dict)
print(my_list)
print("Средняя прибыль:",avg_sum/avg_count)

with open("info.json","w", encoding='utf-8') as f_json:
    json.dump(my_list,f_json)