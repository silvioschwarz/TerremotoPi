const path = require('path')
const {spawn} = require('child_process')

/**
 * Run python script, pass in `-u` to not buffer console output 
 * @return {ChildProcess}
 */
function runScript(){
  return spawn('python3', [
    "-u", 
    path.join(__dirname, 'NXP.py'),
    "--foo", "some value for foo",
  ]);
}

const subprocess = runScript()

// print output of script
subprocess.stdout.on('data', (data) => {
  console.log(`data:${data}`);
});
subprocess.stderr.on('data', (data) => {
  console.log(`error:${data}`);
});
subprocess.stderr.on('close', () => {
  console.log("Closed");
});
