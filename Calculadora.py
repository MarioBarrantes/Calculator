while ('Opcion' != 0 ):
        Opcion = input ('''ingrese la opcion que desea ejecutar: 
        1. Suma :
        2. Resta :
        3. Multiplicacion :
        4. Division :
        5. Exponenciacion :
        0. Salir :''')
        


        if Opcion == '1':

                num1 = int (input ("ingrese el primer numero: "))
                num2 = int (input ("ingrese el segundo numero: "))
                suma = num1 + num2
                print ("el resultado de la suma es: ",suma)

        elif Opcion == '2':

                num1 = int (input ("ingrese el primer numero: "))
                num2 = int (input ("ingrese el segundo numero: "))
                resta = num1 - num2
                print ("el resultado de la resta es = ",resta)

        elif Opcion == '3':
                num1 = int (input ("ingrese el primer numero: "))
                num2 = int (input(" ingrese el segundo numero: "))
                multiplicacion = num1 * num2
                print ("el resultado de la multiplicaion es= ",multiplicacion)

        elif Opcion == '4':
                num1 = int (input(" ingrese el primer numero: "))
                num2 = int (input (" ingrese el segundo numero: "))
                division = num1 / num2
                print (" el resultado de la division es = ",division)

        elif Opcion == '5':

                basenum = int (input ("ingrese el numero base "))
                exponum = int (input ("ingrese el exponente: "))
                exponenciacion = basenum ** exponum
                print ("el resultado de la exponenciacion es = ",exponenciacion)

        elif Opcion == '0':
                print ("gracias por usar nuestra calculadora")