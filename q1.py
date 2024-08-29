first_string = input("enter a string ")
second_string = input("enter another string ")
first_string = set(first_string)
second_string = set(second_string)
if (list(first_string &  second_string) != []):
    print("complementary")
else:
    print("not complementary")