#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

bool solution(vector<string> phone_book) {
	bool answer = true;

	unordered_map<string, int> hash_map;
	for(int i = 0; i < phone_book.size(); i++)
		hash_map[phone_book[i]] = 1;

	for(int i = 0; i < phone_book.size(); i++) {
		string phone_number = "";
		for(int j = 0; j < phone_book[i].size(); j++) {
			phone_number += phone_book[i][j];
			cout << phone_number << endl;
			if(hash_map[phone_number] && phone_number != phone_book[i])
				answer = false;
		}
	}

	return answer;
}

int main()
{
	vector<string> phone_book;
	phone_book.push_back("124");
	phone_book.push_back("324234124");
	phone_book.push_back("134534");
	phone_book.push_back("1234");
	phone_book.push_back("12345345344");
	phone_book.push_back("12456356");
	solution(phone_book);
}
