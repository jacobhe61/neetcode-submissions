class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    jump(nums: number[]): number {
        let count = 0
        let r = 0
        let l = 0
        while (r < nums.length-1) {
            let max = 0
            for (let i = l; i <= r; i++) {
                max = Math.max(max, i + nums[i])
            }
            l = r + 1
            r = max
            count++
        }
        return count
    }
}
