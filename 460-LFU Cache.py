# class Node{
#     Node prev, next;
#     int key, value;
#     int freq;
#     public Node(int key, int value){
#         this.key = key;
#         this.value = value;
#         freq = 1;
#     }
# }
# class DoubleLink{
#     Node head, tail;
#     int length;
#     public void addFirst(Node p){
#         if(head == null && tail == null){
#             head = tail = p;
#         }
#         Node h = head;
#         h.prev = p;
#         p.next = h;
#         head = p;
#         length ++;
#     }
#     public void remove(Node p){
#         if(head == p && tail == p){
#             head = tail = null;
#         }else if(head == p){
#             p.next.prev = null;
#             head = p.next;
#         }else if(tail == p){
#             p.prev.next = null;
#             tail = p.prev;
#         }else{
#             p.prev.next = p.next;
#             p.next.prev = p.prev;
#         }
#         length --;
#     }
#     public int removeLast(){
#         Node last = tail;
#         remove(tail);
#         return last.key;
#     }
# }

# class LFUCache {
#     HashMap<Integer, Node> keyMap;
#     HashMap<Integer, DoubleLink> freqMap;
#     int capacity;
#     int minFreq;

#     public LFUCache(int capacity) {
#         keyMap = new HashMap<>();
#         freqMap = new HashMap<>();
#         this.capacity = capacity;
#         minFreq = -1;
#     }
    
#     public int get(int key) {
#         if(!keyMap.containsKey(key)){
#             return -1;
#         }
#         int value = keyMap.get(key).value;
#         put(key, value);
#         return value;
#     }
    
#     public void put(int key, int value) {
#         if(capacity == 0){
#             return;
#         }
#         //in or not in 
#         Node curNode;
#         if(keyMap.containsKey(key)){
#             curNode = keyMap.get(key);
#             curNode.value = value;
#             keyMap.put(key, curNode);
#             update(curNode);
#         }else{
#             curNode = new Node(key, value);
#             if(capacity == keyMap.size()){
#                 DoubleLink minFreqLink = freqMap.get(minFreq);
#                 int lastKey = minFreqLink.removeLast();
#                 keyMap.remove(lastKey);
#             }
#             keyMap.put(key, curNode);
#             minFreq = 1;
#             DoubleLink nextLink = freqMap.getOrDefault(minFreq, new DoubleLink());
#             nextLink.addFirst(curNode);
#             freqMap.put(minFreq, nextLink);
#         }
#     }
#     public void update(Node node){
#         //the node must have existed in cache
#         DoubleLink oldLink = freqMap.get(node.freq);
#         oldLink.remove(node);
#         if(oldLink.length == 0 && node.freq == minFreq){
#             minFreq ++;
#         }
#         node.freq ++;
#         DoubleLink newLink = freqMap.getOrDefault(node.freq, new DoubleLink());
#         newLink.addFirst(node);
#         freqMap.put(node.freq, newLink);
#     }
# }

# /**
#  * Your LFUCache object will be instantiated and called as such:
#  * LFUCache obj = new LFUCache(capacity);
#  * int param_1 = obj.get(key);
#  * obj.put(key,value);
#  */