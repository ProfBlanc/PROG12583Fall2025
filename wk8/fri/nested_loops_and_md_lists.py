data = [
    [1, 2, 3],
    ["hi", "bye", "dry"],
    [10.5, 22.1, 30.8]
]

d1 = [
    1,
    "one",
    True
]

for d in data:
    print(d)

print("*" * 10)

for row in data:
    for column in row:
        print(column, end="\t")
    print()  # new line


nested_supreme = [
    [
        [
            "hi", "there", "Everyone"
        ],
        [
            1, 2, 3, 4
        ]
    ],
    [
        {"first":"fun", "second": "times"},
        ("python", "rocks")
    ]
]

print(nested_supreme[0][1][1])
print("*" * 10)
for dimension1 in nested_supreme:
    for dimension2 in dimension1:
        for dimension3 in dimension2:
            print(dimension3, end=' ')
        print()