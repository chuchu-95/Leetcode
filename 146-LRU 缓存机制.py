# class Node {
#     public int key, val;
#     public Node next, prev;
#     public Node(int k, int v) {
#         this.key = k;
#         this.val = v;
#     }
# }

# class DoubleList{
#     private Node head, tail;
#     private int length;

#     public void addFirst(Node node){
#         if(head == null){
#             head = tail = node;
#         }else{
#             Node h = head;
#             h.prev = node;
#             node.next = h;
#             head = node;
#         }
#         length ++;
#     }

#     public void remove(Node node){
#         if(head == node && tail == node){
#             head = null;
#             tail = null;
#         }else if(head == node){
#             node.next.prev = null;
#             head = node.next;
#         }else if(tail == node){
#             node.prev.next = null;
#             tail = node.prev;
#         }else{
#             node.prev.next = node.next;
#             node.next.prev = node.prev;
#         }
#         length --;
#     }
#     public Node removeLast(){
#         Node node = tail;
#         remove(tail);
#         return node;
#     }
#     public int getLength(){
#         return length;
#     }
# }

# class LRUCache {
#     //hashMap + doubleList
#     public HashMap<Integer, Node> map;
#     public DoubleList cache;
#     public int capacity;

#     public LRUCache(int capacity) {
#         this.capacity = capacity;
#         map = new HashMap<Integer, Node>();
#         cache = new DoubleList();
#     }
    
#     public int get(int key) {
#         if(!map.containsKey(key)){
#             return -1;
#         }
#         int value = map.get(key).val;
#         put(key, value);
#         return value;
#     }
    
#     public void put(int key, int value) {
#         Node newNode = new Node(key, value);
#         if(map.containsKey(key)){
#             cache.remove(map.get(key));
#             cache.addFirst(newNode);
#             map.put(key, newNode);
#         }
#         else{
#             if(cache.getLength() == capacity){
#                 Node last = cache.removeLast();
#                 map.remove(last.key);
#             }
#             cache.addFirst(newNode);
#             map.put(key, newNode);
#         }
#     }
# }

# /**
#  * Your LRUCache object will be instantiated and called as such:
#  * LRUCache obj = new LRUCache(capacity);
#  * int param_1 = obj.get(key);
#  * obj.put(key,value);
#  */