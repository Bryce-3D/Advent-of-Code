#include <bits/stdc++.h>
using namespace std;

template <typename T>
using v = vector<T>;
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
    str txt = read_file("Input.txt");
    v<str> lines = split(txt,"\n");

    map<int,int> count_l;
    map<int,int> count_r;
    for (str line : lines) {
        v<str> split_line = split(line, " ");
        int l = stoi(split_line[0]);
        int r = stoi(split_line[1]);
        if (count_l.count(l)) {
            count_l[l] += 1;
        } else {
            count_l[l] = 1;
        }
        if (count_r.count(r)) {
            count_r[r] += 1;
        } else {
            count_r[r] = 1;
        }
    }

    int ans = 0;
    for (const auto &[n,count] : count_l) {
        if (count_r.count(n)) {
            ans += n*count*count_r[n];
        }
    }
    cout << ans << endl;
}
