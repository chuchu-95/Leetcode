# class FreqStack {
#     HashMap<Integer, Integer> freqMap;
#     HashMap<Integer, Stack<Integer>> stackMap;
#     int maxFreq;

#     public FreqStack() {
#         freqMap = new HashMap<>();
#         stackMap = new HashMap<>();
#         maxFreq = 0;
#     }
    
#     public void push(int val) {
#         int curFreq = freqMap.getOrDefault(val, 0) + 1;
#         freqMap.put(val, curFreq);
#         if(!stackMap.containsKey(curFreq)){
#             stackMap.put(curFreq, new Stack<Integer>());
#         }
#         stackMap.get(curFreq).add(val);
#         maxFreq = Math.max(maxFreq, curFreq);
#     }
    
#     public int pop() {
#         int mostVal = stackMap.get(maxFreq).pop();
#         freqMap.put(mostVal, maxFreq-1);
#         if(stackMap.get(maxFreq).size() == 0){
#             maxFreq --;
#         }
#         return mostVal;
#     }
# }

# /**
#  * Your FreqStack object will be instantiated and called as such:
#  * FreqStack obj = new FreqStack();
#  * obj.push(val);
#  * int param_2 = obj.pop();
#  */