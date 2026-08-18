class ListNode {
    int val;
    ListNode next;

    public ListNode(int val, ListNode next){
        this.val = val;
        this.next = next;
    }

}
class LinkedList {
    ListNode head;
    ListNode tail;

    public LinkedList() {
        this.head = null;
        this.tail = this.head;
    }

    public int get(int index) {
       int i = 0;
       ListNode curr = head;

       while(curr != null) {
        if(index == i) {
            return curr.val;
        }
        i++;
        curr = curr.next;
       }
       return -1;
    }

    public void insertHead(int val) {
        if(head == null){
            head = new ListNode(val,null);
            tail = head;
        }else {
            var newNode = new ListNode(val, head);
            head = newNode;
        }
    }

    public void insertTail(int val) {
        if(tail !=null) {
            tail.next = new ListNode(val,null);
            tail = tail.next;
        }else{
            head = tail = new ListNode(val,null);
        }
    }

    public boolean remove(int index) {
        if(this.head == null){
            return false;
        }
        if(index == 0) {
            this.head = this.head.next;
            if(this.head == null) {
                this.tail = this.head;
            }
            return true;
        }
        ListNode curr = this.head;
        int i = 0;

        while (curr != null && i < index - 1) {
            curr = curr.next;
            i++;
        }

        if (curr == null || curr.next == null) return false;

        if (curr.next == this.tail) {
            this.tail = curr;
        }

        curr.next = curr.next.next;
        return true;
    }


    public ArrayList<Integer> getValues() {
        var res = new ArrayList<Integer>();

        ListNode curr = this.head;
        while(curr != null) {
            res.add(curr.val);
            curr = curr.next;
        }
        return res;
    }
}
