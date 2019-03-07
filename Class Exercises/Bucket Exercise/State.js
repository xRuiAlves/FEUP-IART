const b1_max = 4;
const b2_max = 3;

class State {
    constructor(b1, b2, origin_state) {
        this._b1 = b1;
        this._b2 = b2;
        this._origin_state = origin_state;
        this._depth = origin_state ? (origin_state._depth + 1) : 0;
    }

    set b1(b1) {
        this._b1 = b1;
    }

    get b1() {
        return this._b1;
    }

    set b2(b2) {
        this._b2 = b2;
    }

    get b2() {
        return this._b2;
    }

    get origin_state() {
        return this._origin_state;
    }

    get depth() {
        return this._depth;
    }

    isB1Full() {
        return this.b1 === b1_max;
    }

    isB2Full() {
        return this.b2 === b2_max;
    }

    equals(other_state) {
        return (
            this.b1 === other_state.b1 &&
            this.b2 === other_state.b2
        )
    }

    print() {
        console.log("(" + this._b1 + ", " + this._b2 + ")");
    }
}

module.exports = {
    State,
    b1_max,
    b2_max
}