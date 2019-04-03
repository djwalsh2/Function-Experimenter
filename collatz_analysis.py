import pandas as pd

"""
Converts a value to decimal
"""
def binary_value(decimal):
    return "{0:08b}".format(decimal)

"""
Convert to binary and get first bit
"""
def get_first_bit(decimal):
    value = "{0:08b}".format(decimal)
    return value[0]

"""
Convert to binary and get last bit
"""
def get_last_bit(decimal):
    value = "{0:08b}".format(decimal)
    return value[-1]

"""
Read CSV into a dataframe
"""
df_collatz = pd.read_csv("collatz.csv")


"""
Create new pd column with binary values for input and output i.e x0,x5
"""
df_collatz['binary_input'] = df_collatz['x0'].apply(binary_value)
df_collatz['binary_output'] = df_collatz['x5'].apply(binary_value)

"""
Create new pd columns with first and last bits of x0 and x5
"""
df_collatz['x0_first_bit'] = df_collatz['x0'].apply(get_first_bit)
df_collatz['x0_last_bit'] = df_collatz['x0'].apply(get_last_bit)
df_collatz['x5_first_bit'] = df_collatz['x5'].apply(get_first_bit)
df_collatz['x5_last_bit'] = df_collatz['x5'].apply(get_last_bit)

"""
Print values
"""
print(df_collatz['x0_first_bit'].value_counts())
print(df_collatz['x0_last_bit'].value_counts())
print(df_collatz['x5_first_bit'].value_counts())
print(df_collatz['x5_last_bit'].value_counts())

"""
Print Dataframe
"""
print(df_collatz.to_string(index=False))
