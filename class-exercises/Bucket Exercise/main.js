const { State } = require("./State");
const StateMachine = require("./StateMachine");
const Stack = require("./Stack");
const Queue = require("./Queue");

const initial_state = new State(0,0);
const final_state = new State(2,0);

const bfs = () => {
    const sm = new StateMachine(initial_state, final_state);
    let to_visit = new Queue();
    to_visit.push(initial_state);

    while (to_visit.length > 0) {
        const state = to_visit.pop();
        sm.visit(state);

        if (sm.isFinished()) {
            sm.printSolution();
            return true;
        }

        to_visit.push_items(sm.getPossibleStates(state));
    }

    return false;   // No solution found
}

const dfs = (limit_depth) => {
    const sm = new StateMachine(initial_state, final_state);
    let to_visit = new Stack();
    to_visit.push(initial_state);

    while (to_visit.length > 0) {
        const state = to_visit.pop();

        // In case of limited depth, do not analise over-deep states
        if (limit_depth && state.depth > limit_depth) {
            continue;
        }

        sm.visit(state);

        if (sm.isFinished()) {
            sm.printSolution();
            return true;
        }

        to_visit.push_items(sm.getPossibleStates(state));
    }

    return false;   // No solution found
}

const iterative_deepening = () => {
    const sm = new StateMachine(initial_state, final_state);
    let depth = 1;

    while(!dfs(depth)) {
        depth++;
    }
}

console.log("--- Depth-First Search ---");
bfs();
console.log("--- Breadth-First Search ---");
dfs();
console.log("--- Iterative Deepening Search ---");
iterative_deepening();