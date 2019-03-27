class Queue {
    constructor() {
        this.queue = [];
    }

    get length() {
        return this.queue.length;
    }

    pop() {
        const first = this.queue[0];
        this.queue.splice(0, 1);
        return first;
    }

    push(item) {
        this.queue.push(item);
    }

    push_items(items) {
        this.queue = this.queue.concat(items);
    }

    get first() {
        return this.queue[0];
    }
}

module.exports = Queue;