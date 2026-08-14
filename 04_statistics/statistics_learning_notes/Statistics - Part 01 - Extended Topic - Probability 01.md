# Probability — Confusion-Free Notes

## 1. Probability Kya Hoti Hai?
Probability ka simple meaning hai:
* **Kisi event ke hone ke chances kitne hain?**
* Probability kisi event ke occurrence ki likelihood/chance batati hai.

### Probability ki Range
$$0 \leq P(A) \leq 1$$

Iska matlab:
* $P(A) = 0 \rightarrow$ Event **impossible** hai
* $P(A) = 1 \rightarrow$ Event **definitely** hoga
* $0 < P(A) < 1 \rightarrow$ Event hone ke kuch chances hain

Probability ko percentage mein bhi likh sakte hain:
$$0.26 \times 100 = 26\%$$

---

## 2. Basic Probability Formula

$$\boxed{P(A) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}}}$$

Video mein isko:
$$\boxed{\text{True Outcomes} \div \text{Total Outcomes}}$$
ke concept se explain kiya gaya hai.

### Example 1: Coin Toss
Agar ek coin toss karte hain:
* **Possible outcomes:** $\{H, T\}$
* **Total outcomes:** $2$

#### Head ki Probability:
* Favorable outcome: $1$
* Total outcomes: $2$
* $P(H) = \frac{1}{2}$
* Similarly: $P(T) = \frac{1}{2}$

---

### Example 2: Dice
Ek dice ke possible outcomes:
$$\{1, 2, 3, 4, 5, 6\}$$
* **Total outcomes:** $6$

#### Probability of Getting 6:
* Favorable outcome: $1$
* $P(6) = \frac{1}{6}$
* Isi tarah $P(4) = \frac{1}{6}$ kyunki 4 sirf ek possible favorable outcome hai.

---

### Example 3: Cards
Ek standard deck mein:
* **Total cards:** $52$
* **Hearts:** $13$

#### Probability of Getting a Heart:
$$P(\text{Heart}) = \frac{13}{52} = \frac{1}{4}$$

Percentage:
$$\frac{1}{4} \times 100 = 25\%$$

$$\boxed{P(\text{Heart}) = 25\%}$$

---

## 3. Types of Events
Video mein teen types of events discuss kiye gaye hain:
1. **Independent Events**
2. **Dependent Events**
3. **Mutually Exclusive Events**

---

### 3.1 Independent Events
#### Meaning:
Two events independent hote hain jab:
> Ek event ke hone se doosre event ke hone par koi effect nahi padta.

Mathematically:
$$\boxed{P(A \cap B) = P(A) \times P(B)}$$

Yahan $A \cap B$ ka matlab hai: **A AND B dono events ka hona**.

#### Example: Two Coin Tosses
Suppose:
* **Event (A):** First toss = Head
* **Event (B):** Second toss = Tail

First toss ka result second toss ko affect nahi karta. Therefore, both events are independent.
* $P(A) = \frac{1}{2}$
* $P(B) = \frac{1}{2}$

$$P(A \cap B) = P(A) \times P(B) = \frac{1}{2} \times \frac{1}{2} = \boxed{\frac{1}{4}}$$

#### Logic Se Samjho:
Do coin tosses ke possible outcomes: $\{HH, HT, TH, TT\}$
* **Required result:** First = Head AND Second = Tail
* Sirf $HT$ favorable hai.
* So, $P(HT) = \frac{1}{4}$. Same answer multiplication rule se bhi aata hai.

#### Dice Example:
* First roll = 6 $\rightarrow P(6) = \frac{1}{6}$
* Second roll = 3 $\rightarrow P(3) = \frac{1}{6}$
* Dono rolls ek doosre ko affect nahi karte.

$$P(6 \text{ first AND } 3 \text{ second}) = \frac{1}{6} \times \frac{1}{6} = \boxed{\frac{1}{36}}$$

---

### 3.2 Dependent Events
#### Meaning:
Two events dependent hote hain jab:
> Ek event ke hone se doosre event ki probability change ho jaye.

$$\text{First Event} \rightarrow \text{Second Event ki Probability Change}$$

#### Example: Cards Without Replacement
Ek deck mein:
* Total cards = $52$
* Kings = $4$

