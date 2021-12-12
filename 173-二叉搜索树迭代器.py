# /**
#  * Definition for a binary tree node.
#  * public class TreeNode {
#  *     int val;
#  *     TreeNode left;
#  *     TreeNode right;
#  *     TreeNode() {}
#  *     TreeNode(int val) { this.val = val; }
#  *     TreeNode(int val, TreeNode left, TreeNode right) {
#  *         this.val = val;
#  *         this.left = left;
#  *         this.right = right;
#  *     }
#  * }
#  */
# class BSTIterator {
#     private ArrayList array = new ArrayList();
#     private int point = -1;

#     public BSTIterator(TreeNode root) {
#         //iterartion
#         Stack stack = new Stack();
#         stack.push(root);
#         while(!stack.empty()){
#             TreeNode t = (TreeNode)stack.peek();
#             while(t != null){
#                 stack.push(t.left);
#                 t = t.left;
#             }
#             stack.pop();
#             if(!stack.empty()){
#                 TreeNode cur = (TreeNode)stack.pop();
#                 array.add(cur.val);
#                 stack.push(cur.right);
#             }
#         }
#     }
    
#     public int next() {
#         point ++;
#         int nxt = (int)array.get(point);
#         return nxt;
#     }
    
#     public boolean hasNext() {
#         if(point < array.size()-1){
#             return true;
#         }
#         else{
#             return false;
#         }
#     }
# }

# /**
#  * Your BSTIterator object will be instantiated and called as such:
#  * BSTIterator obj = new BSTIterator(root);
#  * int param_1 = obj.next();
#  * boolean param_2 = obj.hasNext();
#  */