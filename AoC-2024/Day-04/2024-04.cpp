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

int count_1(v<str> M, int r, int c) {
    /* Number of "XMAS" in M starting from M[r][c] */
    v<v<int>> dirs = {
        {-1, 0},   // N
        {-1,-1},   // NE
        { 0,-1},   // E
        { 1,-1},   // SE
        { 1, 0},   // S
        { 1, 1},   // SW
        { 0, 1},   // W
        {-1, 1},   // NW
    };

    int R = M.size();
    int C = M[0].size();

    int ans = 0;
    for (v<int> dir : dirs) {
        // Coordinates of the word along the direction
        v<int> v_r = {r, r+dir[0], r+2*dir[0], r+3*dir[0]};
        v<int> v_c = {c, c+dir[1], c+2*dir[1], c+3*dir[1]};
        // Check if the word is inside the grid
        if (v_r[0] < 0 || v_r[0] >= R) {
            continue;
        }
        if (v_r[3] < 0 || v_r[3] >= R) {
            continue;
        }
        if (v_c[0] < 0 || v_c[0] >= C) {
            continue;
        }
        if (v_c[3] < 0 || v_c[3] >= C) {
            continue;
        }
        // Check if the word spells "XMAS"
        str w = "";
        for (int i = 0; i < v_r.size(); i++) {
            w += M[v_r[i]][v_c[i]];
        }
        if (w == "XMAS") {
            ans += 1;
        }
    }

    return ans;
}

int count_2(v<str> M, int r, int c) {
    if (r <= 0 || r >= M.size()-1) {
        return 0;
    }
    if (c <= 0 || c >= M[0].size()-1) {
        return 0;
    }
    if (M[r][c] != 'A') {
        return 0;
    }
    str w0{M[r-1][c-1],M[r+1][c+1]};
    str w1{M[r-1][c+1],M[r+1][c-1]};
    if (w0 != "MS" && w0 != "SM") {
        return 0;
    }
    if (w1 != "MS" && w1 != "SM") {
        return 0;
    }
    return 1;
}

int main() {
    str txt = read_file("Input.txt");
    v<str> M = split(txt, "\n");
    int R = M.size();
    int C = M[0].size();

    int ans_1 = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            ans_1 += count_1(M,r,c);
        }
    }
    cout << ans_1 << endl;

    int ans_2 = 0;
    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            ans_2 += count_2(M,r,c);
        }
    }
    cout << ans_2 << endl;
}
