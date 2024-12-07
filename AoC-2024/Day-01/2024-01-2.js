const fs = require('fs')
txt = fs.readFileSync('Input.txt', 'utf8')

// Counts of each number in the left and right lists
d_l = {}
d_r = {}

lines = txt.split('\n')

for (i = 0; i < lines.length; i++) {
    line = lines[i]
    a = line.split(' ')
    l = Number(a[0])
    r = Number(a[a.length-1])

    if (l in d_l) {
        d_l[l] += 1
    } else {
        d_l[l] = 1
    }

    if (r in d_r) {
        d_r[r] += 1
    } else {
        d_r[r] = 1
    }
}

ans = 0
for (n in d_l) {
    if (!(n in d_r)) {
        continue
    }
    ans += n*d_l[n]*d_r[n]
}

console.log(ans)
