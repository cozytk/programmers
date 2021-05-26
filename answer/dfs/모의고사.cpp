#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    int i = -1;
    int cnt1 = 0;
    int cnt2 = 0;
    int cnt3 = 0;
    int max = 0;
    while (answers[++i])
    {
        if (answers[i] == (i % 5 + 1))
            cnt1++;
        if (i % 2 == 0 && answers[i] == 2)
            cnt2++;
        else if (i % 8 == 1 && answers[i]== 1)
            cnt2++;
        else if (i % 8 == 3 && answers[i]== 3)
            cnt2++;
        else if (i % 8 == 5 && answers[i]== 4)
            cnt2++;
        else if (i % 8 == 7 && answers[i]== 5)
            cnt2++;
        if ((i % 10 == 0 || i % 10 == 1) && answers[i] == 3)
            cnt3++;
        else if ((i % 10 == 2 || i % 10 == 3) && answers[i] == 1)
            cnt3++;
        else if ((i % 10 == 4 || i % 10 == 5) && answers[i] == 2)
            cnt3++;
        else if ((i % 10 == 6 || i % 10 == 7) && answers[i] == 4)
            cnt3++;
        else if ((i % 10 == 8 || i % 10 == 9) && answers[i] == 5)
            cnt3++;
    }
    if (cnt1 <= cnt2)
        max = cnt2;
    else
        max = cnt1;
    if (max <= cnt3)
        max = cnt3;
    if (cnt1 == max)
        answer.push_back(1);
    if (cnt2 == max)
        answer.push_back(2);
    if (cnt3 == max)
        answer.push_back(3);
    std::cout << cnt1 << " " << cnt2 << " " << cnt3 << std::endl;
    return answer;
}

/* To improve,
   make every condition in loop -> make 3 vector to save answers.
   compare using condition -> use max_element() method in vector container.
   use each int cnt variable -> use vector cnt
   */
