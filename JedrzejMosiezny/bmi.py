def bmi_calc(w, h):
    try:
        w = float(input("podaj wagę w kg: "))
        h = float(input("podaj wzrost w m: "))
        bmi = (w/h**2)
        return(print("Twoje bmi wynosi: " + str(bmi)))
    except TypeError:
        print('wrong types added')
    except ValueError:
        print('cannot change to float type')
    except ZeroDivisionError:
        print('dzielisz przez 0 kretynie')  

bmi_calc(90, 178)