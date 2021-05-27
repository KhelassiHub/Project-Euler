// #include <iostream>
// #include <utility>
// #include <set>
// #include <iterator>
#include <bits/stdc++.h>
// #include <vector>
// #include <sstream>
// #include <algorithm>
// #include <string>
// #include <cstring>

using namespace std;


int main()
{
    /* code */
    double i,j,ii,jj,num,denum;
    double fraction,firstFrac,secondFrac,thirdFrac,fourthFrac;
    set<pair<int, int>> s1;
    for (i = 1; i < 10; i++)
    {
        for (j = 1; j < 10; j++)
        { 
            for (ii = 1; ii < 10; ii++)
            {
                for (jj = 1; jj < 10; jj++)
                {
                    num = 10 * i + j;
                    denum = 10 * ii + jj;
                    fraction = num / denum;
                    firstFrac = j / jj;
                    secondFrac = j / ii;
                    thirdFrac = i / jj;
                    fourthFrac = i / ii;
                    if (i!=j && ii!=jj)
                    {
                    if (fraction==firstFrac && jj > j && i==ii)
                    {
                        s1.insert(make_pair(j, jj));
                        cout << fraction << " and " << firstFrac << " -- " << j << "/" << jj << " -- " << num << "/" << denum << endl;
                    }
                    else if (fraction==secondFrac && ii > j && i==jj)
                    {
                        s1.insert(make_pair(j,ii));
                        cout << fraction << " and " << secondFrac << " -- " << j << "/" << ii << " -- " << num << "/" << denum << endl;
                    }
                    else if (fraction==thirdFrac && jj > i && j==ii)
                    {
                        s1.insert(make_pair(i,jj));
                        cout << fraction << " and " << thirdFrac << " -- " << i << "/" << jj << " -- " << num << "/" << denum << endl;
                    }
                    else if (fraction==fourthFrac && ii > i && j==jj)
                    {
                        s1.insert(make_pair(i,ii));
                        cout << fraction << " and " << fourthFrac << " -- " << i << "/" << ii << " -- " << num << "/" << denum << endl;
                    }
                    }
                }   
            }   
        }
    }
    // to display the pairs
    for (auto const &var : s1)
    {
        cout << "(" << var.first << ", " << var.second << ") ";
    }
    cout << endl;
    return 0;
    }
