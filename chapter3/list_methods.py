a = [1,10,3,7,20]
# li_sorted = a.sort() is a wrong way to sort a list. output will be none.
# a.sort()  # sorting the elements of list.
#a.append(100)
#a.reverse() #reverse theh lise
#a.pop(2) #will remove the element from the given index. in this 2 is the given index.
# a.remove(20) will remove the element that we want.
# a.insert(2,199) # will insert the element to its assigned index.
print(a)


# Question to take input of marks from the students and print it in sorted manner.
Marks1 = int(input("Enter the marks of student 1 : "))
Marks2 = int(input("Enter the marks of student 2 : "))
Marks3 = int(input("Enter the marks of student 3 : "))
Marks4 = int(input("Enter the marks of student 4 : "))
Marks5 = int(input("Enter the marks of student 5 : "))
Marks6 = int(input("Enter the marks of student 6 : "))
Score_sorted_list = [Marks1,Marks2,Marks3,Marks4,Marks5,Marks6]
Score_sorted_list.sort()
print(Score_sorted_list)