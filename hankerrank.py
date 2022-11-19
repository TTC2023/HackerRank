import math

# def plusMinus(arr):
#     positive_num = 0
#     negative_num = 0
#     zero_num = 0
#     for i in range(len(arr)):
#         if arr[i] > 0:
#             positive_num += 1
#         if arr[i] < 0:
#             negative_num += 1
#         if arr[i] == 0:
#             zero_num += 1
#             print(zero_num)
#     return int(format(positive_num/len(arr),'.6f')),round(negative_num/len(arr),6),round(zero_num/len(arr),6)

# x = plusMinus([-4,3,-9,0,4,1])
# print(x)

# def divisibleSumPairs(n, k, ar):
#     outcome = 0
#     for i in range(n):
#         for j in range(n):
#             if i < j:
#                 if (ar[i] + ar[j])%k == 0:
#                     outcome += 1
#     return outcome

# x = divisibleSumPairs(6,3,[1,3,2,6,1,2])
# print(x)

# def gradingStudents(grades):
#     new_grades = []
#     for grade in grades:
#         if grade < 38:
#             new_grades.append(grade)
#         if grade % 5 > 2:
#             rounded_grade = round(grade/5) * 5
#             new_grades.append(rounded_grade)
#     return new_grades
# x= gradingStudents([73,67,38,33])
# print(x)

# def bon_appetite(bill,k,b):
#     total_bill = 0
#     for i in range(len(bill)):
#         total_bill += bill[i]
#     anna = (total_bill - bill[k])/2
#     if anna == b:
#         return "Bon Appetite"
#     if anna != b:
#         return b-anna
# print(bon_appetite([3,10,2,9],1,12))

# def hurdleRace(k, height):
#     tallest = height[0]
#     for i in range(0,len(height)):
#         if height[i] > tallest:
#             tallest = height[i]
#     if k > tallest:
#         print(0)
#     if k < tallest:
#         print(tallest - k)


# print(hurdleRace(4,[1,6,3,5,2]))

# def catAndMouse(x, y, z):
#     cat_A = x-z
#     cat_B = y-z
#     if cat_A < 0:
#         cat_A = cat_A * -1
#     if cat_B < 0:
#         cat_B = cat_B * -1
#     if cat_A > cat_B:
#         print("Cat A")
#     if cat_B > cat_A:
#         print("Cat B")
#     else:
#         print("Mouse C")


# print(catAndMouse(1,3,2))

# def staircase(n):
#     staircase = []
#     spaces = n - 1
#     hashtags = 1
#     for i in range(n):
#         print((' ' * spaces)+('#' * hashtags))
#         spaces -=1
#         hashtags +=1

# print(staircase(7))

# def angryProfessor(k, a):
#     on_time = 0
#     for i in range(len(a)):
#         if a[i] <= 0:
#             print(a[i])
#             on_time += 1
#     if on_time < k:
#         return 'YES'
#     if on_time >= k:
#         return 'NO'

# # yes = cancelled, no = not cancelled
# print(angryProfessor(2,[10,2,-4,-8]))

# def birthday(s, d, m):
#     total_counter = 0
#     for i in range(len(s)):
#         print(s[i:i+m])
#         count = sum(s[i:i+m])
#         if count == d:
#             total_counter += 1
#     return total_counter

# print(birthday([2,2,1,3,2],4,2))

# def viralAdvertising(n):
#     shared = 5
#     cumalative = 2
#     if n > 1:
#         for i in range(1,n):
#             people_shared = math.floor(shared/2) * 3
#             shared = people_shared
#             cumalative += math.floor(shared/2)
#     else: 
#         return 2 
#     return cumalative

# print(viralAdvertising(5))

# def countingValleys(steps, path):
#     elevation = 0
#     valleys = 0
#     for i in range(steps):
#         print(path[i])
#         if path[i] == "U":
#             elevation += 1
#             if elevation ==0:
#                 valleys += 1
#         if path[i] == "D":
#             elevation -=1


#     return valleys

# print(countingValleys(12,'DDUUDDUDUUUD'))

# def designerPdfViewer(h, word):
#     message = word.lower()
#     tallest_letter = 0
#     for i in range(len(message)):
#         number = ord((message[i])) - 97
#         if h[number] > tallest_letter:
#             tallest_letter = h[number]
#     return tallest_letter * 1 * len(message)



# print(designerPdfViewer([6, 5, 7, 3, 6, 7, 3, 4, 4, 2, 3, 7, 1, 3, 7, 4, 6, 1, 2, 4, 3, 3, 1, 1, 3, 5], 'zbkkfhwplj'))

# 5 in the first position, 1 is in the third position [2]
# y = 3, at the fifth place in the list

# def permutationEquation(p):
#     arr = []
#     for i in range(len(p)+1):
#         for j in range(len(p)):
#             if i == p[j]:
#                 for h in range(len(p)):
#                     if p[h] == j+1:
#                         arr.append(h+1)
#     return arr


# print(permutationEquation([5,2,1,3,4]))

# def findDigits(n):
#     total = 0
#     num = str(n)
#     for i in range(len(num)):
#         if int(num[i]) > 0:
#             if n % int(num[i]) == 0:
#                 total += 1
#     return total


