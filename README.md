# Python-Bibliotheca
more python practice before ProjectEuler

## Temperature converter

#### Description

  Write two functions that will convert temperatures back and forth from the Celsius and Fahrenheit temperature scales. The formulas for making the conversion are as follows:

    Tc=(5/9)*(Tf-32)
    Tf=(9/5)*Tc+32
  where Tc is the Celsius temperature and Tf is the Fahrenheit temperature. More information and further descriptions of how to do the conversion can be found at this NASA Webpage. If you finish this assignment quickly, add a function to calculate the wind chill.

#### Input

Your program should ask the user to input a temperature and then which conversion they would like to perform.

#### Sample session

    Temperature converter

    Enter a temperature: 20
    Convert to (F)ahrenheit or (C)elsius? F

    20 C = 68 F
# Answer: Solved.



## Guessing game

#### Description

The computer will pick a number between 1 and 100. (You can choose any high number you want.) The purpose of the game is to guess the number the computer picked in as few guesses as possible.

#### Input

The user will enter his or her guess until the correct number is guessed.

#### Output

The program will keep asking the user to guess until he or she gets the number correct. Then the program will print how many guesses were required.

#### Sample session

    Time to play a guessing game.

    Enter a number between 1 and 100: 62
    Too high. Try again: 32
    Too low. Try again: 51
    Too low. Try again: 56

    Congratulations! You got it in 4 guesses.
## Solved


#### Leap year finder

#### Description

Leap years occur according to the following formula: a leap year is divisible by four, but not by one hundred, unless it is divisible by four hundred. For example, 1992, 1996, and 2000 are leap years, but 1993 and 1900 are not. The next leap year that falls on a century will be 2400.

#### Input

Your program should take a year as input.

#### Output

Your program should print whether the year is or is not a leap year.

#### Sample Session

    What year: 1999
    1999 is not a leap year.

    What year: 1988
    1988 is a leap year.
   
## Loan and payment calculator

#### Description

The interest due on a loan can be calculated according to the simple formula:

I = P × R × T

where I is the interest paid, P is the amount borrowed (principal), R is the interest rate, and T is the length of the loan.

It is common for loans to be amortized which allows the lendor to collect their interest early in the loan period. We will ignore amortization for the purpose of this program. For bonus points, figure out how to do amortization and print an amortization schedule with the payment schedule. There is an excellent explanation of the amortization formula at Interest.com.

Write a program that calculates the interest due on a loan and prints a payment schedule. Make sure you round the output to two decimal places. For bonus points, figure out how to calculate amortization and print an amortization schedule. It will be your responsibility to find an appropriate format for the amortization printout.

Make sure you handle the dollars correctly! Floating point numbers in Python (and other programming languages) are subject to rouding errors when doing floating point arithmetic. For an explanation of this phenomenon, see the floating point arithmetic section of the Python tutorial. One of the most common strategies to solve the problem is to do all money-related calculations in pennies, converting back to dollars when the results are displayed. If you don't handle this issue correctly, your program won't give correct answers in all cases.

#### Input

The program will prompt the user for the amount borrowed, interest rate as a percentage (in annual interest terms), and the term of the loan in years.

#### Output

The program will print the amount borrowed, total interest paid, the amount of the monthly payment, and a payment schedule.

#### Sample session

    Loan calculator

    Amount borrowed: 100
    Interest rate: 6
    Term (years): 1

    Amount borrowed:    $100.00
    Total interest paid:  $6.00

               Amount     Remaining
    Pymt#       Paid       Balance
    -----      -------    ---------
      0        $ 0.00      $106.00
      1        $ 8.84      $ 97.16
      2        $ 8.84      $ 88.32
      3        $ 8.84      $ 79.48
      4        $ 8.84      $ 70.64
      5        $ 8.84      $ 61.80
      6        $ 8.84      $ 52.96
      7        $ 8.84      $ 44.12
      8        $ 8.84      $ 35.28
      9        $ 8.84      $ 26.44
     10        $ 8.84      $ 17.60
     11        $ 8.84      $  8.76
     12        $ 8.76      $  0.00

