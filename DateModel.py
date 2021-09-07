from DateStruct import DateTAD

class Model:
    def __init__(self):
        return

    def lerData(self):
        while True:
            try:
                day = int(input("Digite o dia: "))
                month = int(input("Digite o mês: "))
                year = int(input("Digite o ano: "))
                date = DateTAD(day, month, year)
                if self.validarData(date) == 1:
                    break
                else:
                    print("Data não existe!")
            except:
                print("valor inválido!")

        return DateTAD(day, month, year)

    def validarData(self, date): 
        if date.month < 1 or date.month > 12 or date.year <= 0:
            return 0            
        
        if date.month in (1, 3, 5, 7, 8, 10, 12):
            last_day = 31
        elif date.month == 2:
            if (date.year % 4 == 0) and (date.year % 100 != 0 or date.year % 400 == 0):
                last_day = 29
            else:
                last_day = 28
        else:
            last_day = 30

        if date.day < 1 or date.day > last_day:
            return 0
        return 1

    def verificarBissexto(self, date):
        if (date.year % 4 == 0) and (date.year % 100 != 0 or date.year % 400 == 0):
            return 1
        return 0

    def verificarPascoa(self, year):
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1 
        return DateTAD(day, month, year)

    def escreverExtenso(self, date):
        month_ext = {1: 'janeiro', 2 : 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
        return (str(date.day) + " de " + month_ext[date.month] + " de " + str(date.year))


        
    