# print(findDigits(101))

# def sockMerchant(n, ar):
#     pairs = 0
#     newarr=[]
#     for i in range(n):
#         if i == 0:
#             total = 1
#         else:
#             total = 0
#         for j in range(1,n):
#             if ar[i] in newarr:
#                 break
#             if ar[i] == ar[j]:
#                 total += 1
#         if total > 1:
#             pairs += math.floor(total/2)
#             newarr.append(ar[i])
#     return pairs

# print(sockMerchant(7,[1,2,1,2,1,3,2]))

# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     apple_arr = []
#     orange_arr = []
#     a_hit = 0
#     o_hit = 0
#     for i in range(len(apples)):
#         apple_distance = a + apples[i]
#         apple_arr.append(apple_distance)
#         print(apple_arr)
#     for i in range(len(oranges)):
#         orange_distance = b + oranges[i]
#         orange_arr.append(orange_distance)
#         print(orange_arr)
#     for i in range(len(apple_arr)):
#         if apple_arr[i] >= s and apple_arr[i] <= t:
#             a_hit +=1
#     for i in range(len(orange_arr)):
#         if orange_arr[i] >= s and orange_arr[i] <= t:
#             o_hit +=1
#     return a_hit,o_hit
# print(countApplesAndOranges(7,10,4,12,[2,3,-4],[3,-2,-4]))

# def gradingStudents(grades):
#     new_arr = []
#     for i in range(len(grades)):
#         if grades[i] < 38:
#             new_arr.append(grades[i])
#         if grades[i] >= 38:
#             if grades[i] % 5 >= 3:
#                 new_grade = round(grades[i]/5) * 5
#                 new_arr.append(new_grade)
#             else: 
#                 new_arr.append(grades[i])
#     return new_arr

# print(gradingStudents([37,38]))

# def timeConversion(s):
#     if s[8:] == "AM":
#         if int(s[:2]) == 12:
#             new_time = '00' + s[2:8]
#             return new_time
#         else: 
#             return s[:8]
#     if s[8:] == "PM":
#         if int(s[:2]) == 12:
#             return s[:8]
#         else:
#             add_twelve = int(s[:2]) + 12
#             new_time = str(add_twelve) + s[2:8]
#             return new_time

# print(timeConversion('07:05:45PM'))

# def kangaroo(x1, v1, x2, v2):
#     for n in range(10001):
#         if x1+(n*v1)==x2+(n*v2):
#             return 'YES'
#     return 'NO'

# print(kangaroo(21,6,47,3))

# def getTotalX(a, b):
#     count = 0
#     arr = []
#     if len(a) > 1 and len(b) > 1:
#         for i in range(a[0]+1,b[1]):
#             for j in range(len(a)):
#                 if i > a[j]:
#                     if i%a[j] == 0:
#                         arr.append(i)
#                 else:
#                     if a[j]%i == 0:
#                         arr.append(i)
#             for j in range(len(b)):
#                 if i > b[j]:
#                     if i%b[j] == 0:
#                         arr.append(i)
#                 else:
#                     if b[j]%i == 0:
#                         arr.append(i)
#         for i in range(1,len(arr)):
#             if arr[i-1] != arr[i]:
#                 if arr.count(arr[i]) == 4:
#                     count += 1
#     else:
#         pass
#     return count

# print(getTotalX([1],[100]))

# def diagonalDifference(n,arr):
#     num = 0
#     first_total = 0
#     second_total = 0
#     while num < n:
#         first_total += arr[num][num]
#         num += 1
#     number = n
#     other = 0
#     while number > 0:
#         second_total += arr[other][number-1]
#         number -= 1
#         other += 1
#     return abs(first_total-second_total)

# print(diagonalDifference(3,[[11, 2, 4],[4, 5, 6],[10, 8, -12]]))

# def migratoryBirds(arr):
#     arr.sort(reverse=True)
#     count = 0
#     smallest = 0
#     for i in range(len(arr)):
#         x = arr.count(arr[i])
#         if x >= count:
#             count = x
#             smallest = arr[i]
#     return smallest


# print(migratoryBirds([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]))

# def utopianTree(n):
#     height = 0
#     growth = False
#     for i in range(n+1):
#         if not growth:
#             height += 1
#             growth = True
#         else: 
#             height = height * 2
#             growth = False
#     return height

# print(utopianTree(5))

# def beautifulDays(i, j, k):
#     count = 0
#     for i in range(i,j+1):
#         reverse = str(i)[::-1]
#         problem = abs(i - int(reverse))
#         if problem % k == 0:
#             count += 1
#     return count
# print(beautifulDays(20,23,6))

def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    purchases = []
    for i in range(len(keyboards)):
        if i < b:
            for j in range(len(drives)):
                if keyboards[i] + drives[j] <= b:
                    purchases.append(keyboards[i] + drives[j])
    purchases.sort()
    if len(purchases) > 0:
        return purchases[len(purchases)-1]
    else:
        return -1
    return options


print(getMoneySpent([40,50,60,20,30,15,18],[5,8,12,14,23,43],60))