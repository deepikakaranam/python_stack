class LinkedList
{
    constructor(value)
    {
        this.head = null;
        this.length = 0;
        this.addToHead(value);
    }

    addToHead(value) {
        const newNode = { value }; // 1
        newNode.next = this.head;  // 2
        this.head = newNode;       // 3
        this.length++;
        return this;
    }
 }


var test = new LinkedList('first')
.addToHead('second')
.addToHead('third');

console.log(test.length);
console.log(test.head.value);
console.log(test.head.next.value);
console.log(test.head.next.next.value);
