total_money = 100
chocolate_price = 7
# define two parameters that can be changed
def chocolate_calcul(total_money,chocolate_price) :
    number_bar = total_money//chocolate_price
    money_left = total_money-number_bar*chocolate_price
    print(str(number_bar)+' bars can be brought.')
    print(str(money_left)+' are left over.')
    return
# define the function
chocolate_calcul(total_money,chocolate_price)
# use the function and print the result
