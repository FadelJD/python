Imports System

Module Program
    Sub Main(args As String())
        Dim User, Pass As String
        Dim StoredName As String = ("achmed")
        Dim StoredPass As String = ("123")
        Dim Correct As Boolean = False
        Dim count As Integer = 0
        Dim Ans As Char
        Dim SecQue = ("Are you Mr. Ackerman?")
        Do
            Do
                If count < 3 Then
                    Console.Write("Enter Username: ")
                    User = Console.ReadLine()
                    Console.Write("Enter Password: ")
                    Pass = Console.ReadLine()
                    count += 1
                    If (User = StoredName) And (Pass = StoredPass) Then
                        Console.WriteLine("Access Granted!")
                        Correct = True
                    Else
                        Console.WriteLine("Login Failed")
                    End If
                End If
            Loop Until (Correct = True) Or (count >= 3)
            If Correct = False Then
                Console.Write(SecQue & " Ans = 'Yes/No' only: ")
                Ans = Console.ReadLine()
                If Ans = ("Y") Then
                    Console.WriteLine("Access Granted!")
                    Console.WriteLine("Your username: " & StoredName & " & Your password: " & StoredPass)
                    Console.WriteLine("Successfully sent details to Email!")
                Else
                    count = 0
                End If
            End If
        Loop Until Correct = True Or Ans = "Y"
        Console.ReadKey()
    End Sub
End Module





Imports System

Module Program
    Sub Main(args As String())
        Dim bank As String
        Dim amount, feetotal As Double

        Do
            Console.WriteLine("enter bank type: 'same' OR 'different' only")
            bank = Console.ReadLine()
        Loop Until bank = ("same") Or bank = ("different")
        Console.Write("enter amount: ")
        amount = Console.ReadLine()
        If bank = ("same") Then
            If amount > 10000 Then
                feetotal = amount * 0.01
            Else feetotal = 0
            End If

        Else
            feetotal = 50 + (amount * 0.01)
        End If
        Console.WriteLine("For your total amount = " & amount & " and your total fee = " & feetotal)
        Console.ReadKey()
    End Sub
End Module



Imports System

Module Program
    Sub Main(args As String())
        Dim CustType As String
        Dim ChargeCard As Boolean
        Dim OrderPrice, TotDis, BonusCoup, FinPrice As Double
        Dim Ans As String

        Console.WriteLine("Enter the type of customer you are: 'preffered' OR 'regular'")
        CustType = Console.ReadLine()
        If CustType = ("preffered") Then
            Console.Write("Enter the price of items that you ordered (Total): ")
            OrderPrice = Console.ReadLine()
            Console.Write("Did you  use a charge card: (Y/N) only ")
            Ans = Console.ReadLine()
            If Ans = ("Y") Then
                ChargeCard = True
            ElseIf Ans = ("N") Then
                ChargeCard = False
            End If
            If OrderPrice > 1000 Then
                BonusCoup = 0
                FinPrice = OrderPrice * 0.95
                If ChargeCard = True Then
                    FinPrice = FinPrice * 0.95
                End If

            ElseIf 0 < OrderPrice <= 1000 Then
                BonusCoup = 25
                FinPrice = OrderPrice
                TotDis = 0
            End If
        Else
            Console.Write("Enter the price of items that you ordered (Total): ")
            OrderPrice = Console.ReadLine()
            BonusCoup = 5
            TotDis = 0
            FinPrice = OrderPrice
        End If
        Console.WriteLine("Your FinPrice =  " & FinPrice & " with a bonus coupon of: " & BonusCoup)
        Console.ReadKey()
    End Sub
End Module
