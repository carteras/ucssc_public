camper_van = 11_500

daily_rental = 188
storage = 200*12
rego = 622
insurance = 300
on_going = storage+rego+insurance



for days_on_holidays in range(10, 30):
    for days_to_pay_off_on_going in range(24, 4, -1):
        count = 0
        days_spent = camper_van/daily_rental + days_to_pay_off_on_going#on_going/daily_rental
        while days_spent>0:
            days_spent -= days_on_holidays
            days_spent += days_to_pay_off_on_going#on_going/daily_rental
            count += 1
            # print(days_spent)
            if days_spent > 100:
                break
        print(count)
# print(on_going)
# print(camper_van/daily_rental)
# print(on_going/daily_rental)

