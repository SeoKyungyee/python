import pandas as pd

list1 = list(
    [
        ["한빛", "남자", "20", "180"],
        ["한결", "남자", "21", "177"],
        ["한라", "여자", "20", "160"],
    ]
)

col_names = ["이름", "성별", "나이", "키"]
df = pd.DataFrame(list1, columns=col_names)
print(df)

df.to_csv("file.csv", header=True, index=False)