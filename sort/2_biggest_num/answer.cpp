/*
 * cmp func paramater to reference, no need to declare temp1, temp2.
 * remember the exception the 0s.
 */

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(string a, string b)
{
    string temp1 = a + b;
    string temp2 = b + a;

    return temp1 > temp2;
}

string solution(vector<int> numbers) {
    vector<string> temp;
    string answer = "";
    for (auto n : numbers)
        temp.push_back(to_string(n));
    sort(temp.begin(), temp.end(), cmp);
    if (temp[0] == "0")
        return "0";
    for (auto t : temp)
        answer += t;
    return answer;
}
