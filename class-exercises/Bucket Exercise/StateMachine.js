const { State, b1_max, b2_max } = require("./State");

const empty_b1 = (current_state) => {
    if (current_state.b1 === 0) {
        return undefined;
    }
    return new State(0, current_state.b2, current_state);
}

const empty_b2 = (current_state) => {
    if (current_state.b2 === 0) {
        return undefined;
    }
    return new State(current_state.b1, 0, current_state);
}

const fill_b1 = (current_state) => {
    if (current_state.b1 === b1_max) {
        return undefined;
    }
    return new State(b1_max, current_state.b2, current_state);
}

const fill_b2 = (current_state) => {
    if (current_state.b2 === b2_max) {
        return undefined;
    }
    return new State(current_state.b1, b2_max, current_state);
}

const b1_to_b2 = (current_state) => {
    if (current_state.isB2Full()) {
        return undefined;
    }

    const diff = Math.min(current_state.b1, b2_max - current_state.b2);
    if (diff === 0) {
        return undefined;
    }
    return new State(
        current_state.b1 - diff,
        current_state.b2 + diff, 
        current_state
    );
}

const b2_to_b1 = (current_state) => {
    if (current_state.isB1Full()) {
        return undefined;
    }

    const diff = Math.min(current_state.b2, b1_max - current_state.b1);
    if (diff === 0) {
        return undefined;
    }
    return new State(
        current_state.b1 + diff,
        current_state.b2 - diff, 
        current_state
    );
}

const transitions = [empty_b1, empty_b2, fill_b1, fill_b2, b1_to_b2, b2_to_b1];

class StateMachine {
    constructor(initial_state, final_state) {
        this.state = initial_state;
        this.final_state = final_state;
        this._visited = [initial_state];
    }

    getPossibleStates(state) {
        let possible_states = [];
        for (let transition of transitions) {
            let temp_state = transition(state);
            if (temp_state && !this.isStateVisited(temp_state)) {
                possible_states.push(temp_state);
            }
        }
        return possible_states;
    }

    isStateVisited(state) {
        for (let visited_state of this._visited) {
            if (state.equals(visited_state)) {
                return true;
            }
        }
        return false;
    } 

    isFinished() {
        return this.state.equals(this.final_state);
    }

    visit(state) {
        if (!this.isStateVisited(state)) {
            this._visited.push(state);
            this.state = state;
        }
    }

    printSolution() {
        const path = this.getSolutionPath();
        console.log("Number of steps: ", this._visited.length);
        console.log("Path size: ", path.length);
        console.log("Path: ");
        this.printPath(path);
    }

    printPath(path) {
        for (let state of path) {
            state.print();
        }
        console.log();
    } 

    getSolutionPath() {
        let path = [this.state];
        while (path[0].origin_state) {
            path.splice(0, 0, path[0].origin_state);
        }
        return path;
    }
}

module.exports = StateMachine;