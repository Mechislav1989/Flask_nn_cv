from datetime import *
import time

class Organize:

    def set_date(self, dates):
        if time.strptime(dates, '%d/%m/%Y'):
            self.dates = dates
        else:
            print('Invalid date')

    def add_deal(self, description, suverity, labor_itensivity):
        self.description = description
        self.suverity = suverity
        self.labor_itensivity = labor_itensivity
        deal = {'description': self.description, 'suverity': self.suverity,
                     'labor_itensity': self.labor_itensivity}
        dict_deal = {'dates': [deal]}
        return dict_deal[self.dates].append(deal)

    def del_deal(self, dates):
        return dict_deal[self.dates].pop(deal)


t = Organize()
t.set_date('17/02/2022')
t.add_deal('watch', 'suv', '3')

