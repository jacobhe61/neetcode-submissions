class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canJump(nums: number[]): boolean {
        let r = 0;
        let l = 0;
        while (r < nums.length-1) {
            let max = 0;
            for (let i = l; i <= r; i++) {
                max = Math.max(max, i + nums[i]);
            }
            if (max <= r) {
                return false;
            }
            l = r + 1;
            r = max;
        }
        return true;
    }
}
