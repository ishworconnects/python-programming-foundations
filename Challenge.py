#Challenge 1: Lets say Nepal has traffic fine Rs.1500 and 20% of the money is contributed to road constructin.Make a function that can calculate money for the road construction.

def find_money_for_road_construction(number_of_people):
    total_money = number_of_people * 1500
    money_for_road_construction = 20/100 * total_money
    return money_for_road_construction

total_money = find_money_for_road_construction(int(input("Enter the number of people: ")))
print(total_money)



