

target = 10000
act_sales = int(input("Enter sales"))


if act_sales > target:
     print("high target")
elif act_sales > 5000:
      print("medum target")
elif act_sales > 2000 : 
    print("low target")
else : 
    print("no target")
                



t_sales = 1000
t_contact = 40
actuals_sales = int(input('enter sales'))
actuals_contact = int(input('enter contact'))


if actuals_sales >= t_sales and actuals_contact>=t_contact:
    bonus = 0.05*t_sales
else:
    bonus = 0
print("Bonus:", bonus)


