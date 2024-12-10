#include <bits/stdc++.h>
using namespace std;

#define vec vector
#define str string
#define pb push_back

vec<string> split(const str& s_, const str& delimiter) {
    /* 
    Splits a string along a delimiter.
    Removes empty strings from the split.
    */
    str s = s_;
    vec<str> ans;
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
    ifstream file("Input.txt");

    vec<int> v_l;
    vec<int> v_r;

    string line;
    vec<str> split_line;
    while (getline(file, line)) {
        split_line = split(line, " ");
        v_l.pb(stoi(split_line[0]));
        v_r.pb(stoi(split_line[1]));
    }

    sort(v_l.begin(), v_l.end());
    sort(v_r.begin(), v_r.end());

    int ans = 0;
    for (int i = 0; i < v_l.size(); i++) {
        ans += abs(v_l[i]-v_r[i]);
    }
    cout << ans << endl;

    file.close();
}
