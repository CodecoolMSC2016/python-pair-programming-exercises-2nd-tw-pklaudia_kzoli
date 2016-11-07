import datetime 

def years(age):
    age = age 
    name = str(input("Enter your name here : "))
    count = int(input("Enter how many time you want to see the resorts :"))  
    year = datetime.date.today().year
    years_left=(100-age) + year
    for i in range (count):
        print(" Hello {} This year is {} and your age is {} so you have {} till you will be 100 years old".format(name ,year, age, years_left))

    return years_left
def main():

    return 


if __name__ == '__main__':
    main()

