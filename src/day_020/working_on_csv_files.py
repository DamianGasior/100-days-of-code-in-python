import csv

with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\dane.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)#skipping the first line
    count=0
    total=0
    for row in reader:
        print(row)   # każda linia to lista
        total+=float(row[2])
        count+=1

    average_age=total/count
    print(f'Average age is {average_age}')
    

print(' Based on file "dane.csv" we build a new file "new_data.csv" ')

with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\dane.csv",mode='r', newline="", encoding="utf-8") as t:
    reader1 = csv.reader(t)
    
    print('przygotowanie do nowego pliku')
    headings=next(reader1)#saving the headins
    print(headings)
    


    with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\new_data.csv", mode='w', newline='', encoding='utf-8') as g:
        writer=csv.writer(g)
        # print(headings)
        writer.writerow([headings[0],headings[1],headings[2]])
        for row in reader1:
            if float(row[2])<30:
                writer.writerow([row[0],row[1],row[2]])

print(' Based on file: "new_data_with_city.csv" we build a new file "new_data.csv" ')

with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\new_data.csv", mode='r', newline='', encoding='utf-8') as k:
    reader2=csv.reader(k)
    headings2=next(reader2)
    headings2.append('city')

    with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\new_data_with_city.csv", mode='w', newline='', encoding='utf-8') as p:
        writer1=csv.writer(p)
        writer1.writerows([headings2])
        # next(reader2)
        for row in reader2:
            row.append("")
            writer1.writerow(row)
    print('end of adding city column, new file was created')
        


print('starting the process of merging')

with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\merged.csv", mode='w', newline="", encoding='utf-8') as merged:
    writer=csv.writer(merged)

    #first file
    with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\dane.csv", newline="", encoding="utf-8") as f1:
        reader3=csv.reader(f1)
        headings3=next(reader3) # copying headings
        writer.writerow(headings3)
        for row in reader3:
            writer.writerow(row)
        
    #second file
    with open(r"c:\Users\Admin\Desktop\Python\repository_dg\100-days-of-code-in-python\src\day_020\new_data.csv", mode='r', newline='', encoding='utf-8') as k1:
        reader4=csv.reader(k1)
        next(reader4) #skip headings
        for row in reader4:
            writer.writerow(row)


print('Files were mreged')