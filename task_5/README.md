# 📝 5 задание: Сумма минимальных разбиений для всех подотрезков

⏱ **Ограничение времени:** 3 секунды  
💾 **Ограничение памяти:** 512 МБ  

---

На день рождения Дмитрию подарили брусок! На данном бруске Дмитрий обнаружил **n** — 1 засечку. Данные засечки разбивают
брусок на **n** сегментов. Длина **i-го** сегмента равняется **а<sub>i</sub>**.


Дмитрию хочется распилить брусок на маленькие части. Распилы разрешается делать только в местах, в которых есть засечки
(но необязательно делать распил там, где есть засечка). Часть считается маленькой, если её длина не превосходит **s**.
При этом Дмитрию хочется тратить как можно меньше усилий, поэтому он хочет делать как можно меньше распилов.


Не успев приступить к делу, Дмитрий задумался: а если бы ему дали не целый брусок, а его подотрезок, который засечками
делился бы на части с длинами **а<sub>l</sub>, а<sub>l</sub>, a<sub>l+1</sub>,..., a<sub>r-1</sub>, a<sub>r</sub>**, то
на какое количество частей он должен бы был распилить брусок, чтобы каждая часть была маленькая? Такое значение
обозначим как **f(l, r)**.

## 🧩 **ЗАДАЧА:** 
Посчитайте, чему равняется $\sum_{l=1}^{n} \sum_{r=1}^{n} f(l, r)$

---

## 📥 Формат входных данных

- число **n** (1 ≤ n ≤ 250000) и **s** (1 ≤ s ≤ 10<sup>15</sup>) — количество сегментов, на которые брусок разбит
засечками, и максимальную возможную длину куска, чтобы он все еще считался маленьким
- значения **a<sub>1</sub>**, **a<sub>2</sub>**,..., **a<sub>n</sub>** (1 ≤ a<sub>i</sub> ≤ min(s, 10<sup>9</sup>)), где 
**a<sub>i</sub>** — длина **i-го** сегмента

---

## 📤 Формат выходных данных

- значение $\sum_{l=1}^{n} \sum_{r=1}^{n} f(l, r)$, где **f(l, r)** — минимальное количество частей, на которое должен быть разбит брусок из сегментов с длинами
**а<sub>l</sub>, а<sub>l+1</sub>,..., a<sub>r</sub>**, чтобы каждая из частей имела длину не более **s**.

---

## ⚠️ Замечание про минимальное разбиение 
- если **а** = \[3,2,2\] и **s** = 4, то минимальным по размеру будет разбиение на части \[3\] и \[2,2\].

- если **а** = \[5,1,5,1,5,1,5\] и **s** = 5, то минимальным по размеру будет разбиение на части
\[5\], \[1\], \[5\], \[1\], \[5\], \[1\], \[5\]

---

## 💬 Комментарий к примеру

📌 *f(1,1) + f(1,2) + f(1,3) + f(2,2) + f(2,3) + f(3,3) = 1 + 1 + 2 + 1 + 2 + 1 = 8*
