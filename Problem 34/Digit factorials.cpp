#include <iostream>
#include <string>

/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: As 1! = 1 and 2! = 2 are not sums they are not included.
*/

using namespace std;

int main()
{
    unsigned int sum = 0, sum_i=0;
    unsigned int i, i_length, factorial;

    for (int i = 3; i < 10000000; i++) //Why 10000000 ? beacause after 8 digits the max sum of 
    // the factorial of digits (which is 99999999) is 2903040 which is written in 7 digits, this means that after 8 digits
    // the factorial sum of digits will never reach the number itself
    {
        string string_i = to_string(i);     //Convert the integer into a string
        i_length = string_i.size();         //Calculating the number of digits in the integer
        sum_i=0;
        for (int j = 0; j < i_length; j++)
        {
            factorial=1;
            for (int z = 1; z <= int(string_i[j]) - 48; ++z) //Calculating the factorial of each digit, -48 for the digit ASCII conversion
                {
                    factorial *= z;
                }
            sum_i+=factorial;   //Summing the factorial of each digit
        }
        if (i == sum_i)     
        {
            sum+=i;
        }
    }
    // Result
    cout << sum << endl;

    return 0;
}