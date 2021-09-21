// C++ version for illustration
#include <iostream>

using namespace std;

int main()
{
    // Set the variables
    int age;
    string name;

    cout << "What is your name?" << endl;
    cin >> name;

    cout << "How old are you?" << endl;
    cin >> age;

    if(age < 18)
    {
        cout << "You may not order beer" << endl;
    }
    else
    {
        cout << "Order anything you like" << endl;
    }

    return 0;
}