const express = require('express')
const app = express()

// <...>

app.get('/run', function (req, res) {
  const subprocess = runScript()
  res.set('Content-Type', 'text/plain');
  subprocess.stdout.pipe(res)
  subprocess.stderr.pipe(res)
})

app.listen(8080, () => console.log('Server running'))
