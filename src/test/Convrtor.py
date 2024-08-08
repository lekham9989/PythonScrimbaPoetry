# Convertor
name1 = input('What is your name?:')
Distance_Km = input('Enter the distance in km?:')
Distance_Mi = float(Distance_Km) / 1.609
print(f'Hello {name1.title()}! You walked {Distance_Km} kms which is {round(Distance_Mi, 1)} miles ')      # formatted strings

