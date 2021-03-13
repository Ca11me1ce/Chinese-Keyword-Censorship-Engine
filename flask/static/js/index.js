var socket = io.connect('http://' + document.domain + ':' + location.port, { 'reconnect': true });
window.onload = function(){
    addLogs("==> The model is standby!")
    socket.on('connect', function(){
        console.log("start connecting")
        
    });
}