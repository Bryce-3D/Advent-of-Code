const fs = require('fs')
let txt = fs.readFileSync('Input.txt', 'utf8')

let M = txt.split('\n')
let R = M.length
let C = M[0].length

let ans = 0
for (let r = 1; r < R-1; r++) {
    for (let c = 1; c < C-1; c++) {
        if (M[r][c] != 'A') {
            continue
        }
        let diag0 = M[r-1][c-1]+M[r+1][c+1]
        let diag1 = M[r-1][c+1]+M[r+1][c-1]
        if (diag0 != 'MS' && diag0 != 'SM') {
            continue
        }
        if (diag1 != 'MS' && diag1 != 'SM') {
            continue
        }
        ans += 1
    }
}

console.log(ans)
