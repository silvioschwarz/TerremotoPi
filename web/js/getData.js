//start.js

function getData() {
  return spawn('python3', [
    "-u",
    path.join(__dirname, 'NXPGetData.py'),
  ]);
}


//function runScript(){
//  return spawn('python3', [
//    "-u", 
//    path.join(__dirname, 'NXP.py'),
//    "--foo", "some value for foo",
//  ]);
//}
