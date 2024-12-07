// https://www.mitchellmudd.dev/blog/read-text-file-nodejs
// https://www.w3schools.com/js/js_string_methods.asp
// https://www.w3schools.com/jsref/jsref_split.asp

const fs = require('fs')
txt = fs.readFileSync('Input.txt', 'utf8')

l_0 = []
l_1 = []

lines = txt.split('\n')
for (i = 0; i < lines.length; i++) {
    a = lines[i].split(' ')   // Get the ith line, then split on spaces
    l_0[i] = Number(a[0])
    l_1[i] = Number(a[a.length-1])
}

l_0.sort()
l_1.sort()

ans = 0
for (i = 0; i < l_0.length; i++) {
    ans += Math.abs(l_0[i]-l_1[i])
}
console.log(ans)



// Recycling Bin ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

// fs.readFile('Sample.txt', 'utf8', (err, data) => {
//     if (err) {
//       console.error(err);
//       return;
//     }
//     console.log(data);
// });

// fetch('Sample.txt').then(r=>r.text()).then(t=>console.log(t));
