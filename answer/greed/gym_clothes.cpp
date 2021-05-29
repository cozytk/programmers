/*
 * I suppose vectors are 'arranged' that's why I spend a lot of time to solve it.
 */

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
	int answer = 0;
	int i = 0;
	int j = 0;
	sort(lost.begin(), lost.end());
	sort(reserve.begin(), reserve.end());
	while (i < lost.size() && j < reserve.size())
	{
		if (lost[i] == reserve[j])
		{
			lost.erase(lost.begin() + i);
			reserve.erase(reserve.begin() + j);
		}
		else if (lost[i] > reserve[j])
			j++;
		else
			i++;
	}
	i = 0;
	j = 0;
	while (i < lost.size() && j < reserve.size())
	{
		if (lost[i] - 1 > reserve[j])
			j++;
		else if (lost[i] - 1 == reserve[j] || \
                 lost[i] + 1 == reserve[j])
		{
			lost.erase(lost.begin() + i);
			reserve.erase(reserve.begin() + j);
		}
		else
			i++;
	}
	answer = n - int(lost.size());
	return answer;
}

/* main example
int main()
{
	vector<int> lost;
	lost.push_back(1);
	lost.push_back(3);
	lost.push_back(5);
	vector<int> reserve;
	reserve.push_back(2);
	reserve.push_back(3);
	reserve.push_back(4);
	return(printf("%d\n", solution(5, lost, reserve)));
}*/
