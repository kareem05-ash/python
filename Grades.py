import pandas as pd 
import yagmail

df = pd.read_excel('results.xlsx')


target_codes = [91240168, 91240568, 91240572, 91240733]

filtered_df = df[df['Code'].isin(target_codes)]

email_body = filtered_df.to_string(index=False)

yag = yagmail.SMTP(user='kareem.aboelala05@eng-st.cu.edu.eg', password='pcqm lhtl lfub jncn')

yag.send(
    to='kareem.ash05@gmail.com',
    subject='selected student results',
    contents=email_body
)

print("Email sent successfully!")