const gameObj = {
    playerOnePoints: 0,
    playerTwoPoints: 0,
    turn: 1,
    fields: [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
]
}

function gameIsFinished() {
    console.log("called")
    if (gameObj.turn == 1) {
        gameObj.playerOnePoints += 1
    } else {
        gameObj.playerTwoPoints += 1
    }
    setTimeout(function() {
        gameObj.fields = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
    ]
    renderPlayerfield()
    }, 500)
    renderScore()
}

function renderPlayerfield() {
    const playfieldTiles = document.querySelectorAll(".playfield div")
    for(let i = 0;i < gameObj.fields.length ;i++) {
        const row = gameObj.fields[i]

        for(let j = 0;j<row.length;j++) {
            const tiles = row[j]
            const tileID = (i*3 + j)
            const playfieldTile = playfieldTiles[tileID] 
            if(tiles === "X") {
                playfieldTile.innerHTML = `<svg version="1.0" xmlns="http://www.w3.org/2000/svg"
                width="100%" height="100%" viewBox="0 0 1280.000000 1280.000000"
                preserveAspectRatio="xMidYMid meet">
               <metadata>
               Created by potrace 1.15, written by Peter Selinger 2001-2017
               </metadata>
               <g transform="translate(0.000000,1280.000000) scale(0.100000,-0.100000)"
               fill="#000000" stroke="none">
               <path d="M3137 9659 l-537 -539 1360 -1360 1360 -1360 -1360 -1360 -1360
               -1360 540 -540 540 -540 1360 1360 1360 1360 1360 -1360 1360 -1360 540 540
               540 540 -1360 1360 -1360 1360 1360 1360 1360 1360 -540 540 -540 540 -1360
               -1360 -1360 -1360 -1360 1360 c-748 748 -1361 1360 -1362 1359 -2 0 -245 -243
               -541 -540z"/>
               </g>
               </svg>
               `
            } else if(tiles === "O") {
                playfieldTile.innerHTML = `
                <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="85%" width="85%" x="0px" y="0px" viewBox="0 0 1000 1000" enable-background="new 0 0 1000 1000" xml:space="preserve">
                <metadata> Svg Vector Icons : http://www.onlinewebfonts.com/icon </metadata>
                <g><path d="M500,10C229.4,10,10,229.4,10,500c0,270.6,219.4,490,490,490c270.6,0,490-219.4,490-490C990,229.4,770.6,10,500,10z M815,815c-40.9,40.9-88.6,73.1-141.6,95.5c-54.9,23.2-113.2,35-173.4,35c-60.2,0-118.5-11.8-173.4-35C273.6,888,225.9,855.9,185,815s-73-88.6-95.5-141.6c-23.2-54.9-35-113.2-35-173.4c0-60.2,11.8-118.5,35-173.4c22.4-53,54.6-100.7,95.5-141.6s88.6-73,141.6-95.5c54.9-23.2,113.2-35,173.4-35c60.2,0,118.5,11.8,173.4,35c53,22.4,100.7,54.6,141.6,95.5c40.9,40.9,73,88.6,95.5,141.6c23.2,54.9,35,113.2,35,173.4c0,60.2-11.8,118.5-35,173.4C888,726.4,855.9,774.1,815,815z"/></g>
                </svg>`
            } else if(tiles === "-") {
                playfieldTile.innerHTML = ""
            }
        }
    }
}

function checkFinishGame() {
    const fields = gameObj.fields
    for(let i=0; i<gameObj.fields.length; i++) {
        const rows = gameObj.fields[i];
        if (rows[0] !== "-" && rows[0] === rows[1] && rows[2] === rows[1]) {
            gameIsFinished();
        }
    }

    for(let j=0; j<gameObj.fields.length; j++) {
        const column = []
        for(let i=0; i<gameObj.fields.length; i++) {
            column.push(gameObj.fields[i][j])

        }
        if (column[0] !== "-" && column[0] === column[1] && column[2] === column[1]) {
            gameIsFinished();
        }
    }

    if(fields[0][2] !== "-" && fields[0][2] === fields[1][1] && fields[2][0] === fields[1][1]) {
        gameIsFinished();
    }
    
    if(fields[0][0] !== "-" && fields[0][0] === fields[1][1] && fields[2][2] === fields[1][1]) {
        gameIsFinished();
    }

    let minusFound = false;
    for(let i=0; i<gameObj.fields.length; i++) {
        const rows = fields[i]
    
        for(let j=0; j<rows.length; j++) {
            const tile = rows[j]
            if (tile === "-") {
                minusFound = true;
            }
        }
    }

    if(!minusFound) {
        setTimeout(function() {
            gameObj.fields = [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]
        ]
        renderPlayerfield()
        }, 500)
    }
}

function renderScore() {
    document.querySelector("#playerOnePoints").textContent = gameObj.playerOnePoints
    document.querySelector("#playerTwoPoints").textContent = gameObj.playerTwoPoints
}

function onFieldClick(e) {
    const clickedID = Number(e.target.id)
    const rowID = Math.trunc((clickedID-1)/3)
    const columnID = Math.trunc((clickedID - 1) % 3)
    if(gameObj.fields[rowID][columnID] !== "-") {
        return;
    }

    if (gameObj.turn === 1) {
        gameObj.fields[rowID][columnID] = "X"
    } else {
        gameObj.fields[rowID][columnID] = "O"
    }
    renderPlayerfield()
    checkFinishGame()
    gameObj.turn = gameObj.turn === 1 ? 2 : 1
}

function onResetButtonClick() {
    gameObj.fields = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    gameObj.turn = 1
    gameObj.playerOnePoints = 0
    gameObj.playerTwoPoints = 0
    renderPlayerfield()
    renderScore()
}

document.addEventListener("DOMContentLoaded", function() {
    const playfieldTiles = document.querySelectorAll(".playfield div")

    for(let i=0; i<playfieldTiles.length; i++) {
        playfieldTiles[i].addEventListener("click", onFieldClick)
    }
    document.querySelector("#resetButton").addEventListener("click", onResetButtonClick)
})