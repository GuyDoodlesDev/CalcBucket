const fs = require('fs');
const homedir = require('os').homedir();
const prgmdir = homedir+'/.CalcBucket';
const tmpdir = prgmdir+'/tmp';
const indexcache = tmpdir+'/master.index'

var index = fs.readFileSync(indexcache).toString();
index = index.split(/^Index of/g).map(s => s.split('\n'));
console.log(index);