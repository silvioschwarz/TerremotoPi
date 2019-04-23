const path = require('path')
const {spawn} = require('child_process')
const express = require('express')
const app = express()
const http = require("http")
const WebSocket = require("ws")
const server = http.createServer(app);
const wss = new WebSocket.Server({server});

function runScript() {
  return spawn('python3', [
    "-u",
    path.join(__dirname, 'NXP.py'),
  ]);
}

app.get('/', function (req, res) {
  res.send(`<!doctype html>
<html lang="en">
<body>
<button type="button" onclick="runWebsocket()">Run with websocket</button>
<pre id="outputWebsocket"></pre>

<script>
  var outputWebsocket = document.getElementById("outputWebsocket")
  function runWebsocket() {
    outputWebsocket.innerText = ""
    openConnection(function (connection) {
      connection.send("run")
    })
  }
  function appendWSText(text) {
    outputWebsocket.innerText += text
  }
  var conn = {}
  function openConnection(cb) {
    // uses global 'conn' object
    if (conn.readyState === undefined || conn.readyState > 1) {
      conn = new WebSocket('ws://' + window.location.host + '/');
      conn.onopen = function () {
        appendWSText("\\nSocket open")
        if(typeof cb === "function"){
          cb(conn)
        }
      };
      conn.onmessage = function (event) {
        appendWSText(event.data)
      };
      conn.onclose = function (event) {
        appendWSText("\\nSocket closed")
      };
    } else if(typeof cb === "function"){
      cb(conn)
    }
  }
  if (window.WebSocket === undefined) {
    appendWSText("\\nSockets not supported")
  } else {
    openConnection();
  }
</script>
</body>
</html>`)
})

function getData() {
  return spawn('python3', [
    "-u",
    path.join(__dirname, 'NXP.py'),
  ]);
}


function runScriptInWebsocket(id, ws) {
  const child = runScript("foobar")
  child.stdout.on('data', (data) => {
    ws.send(`${id}:${data}`);
  });
  child.stderr.on('data', (data) => {
    ws.send(`${id}:error:\n${data}`);
  });
  child.stderr.on('close', () => {
    ws.send(`${id}:done`);
  });
}

let id = 1
wss.on('connection', (ws) => {
  const thisId = id++;
  ws.on('message', (message) => {
    ws.send(`You sent -> ${message}`);
    if ("run" === message) {
      runScriptInWebsocket(thisId, ws)
    }
  });
  ws.send('Connection with WebSocket server initialized');
});

server.listen(8080, () => console.log('Server running'))
