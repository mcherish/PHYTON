def chess_and_crackers(chess_count,boxes_of_crackers):
    print(f"you have {chess_count} chesses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party!")
    print("get a blanket. \n")

print("we can just give the function number directly.")
chess_and_crackers(10,20)

print("or we can use variables from our script")
amount_of_chess = 11
amount_of_crackers = 21
chess_and_crackers(amount_of_chess,amount_of_crackers)

print("we can even do match inside too.")
chess_and_crackers(10+2,20+2)

print("and we can combine the two,variables and match")
chess_and_crackers(amount_of_chess+3,amount_of_crackers+3)

