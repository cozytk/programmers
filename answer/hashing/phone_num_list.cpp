#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book) {
	int j;
	sort(phone_book.begin(), phone_book.end());
	for (int i = 0; i < phone_book.size() - 1; i++) {
		j = 0;
		if (phone_book[i].length() >= phone_book[i + 1].length())
			continue ;
		while (j < phone_book[i].length() && phone_book[i][j] == phone_book[i + 1][j])
			j++;
		if (j == phone_book[i].length())
			return false;
	}
	return true;
}

int main()
{
	vector<string> phone_book;
	phone_book.push_back("1157574");
	phone_book.push_back("124");
	phone_book.push_back("103");
	phone_book.push_back("104678998");
	phone_book.push_back("13445");
	if (solution(phone_book))
		printf("True\n");
	return(0);
}