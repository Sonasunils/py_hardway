
#declare function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("Man that enough for a party!")
    print("Get a blanket.]\n")

print("We can just give the function numbers directly")
cheese_and_crackers(20,30)
print("OR,we can use variables from our script:")
amount_of_cheese=10  
amount_of_crackers=50
#function call
cheese_and_crackers(amount_of_cheese,amount_of_crackers) 
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)
print("And we acn combine the two..Variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000) 