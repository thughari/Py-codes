document.addEventListener('DOMContentLoaded', function () {
    let GRID_SIZE = parseInt(prompt("Enter the number of grids (e.g., 9 for a 9x9 grid):")) || 9;
    let NUM_BOMBS = parseInt(prompt("Enter the number of bombs:")) || 10;

    const container = document.getElementById('container');
    let bombs = [];
    let revealedCells = 0;

    function initializeGame() {
        bombs = placeBombs();
        revealedCells = 0;
        container.innerHTML = '';
        for (let i = 0; i < GRID_SIZE; i++) {
            for (let j = 0; j < GRID_SIZE; j++) {
                const cell = document.createElement('div');
                cell.classList.add('cell');
                cell.setAttribute('data-x', i);
                cell.setAttribute('data-y', j);
                cell.textContent = '';
                container.appendChild(cell);
                cell.addEventListener('click', handleClick);
            }
        }
    }

    function placeBombs() {
        const bombPositions = [];
        while (bombPositions.length < NUM_BOMBS) {
            const x = Math.floor(Math.random() * GRID_SIZE);
            const y = Math.floor(Math.random() * GRID_SIZE);
            const position = `${x},${y}`;
            if (!bombPositions.includes(position)) {
                bombPositions.push(position);
            }
        }
        return bombPositions;
    }

    function handleClick(event) {
        const cell = event.target;
        if (cell.classList.contains('revealed')) return;

        const x = parseInt(cell.getAttribute('data-x'));
        const y = parseInt(cell.getAttribute('data-y'));
        const position = `${x},${y}`;
        if (bombs.includes(position)) {
            revealBombs();
            alert('Game Over!');
            initializeGame();
        } else {
            const bombsNearby = countBombsNearby(x, y);
            cell.textContent = bombsNearby || '';
            cell.classList.add('revealed');
            revealedCells++;
            if (revealedCells === GRID_SIZE * GRID_SIZE - NUM_BOMBS) {
                alert('Congratulations! You won!');
                initializeGame();
            }
        }
    }

    function countBombsNearby(x, y) {
        let count = 0;
        for (let i = x - 1; i <= x + 1; i++) {
            for (let j = y - 1; j <= y + 1; j++) {
                if (i >= 0 && i < GRID_SIZE && j >= 0 && j < GRID_SIZE) {
                    const position = `${i},${j}`;
                    if (bombs.includes(position)) {
                        count++;
                    }
                }
            }
        }
        return count;
    }

    function revealBombs() {
        const cells = document.querySelectorAll('.cell');
        cells.forEach(cell => {
            const x = parseInt(cell.getAttribute('data-x'));
            const y = parseInt(cell.getAttribute('data-y'));
            const position = `${x},${y}`;
            if (bombs.includes(position)) {
                cell.textContent = '💣';
            }
        });
    }

    initializeGame();
});
