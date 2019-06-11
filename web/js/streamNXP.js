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
  res.send(`</head>
    <body>
    <div class="navbar"><span>Real-Time Chart with Plotly.js</span></div>
    <div class="wrapper">
        <div id="chart"></div>
        <script>
        //function getData() {
        //        return Math.random();
        //    } 

            Plotly.plot('chart',[{
                y:[getData()],
                type:'line'
            }]);
            
            var cnt = 0;
            setInterval(function(){
                Plotly.extendTraces('chart',{ y:[[getData()]]}, [0]);
                cnt++;
                if(cnt > 500) {
                    Plotly.relayout('chart',{
                        xaxis: {
                            range: [cnt-500,cnt]
                        }
                    });
                }
            },15);
        </script>
    </div>
    </body>`)
})

function getData() {
  return spawn('python3', [
    "-u",
    path.join(__dirname, 'NXPGetData.py'),
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
