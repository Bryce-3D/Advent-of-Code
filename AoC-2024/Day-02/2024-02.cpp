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

v<int> line_to_nums(str line) {
    v<str> nums_str = split(line, " ");
    v<int> ans;
    for (str s : nums_str) {
        ans.pb(stoi(s));
    }
    return ans;
}

bool works_1(v<int> nums) {
    // Get the differences
    v<int> diffs;
    for (int i = 0; i < nums.size()-1; i++) {
        diffs.pb(nums[i+1]-nums[i]);
    }
    // Get the min and max of the differences
    int m = *min_element(diffs.begin(), diffs.end());
    int M = *max_element(diffs.begin(), diffs.end());
    // Check if it works or not
    if (-3 <= m && M <= -1) {
        return true;
    }
    if (1 <= m && M <= 3) {
        return true;
    }
    return false;
}

bool works_2(v<int> nums) {
    if (works_1(nums)) {
        return true;
    }

    v<int> num_rem;
    // Remove the ith element
    for (int i = 0; i < nums.size(); i++) {
        num_rem = v<int>();
        for (int j = 0; j < nums.size(); j++) {
            if (j != i) {
                num_rem.pb(nums[j]);
            }
        }
        if (works_1(num_rem)) {
            return true;
        }
    }

    return false;
}

int main() {
    string txt = read_file("Input.txt");
    v<str> lines = split(txt, "\n");

    v<int> nums;
    v<v<int>> num_lines;
    for (str line : lines) {
        nums = line_to_nums(line);
        num_lines.pb(nums);
    }

    int ans_1 = 0;
    for (v<int> nums : num_lines) {
        if (works_1(nums)) {
            ans_1 += 1;
        }
    }
    cout << ans_1 << endl;

    int ans_2 = 0;
    for (v<int> nums : num_lines) {
        if (works_2(nums)) {
            ans_2 += 1;
        }
    }
    cout << ans_2 << endl;
}
