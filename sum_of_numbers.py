#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Sept 2019
# Modified by: Jonathan
# Modified on: May 20, 2021
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.

def main():
    # initialize the loop counter and sum
    loop_counter = 0
    sum = 0

    # get the user number as a string
    user_number_string = input("Enter a positive number: ")
    print("")
    try:
        user_number_int = int(user_number_string)
        print("")
    except ValueError:
        print("Please enter a valid number")

    else:
        # calculate the sum of all numbers from 0 to user number
        while (loop_counter <= user_number_int):
            sum = sum + loop_counter
            print("Tracking {0} times through loop.".format(loop_counter))
            loop_counter = loop_counter + 1
            print("The sum of the numbers from"
                  "0 to {} is: {}.".format(user_number_int, sum))
            print("")
        if (user_number_int < 0):
            print("{0} is not a valid number".format(user_number_int))
    finally:
        print("")
        print("Thank you for your input")


if __name__ == "__main__":
    main()
