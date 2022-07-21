import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = abs(limit) #day limit money/callories
        self.records = [] #clear list of records
    def add_record(self, record_obj): 
        #takes an object of the Record class as an argument 
        # and stores it in the records list
        self.records.append(record_obj)

    def get_stats(self,days):
        summary_amount = 0
        second_date = dt.datetime.now().date() - dt.timedelta(days)
        for i in self.records:
            if second_date <= i.date <= dt.datetime.now().date():
                summary_amount = sum([i.amount], summary_amount)
        return summary_amount 
 
    def get_today_stats(self):
        days = 0
        return self.get_stats(days) 

    def get_week_stats(self):
        days = 7
        return self.get_stats(days)

class Record:
    def __init__(self, amount, comment="", date=""):
        self.amount = amount
        self.comment = comment
        self.date = date
        try:
            if self.date != "":
                self.date = dt.datetime.strptime(self.date, "%d.%m.%Y").date()
            else:
                self.date = dt.datetime.now().date()
        except Exception as e:
            print("Что-то пошло не так(class Record)!")

        print("Create record: Quantity of money or callories"
            f" = {self.amount}, comment for record:"
            f" \"{self.comment}\", date of record: \"{self.date}\".")

class CashCalculator(Calculator):
    USD_RATE = 69.0
    EURO_RATE = 77.0
    RUB_RATE = 1.0

    def get_today_cash_remained(self, currency = "rub"):
        currencies = {
            'eur': ('Euro', self.EURO_RATE),
            'usd': ('USD', self.USD_RATE),
            'rub': ('руб', self.RUB_RATE),
        }     
        sign, rate = currencies.get(currency)
        amount = self.get_today_stats()
        try:
            if self.limit == amount:
                return ("Денег нет, держись")
            elif self.limit < amount:
                delta = round((amount - self.limit)/rate,2)
                return (f"Денег нет, держись: твой долг - {delta} {sign}")
            else:
                delta = round((self.limit - amount)/rate,2)
                return (f"На сегодня осталось {delta} {sign}")
        except Exception as e:
            print("Что-то пошло не так(class CashCalculator)!")

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        now_amount = self.get_today_stats()
        try:
            if self.limit <= now_amount:
                return ("Хватит есть!")
            else:
                delta = self.limit - now_amount
                return ("Сегодня можно съесть что-нибудь ещё, но с общей "
                    f"калорийностью не более {delta} кКал")
        except Exception as e:
            print("Что-то пошло не так(class CaloriesCalculator)!")
            
def main():
    cash_calculator = CashCalculator(2500)
    cash_calculator.add_record(Record(amount=150, comment="кофе")) 
    cash_calculator.add_record(Record(amount=100, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=300, comment="бар в Танин др", date="08.11.2019"))
    cash_calculator.add_record(Record(amount=100, comment="За 20_07_2022", date="20.07.2022"))
    cash_calculator.add_record(Record(amount=200, comment="За 19_07_2022", date="19.07.2022"))
    cash_calculator.add_record(Record(amount=300, comment="За 18_07_2022", date="18.07.2022"))
    cash_calculator.add_record(Record(amount=400, comment="За 17_07_2022", date="17.07.2022"))
    cash_calculator.add_record(Record(amount=500, comment="За 16_07_2022", date="16.07.2022"))
    cash_calculator.add_record(Record(amount=600, comment="За 15_07_2022", date="15.07.2022"))
    cash_calculator.add_record(Record(amount=700, comment="За 14_07_2022", date="14.07.2022"))
    cash_calculator.add_record(Record(amount=800, comment="За 13_07_2022", date="13.07.2022"))
    cash_calculator.add_record(Record(amount=900, comment="За 12_07_2022", date="12.07.2022"))
    print(cash_calculator.get_today_cash_remained("rub"))
    print(cash_calculator.get_today_cash_remained("usd"))
    print(cash_calculator.get_today_cash_remained("eur"))
    print(cash_calculator.get_today_cash_remained())
    print(cash_calculator.get_today_stats())
    print(cash_calculator.get_week_stats())
    cash_calculator2 = CaloriesCalculator(100)
    cash_calculator2.add_record(Record(amount=300, comment="За 21_07_2022"))
    cash_calculator2.add_record(Record(amount=200, comment="За 21_07_2022_2"))
    cash_calculator2.add_record(Record(amount=100, comment="За 20_07_2022", date="20.07.2022"))
    cash_calculator2.add_record(Record(amount=200, comment="За 19_07_2022", date="19.07.2022"))
    cash_calculator2.add_record(Record(amount=300, comment="За 18_07_2022", date="18.07.2022"))
    cash_calculator2.add_record(Record(amount=400, comment="За 17_07_2022", date="17.07.2022"))
    cash_calculator2.add_record(Record(amount=500, comment="За 16_07_2022", date="16.07.2022"))
    cash_calculator2.add_record(Record(amount=600, comment="За 15_07_2022", date="15.07.2022"))
    cash_calculator2.add_record(Record(amount=700, comment="За 14_07_2022", date="14.07.2022"))
    cash_calculator2.add_record(Record(amount=800, comment="За 13_07_2022", date="13.07.2022"))
    cash_calculator2.add_record(Record(amount=900, comment="За 12_07_2022", date="12.07.2022"))
    cash_calculator2.add_record(Record(amount=900, comment="За 12_09_2023", date="12.09.2023"))
    print(cash_calculator2.get_calories_remained())
    print(cash_calculator2.get_today_stats())
    print(cash_calculator2.get_week_stats())

if __name__ == '__main__':
    main()