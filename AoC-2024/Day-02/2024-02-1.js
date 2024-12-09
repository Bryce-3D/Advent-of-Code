const fs = require('fs')
txt = fs.readFileSync('Input.txt', 'utf8')

lines = txt.split('\n')

ans = 0
for (Homu = 0; Homu < lines.length; Homu++) {
    line = lines[Homu]
    a = line.split(' ')
    diffs = []
    for (i = 0; i < a.length-1; i++) {
        diffs[i] = a[i+1]-a[i]
    }
    m = Math.min(...diffs)
    M = Math.max(...diffs)
    if (-3 <= m && M <= -1) {
        ans += 1
    }
    if (1 <= m && M <= 3) {
        ans += 1
    }
}
console.log(ans)
