class Stack {
    constructor() {
        this.stack = [];
    }

    get length() {
        return this.stack.length;
    }

    pop() {
        const last = this.stack[this.stack.length - 1];
        this.stack.pop();
        return last;
    }

    push(item) {
        this.stack.push(item);
    }

    push_items(items) {
        this.stack = this.stack.concat(items);
    }

    get top() {
        return this.stack[this.stack.length - 1];
    }
}

module.exports = Stack;