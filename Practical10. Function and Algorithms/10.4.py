
number_bar = 0
def chocolate_calcul(total_money,chocolate_price) :
    number_bar = total_money//chocolate_price
    money_left = total_money-number_bar*chocolate_price
    print(str(number_bar)+' bars can be brought.')
    print(str(money_left)+' are left over.')
    return
chocolate_calcul(100,7)
