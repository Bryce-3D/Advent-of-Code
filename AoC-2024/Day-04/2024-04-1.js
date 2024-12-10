const fs = require('fs')
let txt = fs.readFileSync('Input.txt', 'utf8')

let M = txt.split('\n')
let R = M.length
let C = M[0].length

let dirs = [
    [-1, 0],   // N
    [-1,-1],   // NW
    [ 0,-1],   // W
    [ 1,-1],   // SW
    [ 1, 0],   // S
    [ 1, 1],   // SE
    [ 0, 1],   // E
    [-1, 1],   // NE
]

let ans = 0
for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
        for (let dir of dirs) {
            // Get the coordinates along the given direction
            let r1 = r + 1*dir[0]
            let r2 = r + 2*dir[0]
            let r3 = r + 3*dir[0]
            let c1 = c + 1*dir[1]
            let c2 = c + 2*dir[1]
            let c3 = c + 3*dir[1]

            // Check if the word lies within the grid
            if (Math.min(r,r3) < 0 || Math.max(r,r3) >= R) {
                continue
            }
            if (Math.min(c,c3) < 0 || Math.max(c,c3) >= C) {
                continue
            }

            // Check if the word spells out XMAS
            let word = M[r][c] + M[r1][c1] + M[r2][c2] + M[r3][c3]
            if (word == 'XMAS') {
                ans += 1
            }
        }
    }
}

console.log(ans)

