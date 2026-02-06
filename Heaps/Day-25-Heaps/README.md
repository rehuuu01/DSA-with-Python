# Day 25 – Heaps / Priority Queue (Python)

## 📌 Topics Covered
Today’s focus was on **Heaps** and **Priority Queue** patterns using Python.

Heaps are extremely useful for problems involving:
- Kth largest / smallest elements
- Top K problems
- Efficient sorting

---

## 🧠 Key Concepts
- Min Heap vs Max Heap
- Complete Binary Tree property
- Python `heapq` (min heap)
- Manual heap construction using `heapify`

---

## 🧩 Problems Implemented

### 1️⃣ Kth Largest Element in an Array
**Approach:**  
- Maintain a **min heap of size k**
- Pop smallest element when size exceeds k

**Time:** O(n log k)  
**Space:** O(k)

---

### 2️⃣ Top K Frequent Elements
**Approach:**  
- Use `Counter` to count frequencies
- Min heap of size k storing `(frequency, element)`

**Time:** O(n log k)  
**Space:** O(n)

---

### 3️⃣ Heap Sort (In-Place)
**Approach:**  
- Build a **max heap** using manual `heapify`
- Repeatedly swap root with last element
- Heapify the reduced heap

**Time:** O(n log n)  
**Space:** O(1)  
⚠️ Not stable

---

## 📂 Folder Structure
Day-25-Heaps/
│
├── heap_sort.py
├── kth_largest.py
├── top_k_frequent.py
└── README.md


---

## 🎯 Key Takeaways
- For **Kth / Top K problems**, use a **min heap of size k**
- Python’s `heapq` is a **min heap**
- True Heap Sort requires **manual heapify**

---

## 🚀 Status
✅ Day 25 Completed
