#list=[] #empty list
#l=list() #empty list
"""
l=[10,20,30,40,50]
print(l)
l[1]=60     #Replace 20 with 60
print(l)
#List Methods
l.append(70) #add 70 at the end of the list
print(l)
l.insert(6,80)  #add 80 at index 6
print(l)
l2=[20,90,100]
l.extend(l2)  #add l2 at the end of l
print(l)
l.pop()     #remove last element of the list
print(l)
l.pop(1)    #remove element at index 1
print(l)
l.append(20)
print(l)
l.append(10)
print(l)
l.remove(20)        #remove first occurrence of 20
print(l)
print(l.count(10))  #count the number of occurrences of 10
l.reverse()  #reverse the list  
print(l)   
l.sort()    #sort the list in ascending order
print(l)
(print(l.index(10)))  #return the index of first occurrence of 10
l.clear()  #remove all elements from the list
"""
#-------------------------------------------------------------------------------------------------------------------------------------------------
"""
#Sum of smallest and largest number in the list
l=[10,20,30,40,50]
#print(min(l)+max(l))
#print(l[0]+l[-1])
v=l.pop(0)
v2=l.pop(-1)
sum=v+v2
print(sum)
"""
#  1. The Guest List Manager (append, insert, remove)This program mimics an event planner managing a party invitation list
"""
Guests=['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
print("Initial guest list: ",Guests)
Guests.append('Gary')
print(Guests)
Guests.insert(0,'Ani')
print(Guests)
Guests.remove('Alice')
print(Guests)
"""
# the Undo Stack (pop)This program shows how text editors use lists to track your history and perform an "Undo" action by removing the last item.
"""
Stacks=["Hello", "World",  "Java", "Python"]
print("Current Stack: ",Stacks)
s=Stacks.pop()
print("After Undo: ",Stacks)
print("Popped Element: ",s)
Stacks.pop(2)
print("After: ",Stacks)
"""
#  Shopping Cart Merger (extend)This program demonstrates how to merge a temporary quick-buy list into a main shopping cart.
"""
Cart=['Apples', 'Bananas', 'Cherries']
print("Main Cart: ",Cart)
QuickBuy=['Dates', 'Elderberries']
Cart.extend(QuickBuy)
print("After Merging: ",Cart)
"""
#  Leaderboard Organizer (sort, reverse, index)This program processes a list of game high scores, arranges them from highest to lowest, and finds where a specific score sits.
"""
Scores=[89,78,99,76,56,39,90]
print("Original Scores: ",Scores)
Scores.sort()                           or Scores.sort(reverse=True)  #sort in descending order
print("Sorted Scores: ",Scores)
Scores.reverse()
print("Reversed Scores: ",Scores)
print("Index of 76: ",Scores.index(76))
"""
#  Attendance Tally (count, clear)This program counts how many days a student was present and cleans up the logs at the end of the semester.
"""
attendance=['p','a','a','p','a']
print("Attendance Record: ",attendance)
print("Days Present: ",attendance.count('p'))
print("Days Absent: ",attendance.count('a'))
attendance.clear()
"""

#Write code to perform the following actions in order:
"""Add "Song D" to the very end of the playlist.
Insert a surprise tracks named "Special Intro" at the very beginning (index 0).
Remove "Song B" from the playlist because the user skipped it too many times.
Print the final playlist.

playlist = ["Song A", "Song B", "Song C"]
print("Initial Playlist: ", playlist)
playlist.append("Song D")
print("After adding 'Song D': ", playlist)
playlist.insert(0, "Special Intro")
print("After inserting 'Special Intro': ", playlist)
print("Removing 'Song B' from the playlist.",playlist.remove("Song B"))
print("Final Playlist: ", playlist)
"""

#Write code to:
"""Count how many times the score 100 appears in the list and print it.
Sort the scores from highest to lowest (Hint: Use two methods back-to-back or an argument inside .sort()).
Print the final sorted list.

scores = [100, 50, 100, 200, 50, 300, 100]
print("Initial Scores: ", scores)
print("Count of 100: ", scores.count(100))
print("Sorting scores from highest to lowest.",scores.sort(reverse=True))
print("Final Sorted Scores: ", scores)
"""

#Write code to:
"""Merge all the items from the truck onto the shelf using a single list method.
The warehouse manager decides to take the very last item off the updated shelf to inspect it. 
Use a method to remove that last item and save it in a variable called inspected_item.
Print the inspected_item.Print the final items left on the shelf.

shelf = ["Hammer", "Screwdriver"]
truck = ["Nails", "Saw", "Drill"]
print("Initial Shelf and truck: ", shelf, truck)
shelf.extend(truck)
print("After merging truck onto shelf: ", shelf)
inspected_item = shelf.pop()
print("Inspected Item: ", inspected_item)
print("Final Items on Shelf: ", shelf)
"""

#Write a program to:
"""Find the exact position (index) of "Code feature" using a method and store it in a variable.
Use that variable to insert a brand new task called "Urgent Bugfix" right before "Code feature" (so it takes over that exact index).
Remove the very first task in the list because it is completed, but make sure to print the name of the removed task so the user knows what got finished.
Print the final list.

tasks = ["Email client", "Buy groceries", "Code feature", "Call mom"]
print("Initial Tasks: ", tasks)
t=tasks.index("Code feature")
print("Index of 'Code feature': ", t)
tasks.insert(t, "Urgent Bugfix")
print("After inserting 'Urgent Bugfix': ", tasks)
print("Removed",tasks.pop(0))
print("Final Tasks: ", tasks)
"""

#Write a program to:
"""Figure out which user ID registered the most times by checking the counts. (Hint: Look at 101).
Remove only the first occurrence of that duplicate ID from the list.
Check the count of that ID again to make sure it dropped.Print the final list.

user_ids = [101, 102, 103, 101, 104, 102, 105, 101]
print(user_ids.count(101))
user_ids.remove(101)
print("Removing the first occurrence of 101.")
print(user_ids.count(101))
print("Final User IDs: ", user_ids)
"""

#Write a program to:
"""Merge the regular_line into the vip_line so that all VIPs remain at the front of the combined list.
The security guard suddenly announces that the venue is at capacity and the last two people in the combined line cannot enter.
Use list methods to remove them one by one.
Print the names of the two people who were turned away.
Print the final line of people who successfully got in."""

regular_line = ["Tom", "Sam", "Ben"]
vip_line = ["Anna", "Elsa"]
print("Initial Lines: ", regular_line, vip_line)
vip_line.extend(regular_line)
print("After merging regular line into VIP line: ", vip_line)
p1=vip_line.pop()
p2=vip_line.pop()
print("Turned away: ", p1, "and", p2)
print("Final Line: ", vip_line)