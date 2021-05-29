#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool len_compare(string a, string b) {
	return (a.length() <= b.length());
}

bool solution(vector<string> phone_book) {
	sort(phone_book.begin(), phone_book.end(), len_compare);
	for (int i = 0; i < phone_book.size() - 1; i++) {
		for (int j = i + 1; j < phone_book.size(); j++) {
			int k = 0;
			while (k < phone_book[i].size() && phone_book[i][k] == phone_book[j][k]) {
				k++;
			}
			if (k == phone_book[i].size())
				return false;
		}
	}
	return true;
}

/*
 * abort, segmentation fault.
 * same result with phone_book[i].size() -> phone_book[i].length()
 */