class MyQueueTS {
    stack1: number[];
    stack2: number[];
    
    constructor() {
        this.stack1 = [];
        this.stack2 = [];
    }

    push(x: number): void {
        this.stack1.push(x);
    }

    pop(): number {
        if (this.stack2.length === 0) {
            while (this.stack1.length !== 0) {
                this.stack2.push(this.stack1.pop() as number)
            }
        }
        return this.stack2.pop() as number;
    }

    peek(): number {
        if (this.stack2.length === 0) {
            while (this.stack1.length !== 0) {
                this.stack2.push(this.stack1.pop() as number)
            }
        }
        return this.stack2[this.stack2.length -1]
    }

    empty(): boolean {
        return Math.max(this.stack1.length, this.stack2.length) == 0
    }
}