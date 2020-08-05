import pandas as pd
from tqdm import tqdm

df = pd.read_csv(r'F:\Documenti\machine_learning_avanzato\esercizi estivi\Book ratings\BX-Book-Ratings.csv', delimiter=';')

users = df['User-ID'].unique()
counts = {user: 0 for user in users}

for user in tqdm(users):
    counts[user] = len(df[df['User-ID'] == user])

train_df = pd.DataFrame(columns=["User-ID", "ISBN", "Book-Rating"])
test_df = pd.DataFrame(columns=["User-ID", "ISBN", "Book-Rating"])

for user in tqdm(users):
    df_user = df[df['User-ID'] == user]
    if len(df_user) > 5:
        train_n = int(0.8 * len(df_user))
        df_user_train = df_user.iloc[:train_n, :]
        df_user_test = df_user.iloc[train_n:, :]
        train_df = train_df.append(df_user_train)
        test_df = test_df.append(df_user_test)
        
assert len(df) == len(train_df) + len(test_df)

train_df.head()
test_df.head()

train_df.to_csv(r'F:\Documenti\machine_learning_avanzato\esercizi estivi\Book ratings\BX-Book-Ratings-train.csv', index=False)
test_df.to_csv(r'F:\Documenti\machine_learning_avanzato\esercizi estivi\Book ratings\BX-Book-Ratings-test.csv', index=False)