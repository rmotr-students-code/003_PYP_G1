''' It seems easier to ignore all these calculations and just ask the user to pick a specific date. See forms.py '''

from wtforms import IntegerField, validators, DecimalField, TextField, DateField
from flask_wtf import Form 
import datetime

class Savings(Form):
    subject = TextField(u'What did you give up do you want to give up?(optional)?', [validators.required(), validators.length(max=30)])
    user_date = DateField('Date where activity stopped  ' , format='%Y-%m-%d')
    
    def calculate_duration(d1):
        today = datetime.date.today()
        chosen_date = datetime.date(2015, 12, 12)
        diff = chosen_date - today
        return diff
    
    def find_daily_cost():
        cost = IntegerField('How much did you spend?',[validators.NumberRange(min=1, max=1000000000)])
        occurrence = raw_input('How often did you spend this amount? [D]aily, [W]eekly, [M]onthly or [Y]early?').upper()
        daily_cost = 0
    
        if occurrence == 'D':
            daily_cost = cost
        elif occurrence == 'W':
            daily_cost = cost / 7
        elif occurrence == 'M':
            daily_cost = cost / 30.5
        elif occurrence == 'Y':
            daily_cost = cost / 365.25
        else:
		     print "error during occurrence if statement"  
        return daily_cost
  
    def calculate_cost(diff, daily_cost ):
        total_cost = daily_cost * duration_in_days
        return total_cost

#print calculate duration('2015, 12, 15')