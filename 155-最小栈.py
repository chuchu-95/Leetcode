# class Node{
#     public int data;
#     public Node next;
#     public Node(int d){
#         this.data = d;
#     }
# }

# class MinStack {
#     private Node top;

#     public MinStack() {
#         //null
#     }
    
#     public void push(int val) {
#         Node p = new Node(val);
#         p.next = top;
#         top = p;
#     }
    
#     public void pop() {
#         if(top == null){
#             return;
#         }
#         else{
#             Node p = top;
#             top = top.next;
#         }
#     }
    
#     public int top() {
#         Node p = top;
#         return p.data; 
#     }
    
#     public int getMin() {
#         Node p = top;
#         int minRes = p.data;
#         while(p != null){
#             minRes = Math.min(minRes, p.data);
#             p = p.next;
#         }
#         return minRes;
#     }
# }

# /**
#  * Your MinStack object will be instantiated and called as such:
#  * MinStack obj = new MinStack();
#  * obj.push(val);
#  * obj.pop();
#  * int param_3 = obj.top();
#  * int param_4 = obj.getMin();
#  */