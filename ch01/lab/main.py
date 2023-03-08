import random
weeks = 16
classes = 3
tuition= 6000
cost_per_week= ((tuition/classes)/weeks)
print("Cost per week:", cost_per_week)
classes_per_week= 8
cost_per_class= (cost_per_week/classes_per_week)
print("How much for every class:",cost_per_class)
print(cost_per_class, type(cost_per_class))
print(classes_per_week, type(classes_per_week))
print(cost_per_week, type(cost_per_week))
list= (1,2,3.5,5,8)
Randomization=random.choice(list)
print(Randomization) 
