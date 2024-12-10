// USE `let` OR DIE TO RANDOM GLOBAL VARIABLES
// https://javascript.plainenglish.io/beware-of-unsafe-implicit-globals-in-javascript-f370ccca8fdb
// https://stackoverflow.com/questions/29656267/remove-elements-from-javascript-array-by-position

const fs = require('fs')
txt = fs.readFileSync('Sample.txt', 'utf8')
lines = txt.split('\n')

function works_1(line) {
    diffs = []
    for (let i = 0; i < line.length-1; i++) {
        diffs[i] = line[i+1]-line[i]
    }
    m = Math.min(...diffs)
    M = Math.max(...diffs)
    if (-3 <= m && M <= -1) {
        return true
    }
    if (1 <= m && M <= 3) {
        return true
    }
    return false
}

function works_2(line) {
    if (works_1(line)) {
        return true
    }
    for (let i = 0; i < line.length; i++) {
        //Copy the line except for the ith number

        // let _line = []
        // for (let j = 0; j < line.length-1; j++) {
        //     if (j < i) {
        //         _line[j] = line[j]
        //     } else if (j >= i) {
        //         _line[j] = line[j+1]
        //     }
        // }

        _line = [...line]
        _line.splice(i,1)

        if (works_1(_line)) {
            return true
        }
    }
    return false
}



ans = 0
for (line of lines) {
    line = line.split(' ')
    if (works_2(line)) {
        ans += 1
    }
}
console.log(ans)
