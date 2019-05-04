import csv

age = []
workclass = []
education = []
martialStat = []
occupation = []
relationship = []
hpw = []
arrayHasil = []

percentClass1Y = 0
percentClass1N = 0
percentClass2Y = 0
percentClass2N = 0
percentClass3Y = 0
percentClass3N = 0

# read file
with open('TrainsetTugas1ML.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            age.append([row[1], row[8]])
            workclass.append([row[2], row[8]])
            education.append([row[3], row[8]])
            martialStat.append([row[4], row[8]])
            occupation.append([row[5], row[8]])
            relationship.append([row[6], row[8]])
            hpw.append([row[7], row[8]])

# print(age)
# print(workclass)

def itungPersen(array):
    class1Y = 0
    class1N = 0
    class2Y = 0
    class2N = 0
    class3Y = 0
    class3N = 0
    global percentClass1Y
    global percentClass1N
    global percentClass2Y
    global percentClass2N
    global percentClass3Y
    global percentClass3N
    for i in range(0, len(array)):
        if array[i][0] == 'young' or array[i][0] == 'old' or array[i][0] == 'adult':
            if array[i][0] == 'young':
                if array[i][1] == '>50K':
                    class1Y += 1
                else:
                    class1N += 1
            elif array[i][0] == 'old':
                if array[i][1] == '>50K':
                    class2Y += 1
                else:
                    class2N += 1
            else:
                if array[i][1] == '>50K':
                    class3Y += 1
                else:
                    class3N += 1
        elif array[i][0] == 'Private' or array[i][0] == 'Local-gov' or array[i][0] == 'Self-emp-not-inc':
            if array[i][0] == 'Private':
                if array[i][1] == '>50K':
                    class1Y += 1
                else:
                    class1N += 1
            elif array[i][0] == 'Local-gov':
                if array[i][1] == '>50K':
                    class2Y += 1
                else:
                    class2N += 1
            else:
                if array[i][1] == '>50K':
                    class3Y += 1
                else:
                    class3N += 1
        elif array[i][0] == 'Some-college' or array[i][0] == 'Bachelors' or array[i][0] == 'HS-grad':
            if array[i][0] == 'Some-college':
                if array[i][1] == '>50K':
                    class1Y += 1
                else:
                    class1N += 1
            elif array[i][0] == 'Bachelors':
                if array[i][1] == '>50K':
                    class2Y += 1
                else:
                    class2N += 1
            else:
                if array[i][1] == '>50K':
                    class3Y += 1
                else:
                    class3N += 1
        elif array[i][0] == 'Married-civ-spouse' or array[i][0] == 'Never-married' or array[i][0] == 'Divorced':
            if array[i][0] == 'Married-civ-spouse':
                if array[i][1] == '>50K':
                    class1Y += 1
                else:
                    class1N += 1
            elif array[i][0] == 'Never-married':
                if array[i][1] == '>50K':
                    class2Y += 1
                else:
                    class2N += 1
            else:
                if array[i][1] == '>50K':
                    class3Y += 1
                else:
                    class3N += 1
        elif array[i][0] == 'Prof-specialty' or array[i][0] == 'Craft-repair' or array[i][0] == 'Exec-managerial':
            if array[i][0] == 'Prof-specialty':
                if array[i][1] == '>50K':
                    class1Y += 1
                else:
                    class1N += 1
            elif array[i][0] == 'Craft-repair':
                if array[i][1] == '>50K':
                    class2Y += 1
                else:
                    class2N += 1
            else:
                if array[i][1] == '>50K':
                    class3Y += 1
                else:
                    class3N += 1
        elif array[i][0] == 'Husband' or array[i][0] == 'Not-in-family' or array[i][0] == 'Own-child':
            if array[i][0] == 'Husband':
                if array[i][1] == '>50K':
                    class1Y += 1
                else:
                    class1N += 1
            elif array[i][0] == 'Not-in-family':
                if array[i][1] == '>50K':
                    class2Y += 1
                else:
                    class2N += 1
            else:
                if array[i][1] == '>50K':
                    class3Y += 1
                else:
                    class3N += 1
        elif array[i][0] == 'normal' or array[i][0] == 'low' or array[i][0] == 'many':
            if array[i][0] == 'normal':
                if array[i][1] == '>50K':
                    class1Y += 1
                else:
                    class1N += 1
            elif array[i][0] == 'low':
                if array[i][1] == '>50K':
                    class2Y += 1
                else:
                    class2N += 1
            else:
                if array[i][1] == '>50K':
                    class3Y += 1
                else:
                    class3N += 1

    percentClass1Y = class1Y / countY
    percentClass1N = class1N / countN
    percentClass2Y = class2Y / countY
    percentClass2N = class2N / countN
    percentClass3Y = class3Y / countY
    percentClass3N = class3N / countN

    if percentClass1Y == 0 or percentClass2Y == 0 or percentClass3Y == 0 or percentClass1N == 0 or percentClass2N == 0 or percentClass3N == 0:
        percentClass1Y = (class1Y + 1) / (countY + 3)
        percentClass1N = (class1N + 1) / (countN + 3)
        percentClass2Y = (class2Y + 1) / (countY + 3)
        percentClass2N = (class2N + 1) / (countN + 3)
        percentClass3Y = (class3Y + 1) / (countY + 3)
        percentClass3N = (class3N + 1) / (countN + 3)

    return percentClass1Y, percentClass1N, percentClass2Y, percentClass2N, percentClass3Y, percentClass3N

    # print('------class age------')
    # print(adultN, adultY, youngN, youngY, oldN, oldY)
    # print(percentAdultN, percentAdultY, percentYoungN, percentYoungY, percentOldN, percentOldY)

def naiveBayes(array):
    hasilY = 0
    hasilN = 0

    global arrayHasil
    for i in range(0, len(array)):
        if array[i][1] == 'young':
            hasilY = percentYoungY * percentY
            hasilN = percentYoungN * percentN
        elif array[i][1] == 'adult':
            hasilY = percentAdultY * percentY
            hasilN = percentAdultN * percentN
        elif array[i][1] == 'old':
            hasilY = percentOldY * percentY
            hasilN = percentOldN * percentN

        if array[i][2] == 'Private':
            hasilY *= percentPrivateY
            hasilN *= percentPrivateN
        elif array[i][2] == 'Local-gov':
            hasilY *= percentLocalGovY
            hasilN *= percentLocalGovN
        elif array[i][2] == 'Self-emp-not-inc':
            hasilY *= percentSelfY
            hasilN *= percentSelfN

        if array[i][3] == 'Some-college':
            hasilY *= percentSomeColY
            hasilN *= percentSomeColN
        elif array[i][3] == 'Bachelors':
            hasilY *= percentBachelorY
            hasilN *= percentBachelorN
        elif array[i][3] == 'HS-grad':
            hasilY *= percentHSY
            hasilN *= percentHSN

        if array[i][4] == 'Married-civ-spouse':
            hasilY *= percentMarriedY
            hasilN *= percentMarriedN
        elif array[i][4] == 'Never-married':
            hasilY *= percentNeverY
            hasilN *= percentNeverN
        elif array[i][4] == 'Divorced':
            hasilY *= percentDivorcedY
            hasilN *= percentDivorcedN

        if array[i][5] == 'Prof-specialty':
            hasilY *= percentProfY
            hasilN *= percentProfN
        elif array[i][5] == 'Craft-repair':
            hasilY *= percentCraftY
            hasilN *= percentCraftN
        elif array[i][5] == 'Exec-managerial':
            hasilY *= percentExecY
            hasilN *= percentExecN

        if array[i][6] == 'Husband':
            hasilY *= percentHusbandY
            hasilN *= percentHusbandN
        elif array[i][6] == 'Not-in-family':
            hasilY *= percentNotY
            hasilN *= percentNotN
        elif array[i][6] == 'Own-child':
            hasilY *= percentOwnY
            hasilN *= percentOwnN

        if array[i][7] == 'normal':
            hasilY *= percentNormalY
            hasilN *= percentNormalN
        elif array[i][7] == 'low':
            hasilY *= percentLowY
            hasilN *= percentLowN
        elif array[i][7] == 'many':
            hasilY *= percentManyY
            hasilN *= percentManyN

        #masukin hasil ke arrayHasil
        if hasilY > hasilN:
            arrayHasil.append('>50K')
        elif hasilY < hasilN:
            arrayHasil.append('<=50K')
        else:
            print('error')

    return arrayHasil

# ngitung persenan label
countY = 0
countN = 0
for i in range(0, len(age)):
    if age[i][1] == '>50K':
        countY += 1
    else:
        countN += 1

percentY = countY / len(age)
percentN = countN / len(age)
# print('------label------')
# print(countN, countY)
# print(percentN, percentY)

itungPersen(age)
percentYoungY = percentClass1Y
percentYoungN = percentClass1N
percentOldY = percentClass2Y
percentOldN = percentClass2N
percentAdultY = percentClass3Y
percentAdultN = percentClass3N

itungPersen(workclass)
percentPrivateY = percentClass1Y
percentPrivateN = percentClass1N
percentLocalGovY = percentClass2Y
percentLocalGovN = percentClass2N
percentSelfY = percentClass3Y
percentSelfN = percentClass3N

itungPersen(education)
percentSomeColY = percentClass1Y
percentSomeColN = percentClass1N
percentBachelorY = percentClass2Y
percentBachelorN = percentClass2N
percentHSY = percentClass3Y
percentHSN = percentClass3N

itungPersen(martialStat)
percentMarriedY = percentClass1Y
percentMarriedN = percentClass1N
percentNeverY = percentClass2Y
percentNeverN = percentClass2N
percentDivorcedY = percentClass3Y
percentDivorcedN = percentClass3N

itungPersen(occupation)
percentProfY = percentClass1Y
percentProfN = percentClass1N
percentCraftY = percentClass2Y
percentCraftN = percentClass2N
percentExecY = percentClass3Y
percentExecN = percentClass3N

itungPersen(relationship)
percentHusbandY = percentClass1Y
percentHusbandN = percentClass1N
percentNotY = percentClass2Y
percentNotN = percentClass2N
percentOwnY = percentClass3Y
percentOwnN = percentClass3N

itungPersen(hpw)
percentNormalY = percentClass1Y
percentNormalN = percentClass1N
percentLowY = percentClass2Y
percentLowN = percentClass2N
percentManyY = percentClass3Y
percentManyN = percentClass3N

dataTest = []

# read file
with open('TestsetTugas1ML.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            dataTest.append(row)

# print(dataTest)

naiveBayes(dataTest)

# print(arrayHasil)

#write file
with open('TebakanTugas1ML.csv', 'w', newline='') as new_file:
    csv_writer = csv.writer(new_file)
    for row in range(0,len(arrayHasil)):
        # print(idx)
        csv_writer.writerow([arrayHasil[row]])

print('TebakanTugas1ML.csv saved!!!!')
print(arrayHasil)