**First Draw: King**
$$P(A) = \frac{4}{52}$$

Ab maan lo pehla card King nikla. Ab:
* Total cards remaining = $51$
* Kings remaining = $3$

**Second Draw: King**
$$P(B|A) = \frac{3}{51}$$

Yahan $B|A$ ka matlab hai: **B, given A** (ya A already happen ho chuka hai, ab B ki probability kya hai?).
Since first draw ne second draw ki probability change kar di:
$$\boxed{\text{These are dependent events}}$$

#### Dependent Events ka Multiplication Rule:
$$\boxed{P(A \cap B) = P(A) \times P(B|A)}$$

**Example:**
$$P(\text{First King AND Second King}) = \frac{4}{52} \times \frac{3}{51}$$

#### Independent vs Dependent Comparison:

| Feature | Independent Events | Dependent Events |
| :--- | :--- | :--- |
| **Effect** | One event does not affect the other | One event affects the other |
| **Probability** | Probability remains unchanged | Probability changes |
| **Formula** | $P(A \cap B) = P(A) P(B)$ | $P(A \cap B) = P(A) P(B|A)$ |
| **Example** | Repeated dice rolls | Cards without replacement |

**Main Difference:**
* **With replacement / no effect** $\rightarrow$ Independent
* **Without replacement / effect on next event** $\rightarrow$ Dependent

---

### 3.3 Mutually Exclusive Events
#### Meaning:
Two events mutually exclusive hote hain agar:
> Dono events ek hi time par happen nahi kar sakte.

Mathematically:
$$\boxed{P(A \cap B) = 0}$$

#### Example 1: One Coin Toss
Ek single coin toss mein Head ya Tail aa sakta hai, lekin Head AND Tail ek hi toss mein nahi aa sakte.
$$P(H \cap T) = 0$$

#### Example 2: One Dice Roll
Ek dice ko ek baar roll karne par 1 AND 6 ek saath nahi aa sakte.
$$P(1 \cap 6) = 0$$

So, these are mutually exclusive events.

---

## 4. Addition Rule
Addition Rule ka use hota hai jab question mein **OR / Either / At least one** ka concept ho.

Mathematically: $A \cup B$ ka matlab **A OR B**.

### General Addition Rule:
For any two events:
$$\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}$$

#### Why subtract $P(A \cap B)$?
Because A aur B ko add karte waqt common part do baar count ho jata hai. Isliye common part ko ek baar subtract karte hain.

#### Example: Red Card OR King
A standard deck mein:
* Red cards = $26$
* Kings = $4$
* Red Kings = $2$

$$P(\text{Red OR King}) = P(\text{Red}) + P(\text{King}) - P(\text{Red AND King})$$
$$= \frac{26}{52} + \frac{4}{52} - \frac{2}{52} = \frac{28}{52} = \boxed{\frac{7}{13}}$$

**Why subtract 2?**
Because the two red Kings Red cards mein pehle se count ho chuke hain aur Kings mein bhi, so they were counted twice.

---

## 5. Addition Rule for Mutually Exclusive Events
Agar A aur B mutually exclusive hain, to $P(A \cap B) = 0$.

General formula ban jata hai:
$$\boxed{P(A \cup B) = P(A) + P(B)}$$

### Example: Even OR Odd on a Dice
A fair dice:
* **Event A (Even Number):** $A = \{2, 4, 6\} \rightarrow P(A) = \frac{3}{6} = \frac{1}{2}$
* **Event B (Odd Number):** $B = \{1, 3, 5\} \rightarrow P(B) = \frac{3}{6} = \frac{1}{2}$

A number cannot be both even and odd $\rightarrow P(A \cap B) = 0$.

$$P(A \cup B) = \frac{1}{2} + \frac{1}{2} = \boxed{1}$$

---

### Addition vs Multiplication Rule

| Rule | Keyword / Meaning | Symbol | Formula |
| :--- | :--- | :--- | :--- |
| **Addition Rule** | A **OR** B | $\boxed{A \cup B}$ | $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ |
| **Multiplication Rule** | A **AND** B | $\boxed{A \cap B}$ | Indep: $P(A \cap B) = P(A)P(B)$ <br> Dep: $P(A \cap B) = P(A)P(B\|A)$ |

