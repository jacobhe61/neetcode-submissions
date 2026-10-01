class Solution {
    /**
     * @param {number[]} hand
     * @param {number} groupSize
     * @return {boolean}
     */
    isNStraightHand(hand: number[], groupSize: number): boolean {
        const counts = new Map<number, number>();

        for (const n of hand) {
            if (!counts.has(n)) {
                counts.set(n, 0);
            }
            counts.set(n, counts.get(n)+1);
        }

        let i: number;
        for (const n of hand) {
            i = n;
            while (counts.has(i - 1) && counts.get(i - 1) > 0) {
                i -= 1;
            }
            while (i <= n) {
                while (counts.get(i) > 0) {
                    for (let j = 0; j < groupSize; j++) {
                        if (!counts.has(i + j)) {
                            return false;
                        }
                        counts.set(i + j, counts.get(i + j)-1);
                    }
                }
                i++;
            }
        }
        return true;
    }
}
