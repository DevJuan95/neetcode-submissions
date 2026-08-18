class Node {
    Node next;
    Node prev;
    int value;

    public Node(int value){
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}
class Deque {
    Node dummyHead;
    Node dummyTail;

    public Deque() {
        this.dummyHead = new Node(0);
        this.dummyTail = new Node(0);
        this.dummyHead.next = this.dummyTail;
        this.dummyTail.prev = this.dummyHead;
    }

    public boolean isEmpty() {
        return this.dummyHead.next == this.dummyTail;
    }

    public void append(int value) {
       Node newNode = new Node(value);
       newNode.next = this.dummyTail;
       newNode.prev = this.dummyTail.prev;
       this.dummyTail.prev.next = newNode;
       this.dummyTail.prev = newNode;
    }

    public void appendleft(int value) {
        Node newNode = new Node(value);
        newNode.prev = this.dummyHead;
        newNode.next = this.dummyHead.next;
        this.dummyHead.next.prev = newNode;
        this.dummyHead.next = newNode;
    }

    public int pop() {
        if (isEmpty()){
            return -1;
        }
        int res = this.dummyTail.prev.value;
        
        this.dummyTail.prev = this.dummyTail.prev.prev;
        this.dummyTail.prev.next = this.dummyTail;

        return res;
    }

    public int popleft() {
        if(isEmpty()){
            return -1;
        }

        int res = this.dummyHead.next.value;

        this.dummyHead.next = this.dummyHead.next.next;
        this.dummyHead.next.prev = this.dummyHead;
        return res;
    }
}