---

## 6. Multiplication Rule
Multiplication Rule is used to find: **Probability of two events happening together.**

### Independent Events:
If A and B are independent:
$$\boxed{P(A \cap B) = P(A) \times P(B)}$$
*(Use this when the first event does not affect the second event.)*

**Example:**
First dice roll = 6, Second dice roll = 3
$$P = \frac{1}{6} \times \frac{1}{6} = \boxed{\frac{1}{36}}$$

---

### Dependent Events:
If B depends on A:
$$\boxed{P(A \cap B) = P(A) \times P(B|A)}$$

**Example (Two Kings Without Replacement):**
* First King: $P(A) = \frac{4}{52}$
* Second King after first King drawn: $P(B|A) = \frac{3}{51}$

$$P(A \cap B) = \frac{4}{52} \times \frac{3}{51}$$

---

## 7. Conditional Probability
Conditional Probability ka basic idea:
> Agar humein already pata hai ke ek event happen ho chuka hai, to doosre event ki probability kya hogi?

$$\boxed{P(A|B)}$$
* **Read as:** Probability of A given B
* The condition is written after the vertical bar (`|`).

---

## 8. Contingency Table
Video mein conditional probability ko ek table ke through explain kiya gaya hai.

Suppose people ke baare mein do conditions hain:
1. Person likes Plane
2. Person likes Ship

| | Likes Ship | Does Not Like Ship | Total |
| :--- | :---: | :---: | :---: |
| **Likes Plane** | 2 | 5 | 7 |
| **Does Not Like Plane** | 4 | 3 | 7 |
| **Total** | 6 | 8 | 14 |

Total people = $2 + 5 + 4 + 3 = 14$

Is table ka purpose ye hai ke: **Condition ke basis par sample space ko restrict kiya ja sake.**

---

## 9. Conditional Probability Example

**Question:** A person likes Plane. What is the probability that they also like Ship?

**Important information:** Person already likes Plane.
So ab hum total 14 people consider nahi karenge. Sirf Plane-lovers consider honge ($2 + 5 = 7$).

In 7 people mein 2 people Ship bhi like karte hain:
$$\boxed{P(\text{Ship}|\text{Plane}) = \frac{2}{7}}$$

---

### The Most Important Conditional Probability Rule
For $\boxed{P(A|B)}$, think:
* **B is already known.**
* **Denominator** = total cases where B is true
* **Numerator** = cases where both A and B are true

Formula:
$$\boxed{P(A|B) = \frac{P(A \cap B)}{P(B)}}$$

In simple counting form:
$$\boxed{P(A|B) = \frac{\text{Number of A and B}}{\text{Number of B}}}$$

---

### The Best Way to Understand the Denominator
Suppose $P(\text{Ship}|\text{Plane})$, read it from right to left:
* **Step 1 (Condition):** Plane $\rightarrow$ So only Plane-lovers remain.
* **Step 2:** Among those Plane-lovers, ask: How many also like Ship?
* Therefore: $\frac{\text{Plane AND Ship}}{\text{Plane}}$

$$\boxed{P(A|B) = \frac{P(A \cap B)}{P(B)}}$$

* $A$ = event we want to find
* $B$ = condition already given
* $A \cap B$ = both events happen

---

## Final Confusion-Free Summary

```
PROBABILITY
│
├── Basic Probability
│   └── Favorable / Total
│
├── Types of Events
│   ├── Independent ────> One does not affect the other
│   ├── Dependent ──────> One affects the other
│   └── Mutually Exclusive ──> Cannot happen together
│
├── Probability Rules
│   ├── Addition Rule ──> OR (A ∪ B)
│   └── Multiplication Rule ──> AND (A ∩ B)
│
└── Conditional Probability
    └── GIVEN ──> P(A|B)
```

### Quick Reference Table:
* **OR** $\rightarrow$ Addition Rule
* **AND** $\rightarrow$ Multiplication Rule
* **GIVEN** $\rightarrow$ Conditional Probability
* **No effect** $\rightarrow$ Independent
* **Effect** $\rightarrow$ Dependent
* **Cannot happen together** $\rightarrow$ Mutually Exclusive
