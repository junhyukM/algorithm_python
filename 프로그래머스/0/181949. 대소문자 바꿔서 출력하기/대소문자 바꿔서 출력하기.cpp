#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string str;
    cin >> str;
    for(int i = 0; i <= str.length(); i++) {
        if(isupper(str[i])) {
            str[i] = tolower(str[i]);
        }
        else {
            str[i] = toupper(str[i]);
        }
    }
    cout << str << endl;
    return 0;
}