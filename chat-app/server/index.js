const app = require('express')()
const http = require('http').createServer(app)
const io = require('socket.io')(http)

io.on('connection', socket => { // on connection (when the connection is on)
    socket.on('message', ({ name, message }) => { // on message (if the connected client sends a message)
        io.emit('message', {name, message}) // emit message (emit/display the message along with the client's name)
    })
})

http.listen(4000, function() {
    console.log('Listening on port 4000')
})