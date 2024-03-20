Reqs: 2 sorted arrays and you need to keep them sorted at ALL time

You have new empty space that you need to fill to reach ans. Check "simplest_merge_sort" to see the basic idea

If we have an unsorted array instead of 2 sorted arrays, we would need to convert that into 2 sorted arrays.

We either

1. recognize a pattern like those in "math" directory where the unsorted arr can have a pivot point that bisects 2 sorted arrays. O(n) time

2. divide and conquer to sort the unsorted arr O(log n) time
