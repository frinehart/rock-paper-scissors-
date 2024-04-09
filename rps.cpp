/*

Author: Francis Rinehart
Date: 01/29/2024

*/

#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    srand(time(NULL)); // random number
    int user = 0;
    int cpu = 0;

    cout<<"Rock Paper Scissors Shoot Game!\n\n" <<endl;

    // user selection option
    cout<<"Select the following: \n\n" <<endl;
    cout<<"1. Rock" <<endl;
    cout<<"2. Paper" <<endl;
    cout<<"3. Scissors\n\n" <<endl;
    cin>>user; // select number

    // conditional statement
    if(user == 1)
    {
        cout << "You choose Rock" << endl;
    }
    else if(user == 2)
    {
        cout << "You choose Paper" << endl;
    }
    else if(user == 3)
    {
        cout << "You choose Scissors" << endl;
    }
    else
    {
        cout << "You did not choose any of the options" << endl;
    }

    cpu = rand()%3+1;

    if(cpu == 1)
    {
        cout << "CPU choose Rock" << endl;
    }
    else if(cpu == 2)
    {
        cout << "CPU choose Paper" << endl;
    }
    else
    {
        cout << "CPU choose Scissors" << endl;
    }

    // user and cpu match
    if(user==cpu)
    {
        cout << "Tie!" << endl;
    }

    // If the user selects rock
    else if(user==1)
    {
        if(cpu==2)
        {
            cout<< "You lose" << endl;
        }
        if(cpu==3)
        {
            cout<< "You win" << endl;
        }

       // user selects paper
       else if(user==2)
       {
           if(cpu==1)
           {
               cout<<"You Win"<< endl;
           }
           if(cpu==3)
           {
               cout<<"You lose"<< endl;
           }
       }

    }
    // user selects scissors

    else if(user==3)
    {
        if(cpu==1)
        {
            cout<<"You Lose"<<endl;
        }
        if(cpu==2)
        {
            cout<<"You win"<<endl;
        }
    }

    // 0:10:55


    return 0;
}
