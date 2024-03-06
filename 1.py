import csv

with open('scientist.txt', encoding='utf-8') as file:
    reader = list(csv.DictReader(file,delimiter='#'))

    scientists = []
    preparations = []
    was = False
    reader = sorted(reader, key=lambda x: x['date'])
    print('Разработчиками Аллопуринола были такие люди')
    for row in reader:
        if row['preparation'] not in preparations:
            preparations.append(row['preparation'])
            scientists.append(row)
        if row['preparation'] == 'Аллопуринол':
            if not was:
                name = row['ScientistName']
                was = True
            print(f'{row["ScientistName"]} - {row["date"]}')
        print(f'Оригинальный рецепт принадлежит: {name}')
with open('scientist_origin.txt', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, filenames=['ScientistName', 'preparation', 'date', 'components'], delimiter='#')
    writer.writeheader()
    writer.writerows(scientists)







