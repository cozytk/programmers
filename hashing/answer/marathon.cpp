#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    map<string, int> dict;
    
    for (int i = 0; i < completion.size(); i++)
        dict[completion[i]]++;
    for (int i = 0; i < participant.size(); i++)
    {
        if (!dict[participant[i]])
        {
            answer = participant[i];
            break;
        }
        else
            dict[participant[i]]--;
    }
    
    /*
    int found = 0;
    for (int i = 0; i < participant.size(); i++)
    {
        found = 0;
        for (int j = 0; j < completion.size(); j++)
        {
            if (completion[j] == participant[i])
            {
                completion.erase(completion.begin() + j);
                found = 1;
                break ;
            }
        }
        if (!found)
        {
            answer = participant[i];
            break ;
        }
    }
    */
    return answer;
}

/* commented code -> time out
   */
