# KcalScore – Wireframes (first draft)

Rough layouts of the 3 main screens. These will change after user testing.

## Screen 1: Search (Stories 1, 6)
```
┌─────────────────────┐
│     KcalScore       │
│                     │
│ Enter barcode:      │
│ [_______________]   │
│                     │
│ or search by name:  │
│ [_______________]   │
│                     │
│     [ Search ]      │
│                     │
│  [ Today's log → ]  │
└─────────────────────┘
```

## Screen 2: Food result (Stories 2, 3, 4, 8)
```
┌─────────────────────┐
│ ← Back              │
│ Margherita Pizza    │
│                     │
│   Food Score        │
│     20 / 100        │
│   (Poor)            │
│                     │
│ 235 kcal per 100 g  │
│                     │
│ Portion: [150] g    │
│ = 353 kcal          │
│                     │
│ [ Add to today ]    │
└─────────────────────┘
```
If the food isn't found, this screen shows: "Sorry, that product isn't in the database."

## Screen 3: Today's log (Stories 5, 7)
```
┌─────────────────────┐
│ Today               │
│                     │
│ Oats   150g 563kcal │
│ Pizza  150g 353kcal │
│ Apple  100g  52kcal │
│ ─────────────────── │
│ Total:      968 kcal│
│ Day score:  65 / 100│
│                     │
│ [ + Add food ]      │
└─────────────────────┘
```

## Screen flow
Search → Food result → Add to today → Today's log
