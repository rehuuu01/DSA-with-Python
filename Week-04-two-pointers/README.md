# Day 14 – Two Pointer Technique

## Topics Covered
- Two Pointer Basics
- Palindrome Check (String)
- Container With Most Water

---

## Problems Solved

### 1️⃣ Check Palindrome (String)
**Problem:**  
Given a string, check whether it reads the same forward and backward.

**Approach (Two Pointers):**
- Use two pointers: one at the start, one at the end
- Compare characters at both pointers
- If mismatch → not a palindrome
- Move pointers inward until they meet

**Key Learning:**
- Two pointers help reduce unnecessary comparisons
- Early termination improves efficiency

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

### 2️⃣ Container With Most Water ⭐
**Problem:**  
Given heights of vertical lines, find two lines that together can store the maximum amount of water.

**Approach (Two Pointers):**
- Start with pointers at both ends (maximum width)
- Area is limited by the shorter height
- Move the pointer pointing to the shorter line
- Update maximum area at each step

**Key Insight:**
> Always move the pointer with the smaller height, because increasing the smaller height is the only way to possibly increase area.

**Why Two Pointers?**
- Avoids brute-force O(n²)
- Efficient elimination of impossible cases

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Overall Learnings
- Two pointer technique is powerful for array and string problems
- Pointer movement logic is more important than syntax
- Understanding constraints helps optimize from brute force to linear time

---

✅ Day 14 completed successfully  
