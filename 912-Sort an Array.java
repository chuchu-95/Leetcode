class Solution {
    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length-1);
        return nums;
    }
    public void quickSort(int[]array, int low, int high){
        if(low < high){
            int part = partition(array, low, high);
            quickSort(array, low, part-1);
            quickSort(array, part+1, high);
        }
    }
    public int partition(int[]array, int low, int high){
        int point = low;
        int pivot = array[high];
        while(low < high){
            if(array[low] < pivot){
                int temp = array[low];
                array[low] = array[point];
                array[point] = temp;
                point ++;
            }
            low ++;
        }
        array[high] = array[point];
        array[point] = pivot;
        return point;
    }
}