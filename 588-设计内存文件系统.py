# class Dir{
#     HashMap<String, Dir> dir = new HashMap<>();
#     HashMap<String, String> files = new HashMap<>(); 
# }

# class FileSystem {
#     Dir root;
#     public FileSystem() {
#         root = new Dir();
#     }
    
#     public List<String> ls(String path) {
#         Dir point = root;
#         List<String> lsRes = new ArrayList<>();
#         //if path isn't root directory
#         if(!path.equals("/")){
#             String pathLst[] = path.split("/");
#             for(int i = 1; i < pathLst.length-1; i++){
#                 String curPath = pathLst[i];
#                 point = point.dir.get(curPath);
#             }
#             //point's position is the last one in pathLst
#             String endName = pathLst[pathLst.length-1];
#             //judge if it is file
#             if(point.files.containsKey(endName)){
#                 lsRes.add(endName); 
#                 return lsRes;
#             }
#             else{
#                 point = point.dir.get(endName);  
#             }
#         }
#         //if path == "/": directly return the below contains
#         lsRes.addAll(new ArrayList<>(point.dir.keySet()));
#         lsRes.addAll(new ArrayList<>(point.files.keySet()));
#         Collections.sort(lsRes); 
#         return lsRes;
#     }
    
#     public void mkdir(String path) {
#         //path must be a directory path
#         Dir point = root;
#         String pathLst[] = path.split("/");
#         for (int i = 1; i < pathLst.length; i++){
#             String curPath = pathLst[i];
#             if(!point.dir.containsKey(curPath)){
#                 Dir curDir = new Dir();
#                 point.dir.put(curPath, curDir);
#             }
#             point = point.dir.get(curPath);
#         }
#     }
    
#     public void addContentToFile(String filePath, String content) {
#         Dir point = root;
#         String filePathLst[] = filePath.split("/");
#         for (int i = 1; i < filePathLst.length-1; i ++){
#             String curPath = filePathLst[i];
#             point = point.dir.get(curPath);
#         }
#         String endName = filePathLst[filePathLst.length-1];
#         // add to exsited file
#         if(point.files.containsKey(endName)){
#             String orgContent = point.files.get(endName);
#             point.files.put(endName, orgContent+content);
#         }else{
#             point.files.put(endName, content);
#         }
#     }
    
#     public String readContentFromFile(String filePath) {
#         Dir point = root;
#         String readPathLst[] = filePath.split("/");
#         for(int i = 1; i < readPathLst.length-1; i++){
#             point = point.dir.get(readPathLst[i]);
#         }
#         return point.files.get(readPathLst[readPathLst.length-1]);
#     }
# }

# /**
#  * Your FileSystem object will be instantiated and called as such:
#  * FileSystem obj = new FileSystem();
#  * List<String> param_1 = obj.ls(path);
#  * obj.mkdir(path);
#  * obj.addContentToFile(filePath,content);
#  * String param_4 = obj.readContentFromFile(filePath);
#  */