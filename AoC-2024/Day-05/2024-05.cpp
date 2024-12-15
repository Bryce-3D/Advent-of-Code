#include <bits/stdc++.h>
using namespace std;

template <typename T>
using v = vector<T>;
template <typename X, typename Y>
using p = pair<X,Y>;
using str = string;

#define pb push_back

str read_file(str fn) {
    ifstream file(fn);
    stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

v<string> split(const str& s_, const str& delimiter) {
    /* 
    Splits a string along a delimiter.
    Removes empty strings from the split.
    */
    str s = s_;
    v<str> ans;
    size_t pos = 0;
    str next;
    while (pos != string::npos) {
        pos = s.find(delimiter);
        next = s.substr(0,pos);
        if (next != "") {
            ans.pb(next);
        }
        s.erase(0, pos+delimiter.length());
    }
    return ans;
}

int main() {
    str txt = read_file("Sample.txt");
    str rules_txt = split(txt, "\n\n")[0];
    str order_txt = split(txt, "\n\n")[1];

    v<str> rule_lines = split(rules_txt, "\n");

    v<p<int,int>> rules = 
}