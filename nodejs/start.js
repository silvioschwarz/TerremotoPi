//start.js
var spawn = require('child_process').spawn,
    py    = spawn('python3', ['NXP.py']),
    data = [1,2,3,4,5,6,7,8,9],
    dataString = '';

py.stdout.on('data', function(data){
  dataString += data.toString();
});
py.stdout.on('end', function(){
  console.log('NXP DATA\n',dataString);
});
py.stdin.write(JSON.stringify(data));
py.stdin.end();
