from datetime import date


#Write your function here!

def get_todays_date():

    return (str(date.today().year)+"/"+str(date.today().month)+"/"+str(date.today().day))

#If you want to test your code, you can do so by calling
#your function below. However, this is no longer required
#for grading.
print(get_todays_date())
